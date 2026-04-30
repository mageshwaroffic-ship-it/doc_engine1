# LinkedIn Lead Generation - Usage Examples

## Quick Start

### 1. Single Post Analysis

**User prompt:**
```
/linkedin-lead-generation

Post:
"We're manually processing 200 leads daily. This is consuming 80% of our team's time. 
Anyone know how to automate this? Need something quick, budget approved."

Author: Sarah Chen, Sales Director at TechCorp
```

**Agent output (JSON):**
```json
{
  "author": "Sarah Chen",
  "post": "We're manually processing 200 leads daily...",
  "intent": "HIGH",
  "confidence": "95%",
  "problem": "Manual lead processing consuming 80% of team's time",
  "urgency": "High",
  "keywords": ["manually", "consuming", "automate", "budget approved"],
  "lead_score": 9,
  "suggested_service": "Lead Processing Automation / Workflow Automation",
  "reply": "Hi Sarah, saw your post about manual lead processing. We help teams automate exactly this—many clients see 80%+ time savings. Would love to discuss if helpful 👍"
}
```

---

### 2. Bulk Processing with CSV

**Input CSV (posts.csv):**
```csv
author,post,url,date
Sarah Chen,We're manually processing 200 leads...,linkedin.com/feed/...,2024-04-20
Mike Johnson,Our CRM data is a mess...,linkedin.com/feed/...,2024-04-19
Lisa Wang,Looking for a developer to build our platform,linkedin.com/feed/...,2024-04-18
```

**Run the analyzer:**
```bash
python scripts/lead_analyzer.py \
  --input posts.csv \
  --output leads.xlsx \
  --min-score 6
```

**Output: leads.xlsx**
| author | post | intent | problem | urgency | lead_score | suggested_service | reply |
|--------|------|--------|---------|---------|------------|-------------------|-------|
| Sarah Chen | We're manually processing... | HIGH | Manual lead processing | High | 9 | Lead Automation | Hi Sarah, saw your post... |
| Mike Johnson | Our CRM data is a mess... | MEDIUM | Data inconsistency | Medium | 7 | CRM Cleanup/Automation | Great question, we specialize... |
| Lisa Wang | Looking for a developer... | HIGH | Need platform development | High | 10 | Software Development | Perfect timing! We build... |

---

### 3. Filter Only HIGH Intent Leads

```bash
python scripts/lead_analyzer.py \
  --input posts.csv \
  --output high_priority_leads.xlsx \
  --filter HIGH \
  --min-score 8
```

**Results:** Only posts with HIGH intent + score ≥ 8

---

## Real-World Examples

### Example 1: Manufacturing Company (MEDIUM Intent)

**Raw post:**
```
"We're still using spreadsheets for inventory management. Our supply chain team 
spends hours every day on data entry. It's error-prone and slow. Anyone else dealing 
with this? What's your solution?"
```

**Analysis:**
- Intent: **MEDIUM** (problem stated, no direct ask)
- Pain words: "hours", "data entry", "error-prone", "slow" = +4 points
- Urgency: **Medium** (not explicit)
- Lead score: 1 (MEDIUM) + 4 (pain) + 2 (relevance) = **7/10**
- Service: **Process Automation / ERP Integration**
- Reply: "Totally understand the pain. Spreadsheet-based workflows are a bottleneck for many teams. We automate this type of process with 90%+ accuracy. Happy to explore if interested 👍"

---

### Example 2: E-Commerce Director (HIGH Intent)

**Raw post:**
```
"URGENT: Looking for automation engineer to set up Zapier workflows. 
We're getting 500+ orders daily and our fulfillment process is manual. 
Budget allocated. Need someone ASAP. Any recommendations?"
```

**Analysis:**
- Intent: **HIGH** (explicit ask + multiple signals)
- Keywords: "Looking for", "ASAP", "Budget allocated", "urgent"
- Pain words: "manual", "500+ orders" = +2 points
- Buyer signals: "Budget allocated", "ASAP" = +4 points
- Lead score: 3 (HIGH) + 2 (pain) + 4 (buyer) + 2 (relevance) = **10/10** ⭐
- Service: **Workflow Automation / Order Processing**
- Reply: "Hi, perfect timing! We specialize in order fulfillment automation. Many e-commerce teams save 60+ hours/week with automated workflows. Let's chat about your process 👍"

---

### Example 3: Motivational Post (LOW Intent - SKIP)

**Raw post:**
```
"Excited to announce we just implemented HubSpot and it's transformed our sales process! 
So proud of my team for making this happen. #SalesAutomation #HubSpot"
```

**Analysis:**
- Intent: **LOW** (celebration, not a problem/ask)
- Reason: Already solved their problem
- Lead score: **0** (skip)
- Action: Ignore for lead gen, could add to nurture list later

---

### Example 4: Indirect Need (MEDIUM Intent)

**Raw post:**
```
"How does your company handle customer onboarding at scale? We're struggling 
to manage the process smoothly as we grow. Would love to hear what you've built."
```

**Analysis:**
- Intent: **MEDIUM** (problem implicit, seeking advice)
- Problem: Managing customer onboarding at scale
- Pain words: "struggling" = +1 point
- Buyer context: Growing company = +1 point
- Lead score: 1 (MEDIUM) + 1 (pain) + 1 (scale) + 2 (relevance) = **5/10**
- Service: **Customer Onboarding Automation**
- Reply: "Great question. We help SaaS companies automate their onboarding workflows—saves weeks of manual setup per quarter. Happy to share a framework if helpful 💡"

---

## Scoring Breakdown Examples

### High Score Example (9/10)
```
Post: "We need automation for our 300+ email follow-ups daily. Manual process.
This is critical for Q2. Have budget. Looking for someone to implement."

Scoring:
✓ Intent = HIGH                          +3
✓ Pain words: "automation", "manual"     +2
✓ Buyer words: "budget", "looking for"  +4
✓ Business relevance (email workflow)    +2
✓ Urgency: "Q2", "critical"             +1
─────────────────────────────────────────
  TOTAL: 12 → Capped at 10 = 9-10/10
```

### Medium Score Example (6/10)
```
Post: "Is anyone using automation tools for data entry? 
Our team does this manually and it takes forever."

Scoring:
✓ Intent = MEDIUM                        +1
✓ Pain words: "manually", "takes forever" +2
✓ Buyer signals: none                    +0
✓ Business relevance                     +2
✓ Urgency: none explicit                 +0
─────────────────────────────────────────
  TOTAL: 5 → 6/10 (rounded up due to intent clarity)
```

### Low Score Example (3/10)
```
Post: "Follow me for daily automation tips!"

Scoring:
✓ Intent = LOW (spam keyword)            +0
✓ Pain words: none                       +0
✓ Buyer signals: none                    +0
✓ Spam flag: "follow me"                 → SKIP
─────────────────────────────────────────
  TOTAL: 0 → DO NOT INCLUDE
```

---

## Integration with Your CRM

### Salesforce Import
1. Export from Excel
2. Use Salesforce Data Import Wizard
3. Map columns:
   - `author` → Lead Name
   - `problem` → Description
   - `lead_score` → Custom Score field
   - `suggested_service` → Product Interest
   - `reply` → Notes

### HubSpot Import
1. Export as CSV
2. Go to Contacts → Import
3. Map fields (auto-detects "name", adds others manually)
4. Use `lead_score` for Lead Scoring in workflows

### Google Sheets (Manual CRM)
1. Import Excel to Google Sheets
2. Create filters by `intent` and `lead_score`
3. Add columns: `contacted`, `response`, `outcome`
4. Track outreach effectiveness

---

## Tips & Tricks

### 🔥 Hot Leads (Best for Outreach)
- Filter: `intent = HIGH` AND `lead_score >= 8`
- Send personalized messages within 2 hours of post
- Mention specific problem from their post

### 🌡️ Warm Leads (Nurture)
- Filter: `intent = MEDIUM` AND `lead_score >= 6`
- Send helpful content (blog post, case study)
- Build relationship over 1-2 weeks before pitch

### 🔄 Bulk Processing Tips
```bash
# Process and filter at once
python lead_analyzer.py \
  --input raw_posts.csv \
  --output hot_leads.xlsx \
  --filter HIGH \
  --min-score 8

# Lower threshold for volume
python lead_analyzer.py \
  --input raw_posts.csv \
  --output all_qualified_leads.xlsx \
  --min-score 5
```

### 📊 Weekly Workflow
1. Monday: Export LinkedIn posts from search
2. Tuesday: Run analyzer
3. Wednesday: Review HIGH/MEDIUM leads
4. Thursday: Customize and send replies
5. Friday: Track responses + update CRM

---

## CSV Format Guide

**Required columns (minimum):**
```
author,post
```

**Recommended columns (for best results):**
```
author,post,url,date,title,company,industry
```

**Example full CSV:**
```csv
author,post,url,date,title,company,industry
Sarah Chen,We're processing 200 leads daily...,linkedin.com/feed/1234,2024-04-20,Sales Director,TechCorp,SaaS
Mike Johnson,Our CRM data is a mess...,linkedin.com/feed/5678,2024-04-19,VP Operations,ManufactureCo,Manufacturing
```

---

## Troubleshooting

**Q: No leads found after processing?**  
A: Lower `--min-score` (try `--min-score 3`) or check CSV format

**Q: Excel file has no formatting?**  
A: Install openpyxl: `pip install openpyxl`

**Q: How do I adjust scoring?**  
A: Edit `PAIN_WORDS`, `BUYER_WORDS` in `lead_analyzer.py` line 15

**Q: Can I add custom keywords?**  
A: Yes! Add to the sets at top of `lead_analyzer.py`
