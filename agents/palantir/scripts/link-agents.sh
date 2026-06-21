#!/usr/bin/env bash
set -euo pipefail

ROOT="${SECOND_BRAIN_ROOT:-$HOME/SecondBrain}"
TARGET_DIR="${1:-$(pwd)}"

ln -sf "$ROOT/AGENTS.md" "$TARGET_DIR/AGENTS.md"
ln -sf "$ROOT/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"

echo "Linked AGENTS.md and CLAUDE.md into $TARGET_DIR"
