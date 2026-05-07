---
name: sop-creator
description: Produces scannable, actionable SOPs and runbooks following a universal structure with clear success criteria.
---

# SOP & Runbook Creator

Use this skill when the user asks to create an SOP, runbook, process document, deployment playbook, incident guide, or any technical/operational documentation.

## Trigger phrases
- "create SOP", "write runbook", "document process", "deployment playbook", "incident guide", "how-to guide"

## Core Philosophy

Documentation must be **scannable, actionable, and impossible to misunderstand.**
- Use concrete numbers and names — never "as needed" or "periodically"
- Each step = something to *do*, not something to consider
- Define completion through checklists and testable outcomes

## Universal Template Structure

Every SOP must include these sections in order:

```markdown
# [SOP Title]

**Owner:** [Name/Team]  **Last reviewed:** [Date]  **Version:** [x.x]

## TL;DR
[1-2 sentence summary of what this SOP does and when to use it]

## Definition of Done
- [ ] [Specific, testable outcome 1]
- [ ] [Specific, testable outcome 2]
- [ ] [Specific, testable outcome 3]

## When to Use This
[Exact conditions that trigger this SOP]

## Prerequisites
- [Specific access, tools, or state required]
- [Include exact versions or environment details]

## The Process

### Step 1: [Action verb + object]
[Numbered sub-steps if needed]

Expected output: [What the user should see/get]

### Step 2: ...

## Verify Completion
[How to confirm the SOP worked — commands to run, dashboards to check]

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| [Error message] | [Root cause] | [Exact steps] |

## Questions & Contacts
- [Role]: [Name / Slack / email]
```

## Document Types

**Technical SOPs:**
- Incident runbooks (include severity matrix, escalation path)
- Deployment playbooks (include rollback steps)
- Troubleshooting guides (symptom → cause → fix table)
- Architecture decision records

**Operations SOPs:**
- Process checklists
- Handoff documentation
- Decision trees

**Content SOPs:**
- Production workflows
- Review processes
- Publishing checklists

## Writing Rules

1. "Definition of Done" is the most important section — make it a specific, testable checklist
2. Use numbers: "wait 30 seconds" not "wait a moment"
3. Include exact commands, not descriptions of commands
4. Every troubleshooting row needs an exact fix, not "contact support"
5. No passive voice: "Run the command" not "The command should be run"
