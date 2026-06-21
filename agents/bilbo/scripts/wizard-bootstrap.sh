#!/bin/bash
# Bilbo Bootstrap: PM/PO Context Loader

echo "=== BILBO BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f AGENT.md ] || [ -f agents/bilbo-baggins/AGENT.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"

echo ""
echo "--- Documentation State ---"
[ -f docs/contexto.md ] && echo "contexto.md: ✓" || echo "contexto.md: ✗ (required before any agent acts)"
[ -f docs/requirements.md ] && echo "requirements.md: ✓" || echo "requirements.md: ✗"
[ -f docs/user-stories.md ] && echo "user-stories.md: ✓" || echo "user-stories.md: ✗"
[ -f docs/open-questions.md ] && echo "open-questions.md: ✓" || echo "open-questions.md: ✗"

echo ""
echo "--- Open Questions ---"
if [ -f docs/open-questions.md ]; then
    OPEN=$(grep -c "| open" docs/open-questions.md 2>/dev/null || echo 0)
    echo "Open items: $OPEN"
fi

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md 2>/dev/null | grep "\- \[ \]" || echo "No QUEST_PROGRESS.md found"

echo ""
echo "--- Palantír ---"
[ -d ../palantir ] && echo "Palantír: ✓ linked" || echo "Palantír: ✗ (run scripts/link-agents.sh from Middle-Earth-Agents root)"
