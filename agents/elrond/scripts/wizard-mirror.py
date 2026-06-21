#!/usr/bin/env python3
import sys

# Mirror of Galadriel (Elrond): VueJS Quality Self-Audit
RUBRIC = {
    "1. State Ownership": "State ownership classificado: local/shared/server antes de implementar?",
    "2. Composition API": "Todos os componentes usam `<script setup>`? Zero Options API em código novo?",
    "3. Proof Before Alloy": "Testes Vitest escritos para composables e componentes críticos?",
    "4. Contract Validated": "Contrato de API validado no Palantír antes de qualquer fetch?",
    "5. Design Spec": "Design spec recebida da Galadriel antes de construir componente visual?"
}

def self_audit():
    print("✨ Mirror of Galadriel (Elrond): Reflecting upon your Vue work...")
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
        print("⚠️ The Mirror shows shadows. Strengthen composition and tests before signaling Boromir.")
        sys.exit(1)
    else:
        print("✅ The work is pure. Signal Boromir with artifacts.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
