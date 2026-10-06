#!/usr/bin/env node
import fs from "node:fs";
import process from "node:process";

export function checkPlan(text) {
  const problems = [];
  const add = (line, message) => problems.push({ line, message });
  const lines = text.split(/\r?\n/);
  let fenced = false;
  const visible = lines.map((line) => {
    if (/^\s*(```|~~~)/.test(line)) { fenced = !fenced; return ""; }
    return fenced ? "" : line;
  });
  if (!visible.some((line) => /^# \S/.test(line))) add(1, "Missing plan title");
  for (const heading of ["Goal", "Execution", "Risks"]) {
    const at = visible.findIndex((line) => line === `## ${heading}`);
    const next = at < 0 ? 0 : visible.findIndex((line, i) => i > at && /^## /.test(line));
    const body = at < 0 ? "" : visible.slice(at + 1, next < 0 ? undefined : next).join("\n");
    if (at < 0 || !body.trim()) add(Math.max(at + 1, 1), `Missing ${heading} section or content`);
  }
  const units = visible.flatMap((line, index) => /^## Unit \d+: \S/.test(line) ? [index] : []);
  if (units.length === 0) add(1, "No implementation units");
  const unitNumbers = new Set();
  for (const start of units) {
    const number = Number(visible[start].match(/^## Unit (\d+):/)[1]);
    if (unitNumbers.has(number)) add(start + 1, "Duplicate unit number");
    unitNumbers.add(number);
    let end = visible.findIndex((line, i) => i > start && /^## /.test(line));
    if (end < 0) end = visible.length;
    const sections = new Map();
    let current;
    for (let i = start + 1; i < end; i++) {
      if (visible[i].startsWith("### ")) {
        current = visible[i].slice(4);
        sections.set(current, { line: i + 1, body: [] });
      } else if (current) sections.get(current).body.push(visible[i]);
    }
    for (const name of ["Depends on", "Files", "Build", "Acceptance", "Verify", "Review and delivery"]) {
      const section = sections.get(name);
      if (!section || !section.body.join("\n").trim()) {
        add(start + 1, `Unit ${number} missing ${name} content`);
      } else if (name !== "Depends on" && !section.body.some((line) => /^\s*- \[[ x]\] \S/.test(line))) {
        add(section.line, `Unit ${number} ${name} has no concrete checklist item`);
      }
    }
    const verify = sections.get("Verify");
    if (verify) for (const dimension of ["Unit", "Live", "Perf"]) {
      const item = verify.body.find((line) => new RegExp(`^\\s*- \\[[ x]\\] ${dimension}: \\S`).test(line));
      if (!item) add(verify.line, `Unit ${number} lacks ${dimension} evidence or N/A reason`);
      else if (new RegExp(`${dimension}: N/A\\s*$`, "i").test(item)) {
        add(verify.line, `Unit ${number} ${dimension} N/A needs a reason`);
      }
    }
  }
  visible.forEach((line, i) => {
    if (/<[^>]+>/.test(line)) add(i + 1, "Unfilled template placeholder");
    if (/\b(?:TODO|TBD)\b/.test(line)) add(i + 1, "Unresolved checklist content");
  });
  return problems;
}

if (process.argv[1] && fs.realpathSync(process.argv[1]) === fs.realpathSync(new URL(import.meta.url))) {
  const file = process.argv[2];
  if (!file) { console.error("Usage: node check-plan.mjs <plan.md>"); process.exit(2); }
  try {
    const problems = checkPlan(fs.readFileSync(file, "utf8"));
    for (const { line, message } of problems) console.error(`${file}:${line}: ${message}`);
    if (!problems.length) console.log("Plan structure and evidence coverage verified.");
    process.exitCode = problems.length ? 1 : 0;
  } catch (error) { console.error(error.message); process.exitCode = 2; }
}
