#!/usr/bin/env python3
import sys

# Mirror of Galadriel: UI/UX Quality Self-Audit
RUBRIC = {
    "1. Vision Transcribed": "O componente foi descrito visualmente (Eye of Sauron) antes do CSS?",
    "2. Token-First": "Todos os valores visuais (cores, espaçamento, fontes) usam design tokens?",
    "3. States Covered": "Todos os estados foram cobertos: default, loading, error, empty, focus, hover?",
    "4. Accessibility Gate": "WCAG 2.1 AA: contraste, ARIA, navegação por teclado, focus management?",
    "5. Design Spec Signed": "O contrato de componente (props/slots/eventos) foi assinado com Celebrimbor/Elrond?"
}

def self_audit():
    print("✨ Mirror of Galadriel: Reflecting upon your UI work...")
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
        print("⚠️ The Mirror shows shadows. Refine the design before signaling Boromir.")
        sys.exit(1)
    else:
        print("✅ The vision is pure. Signal Boromir and the frontend agent.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
