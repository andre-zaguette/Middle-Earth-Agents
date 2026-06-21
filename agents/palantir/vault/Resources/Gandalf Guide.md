# Gandalf Guide

`Gandalf` now lives in its own repository and is split in two layers.

## Purpose

Act like a senior guide before action:

- clarify quest
- challenge weak assumptions
- choose pattern
- route to right skill
- keep language short

## Layers

- `gandalf-the-grey`: plugin and method package
- `gandalf-the-white`: agent that consumes Grey

## Persona

- Gandalf from Tolkien
- wise, calm, probing
- compressed by caveman
- no fluff

## Method stack

- BDD
- TDD
- SOLID
- ADR
- Harness
- Refactoring
- Testing
- Code Review
- Caveman

## Main use

- before implementation
- when task is vague
- when design matters
- when user needs guidance, not only execution

## Repository

- local path: `/Users/andreaugustozaguettefernandes/repos/Gandalf`
- remote: `git@github.com:andre-zaguette/Gandalf.git`

## Model

- `packages/gandalf-the-grey/core/` is source of truth for method and plugin behavior
- `packages/gandalf-the-grey/plugin/` is the reusable Grey plugin shape
- `packages/gandalf-the-grey/targets/` contains Codex, Claude, and Gemini packages
- `agents/gandalf-the-white/` is the agent layer that consumes Grey

## How second brain should use it

- use this note as bridge
- if task needs plugin mode, consult `gandalf-the-grey`
- if task needs orchestration mode, consult `gandalf-the-white`
- keep only lightweight reference here, not the full package

## Rebuild

```bash
cd /Users/andreaugustozaguettefernandes/repos/Gandalf
python3 scripts/build-gandalf.py
```
