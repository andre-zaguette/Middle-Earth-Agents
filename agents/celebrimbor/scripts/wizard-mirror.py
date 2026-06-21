#!/usr/bin/env python3
import sys

# Mirror of Galadriel (Celebrimbor): ReactJS Quality Self-Audit
RUBRIC = {
    "1. Boundary Classified": "Server ou Client Component? Justificativa documentada para `use client`?",
    "2. Data Strategy": "Estratégia de dados definida: static/dynamic/cached/server action?",
    "3. Type Contract": "Zero `any`. Todas as props têm interface TypeScript explícita?",
    "4. Proof Before Alloy": "Testes Vitest + RTL escritos para hooks e componentes críticos?",
    "5. Mithril Armor": "Scan executado: dangerouslySetInnerHTML, env vars no client, inputs sem validação?"
}

def self_audit():
    print("✨ Mirror of Galadriel (Celebrimbor): Reflecting upon your React work...")
    score = 0
    total = len(RUBRIC)

    for key, desc in RUBRIC.items():
        print(f"\n[ ] {key}: {desc}")
        val = input("Grade (1-5): ")
        try:
            score += int(val)
        except:
            pass

    final_score = (score / (total * 5)) * 100
    print(f"\n📊 Final Alignment: {final_score:.1f}%")

    if final_score < 80:
        print("⚠️ The Mirror shows shadows. Strengthen boundaries and types before signaling Boromir.")
        sys.exit(1)
    else:
        print("✅ The forge is clean. Signal Boromir with artifacts.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
