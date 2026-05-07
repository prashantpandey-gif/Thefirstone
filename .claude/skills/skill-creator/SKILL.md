---
name: skill-creator
description: Guides creation of new modular Claude Code skills with progressive disclosure and minimal token footprint.
---

# Skill Creator

Use this skill when the user wants to build a new custom skill to extend Claude's capabilities.

## Trigger phrases
- "create skill", "new skill", "build skill", "add skill", "make skill"

## Core Design Philosophy

> "The context window is a public good."

Skills must be lean. Every paragraph you write costs tokens in every future session. Question each inclusion: does Claude need this, or does it already know it?

**Default assumption: Claude is already very smart.** Only include context Claude lacks.

## Skill Structure

```
.claude/skills/<skill-name>/
├── SKILL.md          ← Required. The skill itself.
├── references/       ← Optional. Docs loaded only when needed.
├── scripts/          ← Optional. Executable code.
└── assets/           ← Optional. Templates/boilerplate (not auto-loaded).
```

## SKILL.md Format

```markdown
---
name: <skill-name>
description: <one sentence — used for skill discovery, ~20 words max>
---

# Skill Title

Brief intro: what this skill does and when to use it.

## Trigger phrases
- [keyword], [phrase], [condition]

## [Core instructions...]
```

## Progressive Disclosure (3 tiers)

| Tier | Content | Size | When loaded |
|------|---------|------|-------------|
| Metadata | Frontmatter name + description | ~20 words | Always (CLAUDE.md index) |
| SKILL.md body | Full instructions | <5k words | When skill is triggered |
| References | Detailed docs, configs, examples | Any | Only when Claude decides it's needed |

## Creation Workflow

1. **Understand the need** — What task does the user want to automate? What context does Claude currently lack for this task?
2. **Plan contents** — List what to include. Then remove anything Claude already knows.
3. **Write SKILL.md** — Frontmatter, trigger phrases, concise instructions.
4. **Add references** — Only documentation Claude can't infer. Keep filenames descriptive.
5. **Add scripts** — For deterministic, repeatable operations (file generation, API calls).
6. **Test the skill** — Trigger it in a fresh session. Verify it works with minimal context.

## Quality Checklist

- [ ] Frontmatter has `name` and `description`
- [ ] Description is ≤20 words and clearly explains when to use this skill
- [ ] Trigger phrases cover natural ways a user would ask
- [ ] SKILL.md body is <5k words
- [ ] No information Claude already knows from training
- [ ] References folder only exists if there's content Claude can't infer
- [ ] Scripts are self-contained and handle their own errors

## Anti-patterns to Avoid

- Explaining what Claude already knows (Python syntax, git basics, REST APIs)
- Duplicating information across multiple reference files
- Vague trigger phrases ("help", "do something")
- Instructions that don't distinguish from Claude's default behavior
- Reference files that are just copied documentation Claude was trained on
