#!/usr/bin/env python3
import os, re

# Mithril Armor (Elrond): VueJS Security Scanner
SHADOW_PATTERNS = [
    (r'(?i)api_key.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]', "Secret: API key hardcoded"),
    (r'v-html\s*=', "XSS risk: v-html directive detected"),
    (r':\s*any\b|as\s+any\b', "Type discipline: `any` type detected"),
    (r'defineProps\(\)', "Untyped props: defineProps requires TypeScript generic or runtime definition"),
    (r'\$fetch\((?!.*server)', "Unguarded $fetch: consider useAsyncData for SSR"),
    (r'localStorage\.|sessionStorage\.', "Browser storage in potential SSR context (guard with process.client)"),
]

def scan(directory="."):
    print("🛡️ Mithril Armor (Elrond): Scanning Vue/Nuxt shadows...")
    issues = 0
    for root, _, files in os.walk(directory):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith((".vue", ".ts", ".js")):
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
    print("✨ No shadows. Vue/Nuxt code is shielded.")
    return True

if __name__ == "__main__":
    import sys
    if not scan():
        sys.exit(1)
