#!/bin/bash
# Galadriel Bootstrap: UI/UX Context Loader

echo "=== GALADRIEL BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f AGENT.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"
[ -f docs/contexto.md ] && echo "Context: ✓" || echo "Context: ✗"

echo ""
echo "--- Design System State ---"
[ -d docs/design-tokens ] && echo "Design Tokens: ✓" || echo "Design Tokens: ✗ (define before styling)"
[ -f docs/design-tokens/tokens.md ] && echo "Token Map: ✓" || echo "Token Map: ✗"

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md 2>/dev/null | grep "\- \[ \]"
