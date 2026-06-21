#!/bin/bash
# Boromir Bootstrap Script
# Initializes and verifies the testing harness for our polyglot stack.

echo "Boromir: Initializing and verifying test harness..."

# Verify Python/Pytest
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    if ! pytest --version &> /dev/null; then
        echo "Boromir Error: pytest not found or misconfigured."
    else
        echo "Boromir: Pytest verified."
    fi
fi

# Verify Node.js/Vitest/Playwright
if [ -f "package.json" ]; then
    if ! command -v npx &> /dev/null; then
        echo "Boromir Error: Node.js/npm not found."
    else
        echo "Boromir: Checking Vitest and Playwright..."
        if npx vitest --version &> /dev/null; then echo "Boromir: Vitest verified."; else echo "Boromir Warning: Vitest missing."; fi
        if npx playwright --version &> /dev/null; then echo "Boromir: Playwright verified."; else echo "Boromir Warning: Playwright missing."; fi
    fi
fi

echo "Boromir: Initialization complete."
