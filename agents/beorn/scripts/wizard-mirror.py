#!/usr/bin/env python3
import sys

# Mirror of Galadriel (Beorn): NodeJS/NestJS Quality Self-Audit
RUBRIC = {
    "1. DTO-First": "Todo input externo validado via DTO + class-validator antes de entrar na lógica?",
    "2. Module Isolation": "Módulo não tem dependências circulares? Exports explícitos?",
    "3. Contract Published": "Contrato de API publicado no Palantír antes de agentes consumidores buildarem?",
    "4. Proof Before Alloy": "Testes Jest: unit para service + integration para controller?",
    "5. Mithril Armor": "Scan executado: secrets hardcoded, endpoints sem auth guard, SQL injection?"
}

def self_audit():
    print("✨ Mirror of Galadriel (Beorn): Reflecting upon your Node work...")
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
        print("⚠️ The threshold is not secure. Strengthen DTOs and tests before signaling Boromir.")
        sys.exit(1)
    else:
        print("✅ The threshold holds. Signal Boromir with artifacts and API contracts.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
