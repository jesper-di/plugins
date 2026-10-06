import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("worktree_audit", ROOT / "skills/poteto-mode/scripts/worktree_audit.py")
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)


class AuditTests(unittest.TestCase):
    def test_spaced_paths_dirty_work_and_explicit_history(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo with spaces"
            other = Path(temp) / "other worktree"
            repo.mkdir()
            def run(*args):
                subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)
            run("init", "-b", "main")
            run("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "--allow-empty", "-m", "initial")
            run("worktree", "add", "-b", "task", str(other))
            (other / "untracked.txt").write_text("Retained work")
            rows = audit_module.audit(repo, base="main")
            self.assertEqual(len(rows), 2)
            task = next(row for row in rows if row["path"] == str(other))
            self.assertTrue(task["dirty"])
            self.assertEqual(task["recommendation"], "hold")
            self.assertEqual(task["matching_transcripts"], [])
            self.assertEqual((other / "untracked.txt").read_text(), "Retained work")
            history = Path(temp) / "authorized history"
            history.mkdir()
            (history / "one.jsonl").write_text('"' + str(other) + '/untracked.txt"')
            rows = audit_module.audit(repo, "main", history)
            task = next(row for row in rows if row["path"] == str(other))
            self.assertEqual(task["matching_transcripts"], [str(history / "one.jsonl")])


if __name__ == "__main__":
    unittest.main()
