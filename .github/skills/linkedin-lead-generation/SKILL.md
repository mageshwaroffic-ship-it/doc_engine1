---
name: linkedin-lead-generation
description: 'Extract high-quality B2B leads from LinkedIn posts. Use when identifying prospects for software development, automation, CRM, or AI services. Classifies intent, extracts problems, scores leads (1-10), and generates personalized replies.'
argument-hint: '[paste LinkedIn post] or [provide CSV of posts]'
user-invocable: true
---

# LinkedIn Lead Generation Agent

## Overview

A specialized AI agent that analyzes LinkedIn posts to identify high-quality B2B leads for software development, website development, AI automation, workflow automation, and CRM services. Classifies intent, extracts business problems, scores lead quality, and generates personalized outreach replies.

## When to Use

- Analyzing individual LinkedIn posts for lead potential
- Bulk processing LinkedIn feeds or post exports
- Identifying sales opportunities in industry discussions
- Qualifying prospects before outreach
- Generating personalized connection messages
- Building lead scoring databases (CSV/Excel exports)

## The Process

### 1. Intent Classification

Analyze each LinkedIn post and classify:

**HIGH INTENT** → Direct explicit request for help
- "Looking for a developer..."
- "Need automation help for..."
- "Hiring automation engineer"
- "Looking for CRM solution"

**MEDIUM INTENT** → Indirect problem mention, implied need
- "Manual process taking too long"
- "Our workflow is inefficient"
- "Struggling with manual data entry"
- "Want to reduce repetitive tasks"

**LOW INTENT** → Skip (general discussion, memes, content)
- "Just shared a learning post"
- "Here's a funny industry meme"
- "Celebrating a personal milestone"

See [Classification Criteria](./references/classification.md) for detailed rules.

### 2. Problem & Pain Extraction

Extract from the post:
- **Author Name**: Commenter or post author
- **Problem Statement**: What specific issue are they facing?
- **Urgency Level**: High / Medium / Low (based on keywords)
- **Keywords**: Relevant service/pain keywords
- **Suggested Service**: What your company can offer

Use the [Pain & Buyer Keywords](./references/keywords.md) reference list to identify intent signals.

### 3. Lead Scoring (1-10)

Score based on:
- **Intent clarity**: HIGH=+3pts, MEDIUM=+1pt
- **Pain keyword match**: +1pt per pain word (max +5)
- **Buyer signal match**: +2pts per buyer word
- **Business relevance**: Alignment with your services (+0-2pts)
- **Timeline urgency**: Explicit deadline/budget mention (+1pt)

**Example**:
- HIGH intent (3) + 3 pain words (3) + 2 buyer words (2) = 8/10

### 4. Auto-Reply Generation

Create a short, personalized 3–4 line response that:
- Shows genuine understanding of their problem
- Offers value without being salesy
- Invites conversation subtly
- Friendly but professional tone

See [Reply Templates](./references/prompts.md#auto-reply-template) for examples.

### 5. Output Format

All leads extracted to structured JSON, then exportable to **Excel (.xlsx)** for CRM import or team sharing.

## Step-by-Step Workflow

### For Individual Posts

1. **Copy the LinkedIn post text** (or just describe the situation)
2. **Paste into the agent** with `/linkedin-lead-generation`
3. **Agent analyzes** using classification rules
4. **Get structured output** with:
   - Intent classification (HIGH/MEDIUM/LOW)
   - Extracted problem statement
   - Lead score (1–10)
   - Suggested personalized reply
5. **Use the reply** to connect or message the prospect

### For Bulk Processing

1. **Export LinkedIn posts** to CSV with columns:
   - `author_name`, `post_content`, `post_url`, `date`
2. **Run the [lead analyzer script](./scripts/lead_analyzer.py)**:
   ```bash
   python lead_analyzer.py --input posts.csv --output leads.xlsx
   ```
3. **Excel file generated** with all leads scored and classified
4. **Filter by score** (8+) or intent (HIGH only) for outreach campaigns

## Search Keywords

The agent scans posts containing these keywords to find opportunities:

[See Keywords Reference](./references/keywords.md) for complete lists including:
- Developer/freelance keywords
- Automation keywords  
- CRM/sales keywords
- Process improvement keywords

## Output Fields

```json
{
  "author": "John Smith",
  "post": "We're manually processing 500 leads daily. This is taking too long.",
  "intent": "HIGH",
  "problem": "Manual lead processing is time-consuming and error-prone",
  "urgency": "High",
  "keywords": ["manual", "time consuming", "process"],
  "pain_score": 8,
  "lead_score": 9,
  "suggested_service": "Lead processing automation / Workflow automation",
  "reply": "Hi John, saw your post about manual lead processing. We help automate such workflows and cut processing time by 80%. Would love to discuss if you're open to it 👍"
}
```

## Files & Scripts

- [Prompts Reference](./references/prompts.md) — Full classifier, filter, and reply prompts
- [Keywords Reference](./references/keywords.md) — Pain words, buyer signals, service keywords
- [Lead Analyzer Script](./scripts/lead_analyzer.py) — Bulk process CSV → Excel
- [Classification Criteria](./references/classification.md) — Detailed intent rules

## Tips for Best Results

✅ **DO:**
- Include author context (title/industry if visible)
- Capture the exact problem quoted from the post
- Be specific about urgency signals (dates, budgets mentioned)
- Review HIGH/MEDIUM leads before outreach

❌ **DON'T:**
- Process low-quality/spam posts
- Over-score posts without clear pain signals
- Send generic replies (personalization matters!)
- Ignore industries outside your service offering

## Common Questions

**Q: Can I adjust the lead scoring formula?**  
A: Yes! Edit the scoring weights in [lead_analyzer.py](./scripts/lead_analyzer.py) starting at line 25.

**Q: What if a post mentions multiple problems?**  
A: Extract the primary problem (what would you solve first?) and note secondary issues in the reply.

**Q: How often should I process LinkedIn?**  
A: Weekly or daily depending on volume. The script handles both individual and bulk workflows.
