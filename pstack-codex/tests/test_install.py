import importlib.util
from pathlib import Path
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pstack_install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.target = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_discovery_paths_and_native_agents(self):
        instructions = self.target / "AGENTS.md"
        instructions.write_text("Existing project instructions.\n")
        installed = installer.install(self.target)
        self.assertEqual(len(installed), 59)
        for skill in (ROOT / "skills").iterdir():
            if (skill / "SKILL.md").is_file():
                link = self.target / ".agents/skills" / skill.name
                self.assertEqual(link.resolve(), skill.resolve())
                self.assertTrue((link / "SKILL.md").is_file())
        for role in (self.target / ".codex/agents").glob("*.toml"):
            data = tomllib.loads(role.read_text())
            self.assertIn(str(ROOT), data["developer_instructions"])
        self.assertEqual(instructions.read_text(), "Existing project instructions.\n")
        self.assertFalse((self.target / ".codex/config.toml").exists())
        self.assertEqual(installer.install(self.target), [])

    def test_conflict_rejects_entire_install_without_writes(self):
        conflict = self.target / ".agents/skills/why"
        conflict.mkdir(parents=True)
        (conflict / "SKILL.md").write_text("user-owned skill")
        before = set(self.target.rglob("*"))
        with self.assertRaisesRegex(ValueError, "before writing"):
            installer.install(self.target)
        self.assertEqual(set(self.target.rglob("*")), before)
        self.assertEqual((conflict / "SKILL.md").read_text(), "user-owned skill")

    def test_dry_run_and_agents_only(self):
        self.assertEqual(len(installer.install(self.target, dry_run=True)), 59)
        self.assertEqual(list(self.target.iterdir()), [])
        self.assertEqual(len(installer.install(self.target, agents_only=True)), 4)
        self.assertFalse((self.target / ".agents").exists())

    def test_symlink_parent_cannot_write_outside_project(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.target / ".codex").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "Unsafe parent"):
                installer.install(self.target)
            self.assertEqual(list(Path(outside).iterdir()), [])
            self.assertFalse((self.target / ".agents").exists())

    def test_existing_agent_is_preserved(self):
        agent = self.target / ".codex/agents/poteto-agent.toml"
        agent.parent.mkdir(parents=True)
        agent.write_text('name = "user-owned"\n')
        with self.assertRaises(ValueError):
            installer.install(self.target)
        self.assertEqual(agent.read_text(), 'name = "user-owned"\n')


if __name__ == "__main__":
    unittest.main()
