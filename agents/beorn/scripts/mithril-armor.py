#!/usr/bin/env python3
import os, re

# Mithril Armor (Beorn): NodeJS/NestJS Security Scanner
SHADOW_PATTERNS = [
    (r'(?i)api_key.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]', "Secret: API key hardcoded"),
    (r'(?i)password.*[=:].*[\'"][a-zA-Z0-9]{8,}[\'"]', "Secret: password hardcoded"),
    (r':\s*any\b|as\s+any\b', "Type discipline: `any` type detected"),
    (r'@Get\(|@Post\(|@Put\(|@Patch\(|@Delete\(', None),  # marker for next check
    (r'\.query\(.*\+|\.query\(.*`', "SQL injection risk: string concat in query"),
    (r'eval\(|new Function\(', "Injection risk: eval/new Function detected"),
    (r'process\.env\.[A-Z_]+(?!\s*\|\|)', "Unguarded env var access (add fallback or validation)"),
]

GUARD_PATTERN = re.compile(r'@UseGuards\(|@Public\(\)')

def scan(directory="."):
    print("🛡️ Mithril Armor (Beorn): Scanning Node/NestJS shadows...")
    issues = 0
    for root, _, files in os.walk(directory):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith((".ts", ".js")) and not file.endswith(('.spec.ts', '.test.ts')):
                path = os.path.join(root, file)
                try:
                    content = open(path, errors='ignore').read()
                    for entry in SHADOW_PATTERNS:
                        if entry[1] is None:
                            continue
                        pattern, label = entry
                        if re.search(pattern, content):
                            print(f"🔥 {label} in {path}")
                            issues += 1
                    # Check controllers for missing guards
                    if '.controller.' in file:
                        endpoints = re.findall(r'@(Get|Post|Put|Patch|Delete)\(', content)
                        if endpoints and not GUARD_PATTERN.search(content):
                            print(f"🔥 Controller without @UseGuards or @Public(): {path}")
                            issues += 1
                except:
                    pass
    if issues:
        print(f"\n❌ {issues} shadow(s) found. Fix before signaling Boromir.")
        return False
    print("✨ No shadows. Node/NestJS threshold is shielded.")
    return True

if __name__ == "__main__":
    import sys
    if not scan():
        sys.exit(1)
