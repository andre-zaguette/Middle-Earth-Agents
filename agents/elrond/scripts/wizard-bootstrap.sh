#!/bin/bash
# Elrond Bootstrap: VueJS Context Loader

echo "=== ELROND BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f AGENT.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"
[ -f docs/contexto.md ] && echo "Context: ✓" || echo "Context: ✗"

echo ""
echo "--- Vue/Nuxt Harness ---"
[ -f package.json ] && echo "Package: ✓" || echo "Package: ✗"
[ -f nuxt.config.ts ] && echo "Nuxt: ✓" || echo "Nuxt: ✗ (plain Vue)"
[ -f vitest.config.ts ] || grep -q '"vitest"' package.json 2>/dev/null && echo "Vitest: ✓" || echo "Vitest: ✗"

echo ""
echo "--- API Contracts in Palantír ---"
[ -d docs/archive/contracts ] && ls docs/archive/contracts/ 2>/dev/null || echo "No contracts archived yet"

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md 2>/dev/null | grep "\- \[ \]"
