#!/bin/bash
# The Gates of Argonath: Git Pre-commit Hook — Bilbo Baggins

echo "🛡️ The Gates of Argonath: Inspecting the Caravan..."

# 0. Auto-rebuild targets when core files change
CORE_CHANGED=$(git diff --cached --name-only | grep "^packages/bilbo/core/")
if [ -n "$CORE_CHANGED" ]; then
    echo "📜 Core files changed — rebuilding targets..."
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    python3 "$SCRIPT_DIR/build-bilbo.py"
    if [ $? -ne 0 ]; then
        echo "❌ ERROR: build-bilbo.py failed. Fix core files before committing."
        exit 1
    fi
    git add packages/bilbo/plugin/skills/bilbo/ packages/bilbo/targets/claude/bilbo/
    echo "✅ Targets rebuilt and staged."
fi

# 1. Check Progress Log
if [ ! -f QUEST_PROGRESS.md ]; then
    echo "❌ ERROR: QUEST_PROGRESS.md is missing. No documentation shall pass without a record."
    exit 1
fi

# 2. Check if Progress was updated
if ! git diff --cached --name-only | grep -q "QUEST_PROGRESS.md"; then
    echo "⚠️  WARNING: QUEST_PROGRESS.md not staged. Did you record this quest's steps?"
fi

# 3. Check contexto.md exists before any code docs are committed
DOCS_CHANGED=$(git diff --cached --name-only | grep "^docs/")
if [ -n "$DOCS_CHANGED" ]; then
    if [ ! -f docs/contexto.md ]; then
        echo "❌ ERROR: docs/contexto.md is missing. The map must be drawn before documentation is committed."
        exit 1
    fi
fi

# 4. Check for incomplete requirements (placeholder rows)
if git diff --cached --name-only | grep -q "docs/requirements.md"; then
    if grep -q "| REQ-001 | |" docs/requirements.md 2>/dev/null; then
        echo "❌ ERROR: requirements.md has empty rows. Fill in all requirement fields before committing."
        exit 1
    fi
fi

# 5. Check for unowned open questions
if [ -f docs/open-questions.md ]; then
    UNOWNED=$(grep "| open" docs/open-questions.md | grep -c "| |" 2>/dev/null || echo 0)
    if [ "$UNOWNED" -gt 0 ]; then
        echo "⚠️  WARNING: $UNOWNED open question(s) have no owner. Assign owners before the quest proceeds."
    fi
fi

echo "✅ The Gates are open. Pass, traveler."
exit 0
