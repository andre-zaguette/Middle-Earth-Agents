#!/bin/bash
# Beorn Bootstrap: NodeJS/NestJS Context Loader

echo "=== BEORN BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f AGENT.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"
[ -f docs/contexto.md ] && echo "Context: ✓" || echo "Context: ✗"

echo ""
echo "--- NestJS Harness ---"
[ -f package.json ] && echo "Package: ✓" || echo "Package: ✗"
[ -f nest-cli.json ] && echo "NestJS: ✓" || echo "NestJS: ✗ (plain Node)"
[ -f tsconfig.json ] && grep -q '"strict": true' tsconfig.json && echo "TypeScript strict: ✓" || echo "TypeScript strict: ✗ (required)"
grep -q '"jest"' package.json 2>/dev/null && echo "Jest: ✓" || echo "Jest: ✗"

echo ""
echo "--- Published Contracts ---"
[ -d docs/archive/contracts ] && ls docs/archive/contracts/ 2>/dev/null || echo "No contracts published yet"

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md 2>/dev/null | grep "\- \[ \]"
