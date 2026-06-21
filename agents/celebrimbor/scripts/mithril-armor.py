#!/usr/bin/env python3
import os, re

# Mithril Armor (Celebrimbor): React/Next Security Scanner
SHADOW_PATTERNS = [
    (r'(?i)api_key.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]', "Secret: API key hardcoded"),
    (r'dangerouslySetInnerHTML', "XSS risk: dangerouslySetInnerHTML detected"),
    (r'NEXT_PUBLIC_.*SECRET|NEXT_PUBLIC_.*KEY|NEXT_PUBLIC_.*PASSWORD', "Secret exposed to client via NEXT_PUBLIC_"),
    (r':\s*any\b|as\s+any\b', "Type discipline: `any` type detected"),
    (r'"use client"[\s\S]{0,200}useEffect|"use client"[\s\S]{0,200}useState', "Review: `use client` with hooks — is this justified?"),
    (r'fetch\([\'"`][^\'"`]+[\'"`]\)(?!.*cache)', "No cache strategy on fetch — add cache/revalidate config"),
]

def scan(directory="."):
    print("🛡️ Mithril Armor (Celebrimbor): Scanning React/Next shadows...")
    issues = 0
    for root, _, files in os.walk(directory):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith((".tsx", ".ts", ".jsx", ".js")):
                path = os.path.join(root, file)
                try:
                    content = open(path, errors='ignore').read()
                    for pattern, label in SHADOW_PATTERNS:
                        if re.search(pattern, content):
                            print(f"🔥 {label} in {path}")
                            issues += 1
                except:
                    pass
    if issues:
        print(f"\n❌ {issues} shadow(s) found. Fix before signaling Boromir.")
        return False
    print("✨ No shadows. React/Next code is shielded.")
    return True

if __name__ == "__main__":
    import sys
    if not scan():
        sys.exit(1)
