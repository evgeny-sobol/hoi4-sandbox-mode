# Civil-war cap

Status: ready-for-agent
Type: spec

## Context

The AI civil-war cap drops from three concurrent wars to one. A civil war
started by a national focus (a focus ignition) is exempt from the cap and from
a new 0-12 month cooldown, and a running focus ignition still occupies the
single slot. This changes the existing civil-war rules; it is not a new system.

The design of record is the GDD and the ADR; this spec only anchors the
tickets:

- `docs/gdd/Civil Wars.md` - "Model" (Cap, Focus exemption, Cooldown), "AI weighting", "Coverage"
- `docs/adr/0006-focus-ignitions-exempt-from-the-ai-civil-war-cap.md`
- `CONTEXT.md` - Civil-war cap / Focus ignition / Event/mission ignition / Civil-war cooldown

## Tickets

01 (core) blocks 02-05. 06 is independent. 07 is the acceptance run.
