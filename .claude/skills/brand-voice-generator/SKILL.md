---
name: brand-voice-generator
description: Generates brand.json, config.json, brand-system.md, and tone-of-voice.md for consistent visual and tonal identity across skills.
---

# Brand & Voice Generator

Use this skill when the user wants to set up a brand identity, configure visual design, or prepare for using the pptx-generator skill.

## Trigger phrases
- "create brand", "brand setup", "set up brand", "brand identity", "brand configuration"

## Output Files

All four files are generated into `.claude/skills/pptx-generator/brands/<brand-name>/`:

| File | Contents |
|------|---------|
| `brand.json` | Colors, fonts, asset paths |
| `config.json` | Output directory, naming conventions, batch settings |
| `brand-system.md` | Design philosophy, visual language, component guidelines |
| `tone-of-voice.md` | Writing personality, style rules, word choices |

## Discovery Process (8 steps)

Walk the user through these steps in order. Use quick mode (sensible defaults) if they say they're in a hurry.

### Step 1 — Brand Basics
- Brand name, one-sentence description, primary use case (internal docs, client decks, social content)

### Step 2 — Color Palette (10 colors)
Define colors for: background-primary, background-secondary, text-primary, text-secondary, accent-primary, accent-secondary, surface, border, success, error.

**Dark theme defaults:** Dark backgrounds (#0D0D0D, #1A1A1A), light text (#F5F5F5, #A0A0A0)  
**Light theme defaults:** White/light backgrounds, dark text, colorful accents

### Step 3 — Typography (3 typefaces)
- Heading font, body font, code/monospace font
- Default if unsure: Inter (heading + body), JetBrains Mono (code)

### Step 4 — Assets
- Logo path(s), icon library, illustration style
- Store in `brands/<brand-name>/assets/`

### Step 5 — Voice Personality
Ask: "If your brand were a person at a dinner party, how would they speak?"
Capture: formal/casual, technical/accessible, serious/playful, brief/detailed

### Step 6 — Design Principles
- 3-5 core principles (e.g., "clarity over decoration", "data-forward")
- Signature visual elements (geometric shapes, gradients, photography style)

### Step 7 — Generate Files
Create all four files with the collected information.

### Step 8 — Verify
Confirm files exist at `.claude/skills/pptx-generator/brands/<brand-name>/` and test with the pptx-generator skill.

## brand.json Schema

```json
{
  "name": "<brand-name>",
  "colors": {
    "background": {"primary": "#hex", "secondary": "#hex"},
    "text": {"primary": "#hex", "secondary": "#hex"},
    "accent": {"primary": "#hex", "secondary": "#hex"},
    "surface": "#hex",
    "border": "#hex",
    "success": "#hex",
    "error": "#hex"
  },
  "fonts": {
    "heading": {"family": "Inter", "weight": 700},
    "body": {"family": "Inter", "weight": 400},
    "code": {"family": "JetBrains Mono", "weight": 400}
  },
  "assets": {
    "logo": "assets/logo.png",
    "icon": "assets/icon.png"
  }
}
```

## config.json Schema

```json
{
  "output": {
    "directory": "output/",
    "naming": "{brand}-{date}-{title}",
    "batch_size": 5
  },
  "slides": {
    "width": 10,
    "height": 5.625,
    "dpi": 150
  }
}
```

## Updating Existing Brands

If a brand already exists, load the existing files first and only update the sections the user wants to change. Preserve everything else.
