---
name: pptx-generator
description: Generates branded PPTX presentations and LinkedIn carousels using python-pptx with 16+ layout templates.
---

# PPTX Slide Generator

Use this skill for creating presentations, slide decks, or LinkedIn carousels.

## Trigger phrases
- "create presentation", "make slides", "generate deck", "LinkedIn carousel", "slide deck"

## Prerequisites

1. A brand must exist at `.claude/skills/pptx-generator/brands/*/brand.json`
   - If none exists, run the `brand-voice-generator` skill first
2. `pip install python-pptx`

## Three Operating Modes

| Mode | Format | Output |
|------|--------|--------|
| Presentation slides | 16:9 (10"×5.625") | .pptx file |
| LinkedIn carousel | 1:1 square | .pdf file |
| Manage cookbook layouts | Any | New/updated .py layout files |

## Critical Requirements

### 1. Brand Discovery First
Before generating anything, check `.claude/skills/pptx-generator/brands/*/brand.json`.
Load brand colors, fonts, and assets. Never hardcode colors.

### 2. Read Layout Frontmatters
Before selecting layouts, read the first 40 lines of every `.py` file in `cookbook/` to understand each layout's `best_for`, `avoid_when`, and limits.

### 3. Variety Enforcement
- Content-only slides must be <25% of total
- No more than 2-3 consecutive slides with same layout
- Visual layouts (cards, stats, columns, hero) must be 50%+ of slides

### 4. Batch Generation (max 5 slides)
Never generate more than 5 slides at once. After each batch:
- Check for duplicate titles
- Verify spacing and colors
- Confirm background is explicitly set (see bug fix below)

### 5. Background Bug Fix (Critical)
Every slide MUST set background explicitly:
```python
slide.background.fill.solid()
slide.background.fill.fore_color.rgb = RGBColor(r, g, b)
```
Without this, slides default to white, making content unreadable on dark brands.

### 6. Slide Planning (always required)
Before writing code, create a plan table:

| # | Layout | Title | Key Content | Notes |
|---|--------|-------|-------------|-------|
| 1 | hero | ... | ... | ... |

Verify: no duplicate titles, logical flow, correct layouts for content type.

## Text Rules

- No trailing periods on titles, bullets, labels (unless full sentence)
- No ellipsis in headlines
- Stats/numbers: clean format, no trailing punctuation
- CTAs: no trailing punctuation

## Output

Use settings from `config.json` for:
- Output directory
- File naming convention (`{brand}-{date}-{title}`)
- Batch size

After all batches: combine into single final file, delete part files.

## Layout Decision Tree

For each content block, ask:
1. Is this a key stat or number? → Use stats layout
2. Is this a comparison or list of 3-4 items? → Use cards layout
3. Is this two distinct concepts? → Use two-column layout
4. Is this a hero moment / section opener? → Use hero layout
5. Is it pure text with no visual opportunity? → Use content layout (last resort, max 25%)

## File Locations

All skill resources are in `.claude/skills/pptx-generator/`.
- `brands/<brand>/brand.json` — colors, fonts, assets
- `brands/<brand>/config.json` — output settings
- `cookbook/*.py` — layout templates
