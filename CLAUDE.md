# Claude Code - Second Brain

This project uses a **skills system** for progressive context disclosure.
Skills are loaded on-demand — only when triggered — keeping every session lean.

## Skills Index

| Skill | Trigger | What it does |
|-------|---------|--------------|
| `brand-voice-generator` | "create brand", "brand setup" | Generates brand.json, config.json, brand-system.md, tone-of-voice.md |
| `mcp-client` | "use MCP", "connect to <server>" | Connects to any MCP server without bloating context |
| `pptx-generator` | "create presentation", "make slides", "LinkedIn carousel" | Generates branded PPTX/PDF using python-pptx |
| `sop-creator` | "create SOP", "write runbook", "document process" | Produces scannable, actionable technical documentation |
| `skill-creator` | "create skill", "new skill", "build skill" | Guides creation of new modular skills |
| `remotion` | "Remotion", "create video", "remotion-videos/" | Programmatic video creation with React/Remotion |

## How Skills Work

Each skill lives in `.claude/skills/<name>/SKILL.md`.  
When you trigger a skill by name or keyword, Claude reads its SKILL.md (≤5k words) and any reference files only as needed.  
Nothing is pre-loaded into context — that's how tokens stay low.

## Project Notes

- Skills reference files live in `.claude/skills/<name>/references/`
- Scripts live in `.claude/skills/<name>/scripts/`
- Brand assets for PPTX live in `.claude/skills/pptx-generator/brands/<brand-name>/`
