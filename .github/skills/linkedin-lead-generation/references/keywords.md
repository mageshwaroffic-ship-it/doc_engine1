# LinkedIn Lead Generation Keywords

## 1. Search Keywords (Finding Opportunities)

Posts containing these keywords often indicate business needs. Use these to filter LinkedIn feeds or search.

### Developer/Freelance Keywords
- looking for developer
- need website developer
- freelance developer required
- need developer ASAP
- hiring developer
- looking for CTO
- tech team needed
- development help

### Automation Keywords
- looking for automation
- need automation help
- automate workflow
- business process automation
- workflow automation
- automation engineer
- automate my process
- manual work automation

### AI/ChatBot Keywords
- AI automation help
- chatbot for business
- AI workflow
- automation with AI
- intelligent automation
- need AI solution
- machine learning project

### Integration Keywords
- Zapier automation help
- Make.com automation
- integration needed
- API integration
- workflow integration
- tool integration

### CRM Keywords
- CRM automation setup
- CRM implementation
- sales automation system
- lead management system
- customer database
- CRM customization
- pipeline automation

### Lead Gen Keywords
- lead generation automation
- lead scraping
- lead management
- prospect automation
- outreach automation
- follow-up automation

### General Service Keywords
- need tech team
- hiring automation engineer
- looking for consultant
- tech solution needed
- software solution
- business software
- scaling team

---

## 2. Pain & Urgency Keywords (Scoring Multipliers)

When these keywords appear in a post, they indicate pain points. Use to boost lead scores.

### Pain Words (Slow/Inefficient) — +1pt each
- slow
- manual
- time consuming
- time-consuming
- tedious
- repetitive
- inefficient
- error prone
- error-prone
- wasting time
- draining resources
- bottleneck
- struggling
- difficult
- challenging
- overwhelmed
- drowning in
- stuck with
- losing time on

### Process Pain Words — +1pt each
- manual data entry
- copy/paste
- spreadsheet heavy
- excel hell
- duplicate data
- data inconsistency
- broken workflow
- gaps in process
- missing automation
- legacy system
- outdated
- unreliable

### Financial Pain Words — +2pts (higher intent)
- costing us
- wasting money
- ROI
- budget
- investment
- expensive
- saving money
- reducing costs
- financial impact
- revenue impact

---

## 3. Buyer Signal Keywords (High Intent) — +2pts each

These keywords indicate the person is actively looking to buy/hire or is decision-maker:

### Explicit Hire/Buy
- looking for
- need
- seeking
- in market for
- searching for
- hunting for
- require
- must have
- urgent need

### Timeline/Urgency
- ASAP
- immediately
- urgent
- this week
- this month
- this quarter
- deadline
- by end of month
- before Q3
- timeline
- soon

### Budget/Investment
- budget approved
- allocated budget
- have budget
- funded
- investment ready
- approved spend
- ready to invest
- willing to pay

### Decision Authority
- I own
- I'm responsible for
- I manage
- I lead
- my team
- we need
- we're looking
- we're hiring
- our company

### Scale/Size
- enterprise
- large team
- scaling
- rapid growth
- growing
- expanding
- multi-team
- nationwide
- international

---

## 4. Industry/Vertical Keywords

Identify if the poster is in your target industry:

### Software/Tech
- software
- development
- engineering
- tech team
- coding
- programming
- developer
- platform
- SaaS
- application

### E-Commerce
- e-commerce
- online store
- Shopify
- marketplace
- inventory
- orders
- shipping
- fulfillment

### Sales/Marketing
- sales
- marketing
- leads
- prospect
- pipeline
- CRM
- outreach
- campaigns
- cold outreach
- B2B

### Operations/Finance
- finance
- accounting
- operations
- supply chain
- procurement
- HR
- payroll
- reporting

### Real Estate
- real estate
- property
- agent
- listing
- leasing
- broker

### Healthcare/Medical
- healthcare
- medical
- clinic
- patient
- hospital
- healthcare provider

---

## 5. Negative/Spam Keywords (Reduce Score)

Skip or reduce score if post contains these:

### Spam Indicators — Mark as LOW (ignore)
- follow me for tips
- link in bio
- check my profile
- DM for details
- generic motivational
- just sharing knowledge
- learning journey
- proud to announce (without context)
- celebrating milestone (no business value)
- industry joke
- meme
- repost
- congratulations (no business tie-in)
- thanks for the opportunity

### Out of Scope
- looking for job (not hiring)
- I'm available (freelancer pitching, not buying)
- hire me
- open to opportunities
- freelancer for hire

---

## 6. How to Use These Keywords

### Scoring Example

**Post:** "We're manually processing 200 leads daily. This is killing our productivity. Needs to change ASAP."

**Analysis:**
- Base intent: HIGH (explicit pain) = +3
- Pain keywords: "manually" (+1), "killing" (+1), "productivity" (+1) = +3
- Urgency keywords: "ASAP" (+2) = +2
- **Total: 3 + 3 + 2 = 8/10** ✅ HIGH priority lead

---

### Implementation in Code

```python
PAIN_WORDS = [
    "slow", "manual", "time consuming", "tedious", "repetitive",
    "inefficient", "error prone", "wasting time", "struggling"
]

BUYER_WORDS = [
    "looking for", "need", "ASAP", "urgent", "budget", "approved",
    "seeking", "hiring", "investment", "owned by"
]

SPAM_WORDS = [
    "follow me", "link in bio", "check my profile", "meme", "joke"
]

def score_post(post_text):
    score = 0
    
    # Pain words = +1 each
    for word in PAIN_WORDS:
        if word.lower() in post_text.lower():
            score += 1
    
    # Buyer words = +2 each
    for word in BUYER_WORDS:
        if word.lower() in post_text.lower():
            score += 2
    
    # Spam filter
    for word in SPAM_WORDS:
        if word.lower() in post_text.lower():
            return 0  # Spam, ignore
    
    return min(score, 10)  # Cap at 10
```

---

## 7. Seasonal/Trending Keywords

Add these for timely outreach:

### Quarter-End Keywords
- Q1/Q2/Q3/Q4 goals
- budget planning
- fiscal planning
- new year planning
- half-year review

### Industry Events
- conference
- summit
- expo
- workshop
- training
- certification

### Holiday/Seasonal
- New Year
- tax season
- holiday prep
- back to school
- budget refresh

---

## Notes

- Keywords are **case-insensitive** (search for "ASAP", "asap", "Asap")
- **Combine keyword groups**: A post with pain + buyer + industry words = higher score
- **Context matters**: "slow" in "slow down and breathe" ≠ process pain
- Update these lists quarterly based on your sales data and outreach results
