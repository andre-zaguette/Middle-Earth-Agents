#!/usr/bin/env python3
import os, re

# Mithril Armor (Galadriel): UI/CSS Security & Quality Scanner
SHADOW_PATTERNS = [
    (r'(?i)api_key.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]', "Secret hardcoded in CSS/JS"),
    (r'dangerouslySetInnerHTML', "XSS risk: dangerouslySetInnerHTML detected"),
    (r'v-html\s*=', "XSS risk: v-html directive detected"),
    (r'#[0-9a-fA-F]{3,6}(?!\s*[;}])', "Hardcoded color (use design token)"),
    (r'font-size:\s*\d+px', "Hardcoded font-size (use token/rem)"),
    (r'(?<!\w)outline:\s*none|outline:\s*0', "Accessibility risk: outline removed (breaks keyboard focus)"),
]

def scan(directory="."):
    print("🛡️ Mithril Armor (Galadriel): Scanning for UI shadows...")
    issues = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".css", ".scss", ".vue", ".tsx", ".jsx", ".ts", ".js")):
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
    print("✨ No shadows. The design is shielded.")
    return True

if __name__ == "__main__":
    import sys
    if not scan():
        sys.exit(1)
