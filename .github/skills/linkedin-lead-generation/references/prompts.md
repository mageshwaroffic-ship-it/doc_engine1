# LinkedIn Lead Generation Prompts

## 1. Intent Classification Prompt

```
Analyze the following LinkedIn post and classify its intent.

Return:
- Intent: HIGH / MEDIUM / LOW
- Reason for classification (1-2 sentences)
- Does this post indicate a business need? (Yes/No)
- Confidence level (High/Medium/Low)

Rules:
- HIGH → Explicit request for help, services, or hiring
  Examples: "Looking for developer", "Need automation", "Hiring engineer"
  
- MEDIUM → Problem mentioned but no direct ask yet
  Examples: "Process is slow", "Manual work is inefficient", "Struggling with X"
  
- LOW → General content, learning posts, motivation, unrelated hiring
  Examples: "Here's how to learn Python", "Congrats on new role", "Industry meme"

Post:
{{POST_CONTENT}}
```

## 2. Problem & Pain Extraction Prompt

```
Extract structured information from this LinkedIn post indicating a business problem.

Post content:
{{POST_CONTENT}}

Author (if visible):
{{AUTHOR_NAME}}

Return JSON format:
{
  "author": "Name",
  "problem_statement": "What specific problem is mentioned?",
  "pain_keywords": ["keyword1", "keyword2"],
  "urgency_signal": "High/Medium/Low - based on language",
  "timeline": "Explicit timeframe if mentioned (or 'Not specified')",
  "budget_mention": true/false,
  "industry": "Inferred industry if possible",
  "service_category": "Software Dev / Automation / CRM / Website / AI / Other"
}

Focus on:
1. Direct quotes about pain/problems
2. Emotional language ("frustrated", "struggling", "urgent")
3. Scale indicators ("500 leads", "50% time", "daily")
4. Timeline hints ("this quarter", "ASAP", "by end of month")
```

## 3. Lead Scoring Prompt

```
Score this lead on a 1-10 scale based on lead quality and fit.

Post context:
{{POST_CONTENT}}

Problem: {{PROBLEM}}
Intent: {{INTENT}}
Pain keywords found: {{PAIN_KEYWORDS}}

Scoring Criteria:
- Intent Clarity: HIGH=3pts | MEDIUM=1pt | LOW=0pts
- Pain Keyword Match: +1pt each (max 5pts)
- Buyer Signals (budget/timeline/hiring): +2pts each
- Business Relevance to your services: +2pts
- Clarity of ask: +1pt
- Industry fit: +1pt

Return JSON:
{
  "intent_score": 3,
  "pain_score": 4,
  "buyer_score": 2,
  "relevance_score": 2,
  "clarity_score": 1,
  "industry_fit_score": 1,
  "total_lead_score": 13,
  "final_score": 8,
  "breakdown": "HIGH intent (3) + 4 pain words (4) + buyer signals (2) + relevant service (2)"
}
```

## 4. Auto-Reply Generator Prompt

```
Generate a personalized LinkedIn reply to this post.

Guidelines:
- 3–4 lines maximum (short and punchy)
- Friendly and professional tone
- NOT pushy or salesy
- Show genuine understanding of their problem
- Subtle offer to help
- Include a light emoji (👍 or 💡)
- No CTA links (just offer a conversation)

Problem they mentioned: {{PROBLEM}}
Intent level: {{INTENT}}

Example good replies:
❌ Bad: "Hey, we do automation, check out our website!"
✅ Good: "Hi [Name], saw your post about manual lead processing. We help teams like yours automate that workflow—happy to share ideas if helpful 👍"

Now write the reply:
```

## 5. Post Filter/Noise Detection Prompt

```
Analyze this LinkedIn post and filter out noise/spam.

Spam indicators (mark as SKIP if 5+ apply):
- [ ] Looks like a bot post (auto-generated copy)
- [ ] Multiple irrelevant hashtags (20+)
- [ ] Generic motivational fluff with no real problem
- [ ] Recruitment spam (hiring many roles, vague)
- [ ] Link farming (multiple links, no content)
- [ ] Unrelated to tech/business problems
- [ ] Pure job listing (no problem statement)

Signal to INCLUDE:
- [ ] Specific, real problem mentioned
- [ ] Author seems like actual business person
- [ ] Request for help or expertise
- [ ] Problem relates to software/automation/business

Post:
{{POST_CONTENT}}

Decision: INCLUDE / SKIP
Reason: (1 line)
```

## 6. Batch Processing Template Prompt

```
Process this batch of LinkedIn posts.

Return a CSV-like format (can convert to Excel):

author,post_summary,intent,problem,pain_keywords,lead_score,urgency,suggested_service,reply,score_rationale

For each post:
1. Run classification
2. Extract problem
3. Score lead (skip if LOW intent)
4. Generate reply
5. Output one row

Rules:
- Only include HIGH and MEDIUM intent posts
- Minimum lead score: 5 (optional filter)
- Remove duplicates
- Sort by score (highest first)

Posts to process:
{{POSTS_BATCH}}
```

## 7. Refinement: Personalization Prompt

```
Make this reply MORE personalized using the post context.

Current reply:
{{GENERIC_REPLY}}

Post details:
- Author: {{AUTHOR}}
- Company/Role hint: {{CONTEXT}}
- Specific problem: {{PROBLEM}}
- Emotional tone: {{TONE}} (frustrated, curious, urgent)

Rewrite the reply to:
- Reference their specific problem (not generic)
- Match their tone (mirror urgency level)
- Suggest a concrete angle (e.g., "We helped [similar company] reduce manual data entry by 70%")
- Max 3 lines still
- Keep friendly but credible

New reply:
```

## Implementation Notes

### For Agent Invocation

When using these prompts in the agent:

1. **Single Post**: Use prompts 1 → 2 → 3 → 4 in sequence
2. **Classification Only**: Use prompt 1
3. **Bulk Processing**: Use prompt 6 (feeds data to 1-4)
4. **Fine-tune Reply**: Use prompt 7 after 4

### Variable Substitution

Replace `{{VARIABLE}}` with actual post content:
- `{{POST_CONTENT}}` = Full post text
- `{{AUTHOR_NAME}}` = Author name/title
- `{{PROBLEM}}` = Extracted problem statement
- `{{INTENT}}` = Classification result
- `{{PAIN_KEYWORDS}}` = List of matched pain words

### Output Formatting

Always structure output as JSON for downstream processing (CSV → Excel conversion).
