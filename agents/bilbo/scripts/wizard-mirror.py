#!/usr/bin/env python3
import sys

# Mirror of Galadriel (Bilbo): PM/PO Quality Self-Audit
RUBRIC = {
    "1. contexto.md": "O arquivo docs/contexto.md existe e define quest, objetivo, danger, scope e agentes necessários?",
    "2. Requirements": "Todos os requisitos têm ID, descrição, prioridade (must/should/could) e agente responsável?",
    "3. Acceptance Criteria": "Cada requisito tem ao menos um critério de aceitação no formato Given/When/Then?",
    "4. Scope Boundary": "As listas IN / OUT / DEFERRED estão explícitas e sem ambiguidade?",
    "5. Open Questions": "Todas as questões abertas estão documentadas com owner e deadline?",
}

def self_audit():
    print("✨ Mirror of Galadriel (Bilbo): Reflecting upon your documentation...")
    score = 0
    total = len(RUBRIC)

    for key, desc in RUBRIC.items():
        print(f"\n[ ] {key}: {desc}")
        val = input("Grade (1-5): ")
        try:
            score += int(val)
        except Exception:
            pass

    final_score = (score / (total * 5)) * 100
    print(f"\n📊 Final Alignment: {final_score:.1f}%")

    if final_score < 80:
        print("⚠️  The map is not ready. Strengthen requirements and acceptance criteria before signaling Gandalf.")
        sys.exit(1)
    else:
        print("✅ The map is drawn. Signal Gandalf with SIGNAL_PROJECT_SCOPED.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
