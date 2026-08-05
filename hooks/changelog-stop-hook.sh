#!/usr/bin/env bash
# dokit — Claude Code Stop hook: every change gets a changelog entry.
#
# Blocks the end of a session that left changes in the working tree without
# a new document in docs/changelog/ for today ({date}_{title}.md). This is a
# safety net behind the SKILL.md rule; the entry itself is written by Claude.
#
# Register in the project's .claude/settings.json:
#
#   {
#     "hooks": {
#       "Stop": [
#         { "hooks": [ { "type": "command",
#           "command": "bash .claude/skills/dokit/hooks/changelog-stop-hook.sh" } ] }
#       ]
#     }
#   }
#
# The feature is on by default; remove the hook registration (and tell Claude)
# to turn per-change changelog entries off.

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
command -v git >/dev/null 2>&1 || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Feature applies only after docs/changelog/ exists (init_docs.py creates it).
[ -d docs/changelog ] || exit 0

today="$(date +%F)"

# A changelog entry for today, in any state: untracked, staged, or committed.
entry="$(ls docs/changelog/"${today}"_*.md 2>/dev/null | head -1)"

# Any pending change that is not itself a changelog entry?
dirty="$(git status --porcelain 2>/dev/null | grep -v 'docs/changelog/' | head -1)"

if [ -n "$dirty" ] && [ -z "$entry" ]; then
    cat >&2 <<EOF
dokit: this session changed files but wrote no changelog entry.
Create docs/changelog/${today}_<kebab-title>.md from
docs/templates/changelog-entry-template.md (Summary, Files Changed,
Tests Run, Follow-ups / Risks) before finishing.
EOF
    exit 2
fi

exit 0
