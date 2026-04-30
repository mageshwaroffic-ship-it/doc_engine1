# LinkedIn Lead Classification Criteria

## Intent Classification Rules

### HIGH INTENT (Direct Ask)

**Explicit keywords present:**
- "looking for..." (developer, automation, freelancer, CRM)
- "need..." (help with X, developer for Y, automation of Z)
- "hiring..." (engineer, developer, consultant)
- "seeking..." (anyone who can help with, solution for)
- "we're..." (in market for, looking to, trying to implement)
- "does anyone..." (know how to, have experience with, recommend)
- "any recommendations..." (for X service)
- "struggling with..." + problem statement

**Business context:**
- Author is clearly a decision-maker (CEO, founder, manager, owner)
- Describes a specific business problem needing external help
- Shows budget/timeline awareness (ASAP, this quarter, have budget)
- Multiple solutions/options being considered

**Language signals:**
- Imperative/urgent tone ("must find", "critical need")
- Specific problem stated (not vague)
- Action-oriented ("let me know", "PM me", "DM for details")

**Examples:**
```
"We're looking for a developer to build an e-commerce platform. 
Have budget allocated. Timeline: 3 months. Anyone recommend good agencies?"

"Desperately need someone to automate our lead follow-up process. 
Any automation specialists here? DM me."

"Hiring: Automation engineer for workflow optimization. Serious inquiries only."
```

---

### MEDIUM INTENT (Indirect/Problem Mention)

**Problem statement present, but no direct ask:**
- "we're struggling with..."
- "our process is too slow"
- "manual work is killing productivity"
- "data entry is a bottleneck"
- "need better workflow management"
- "anyone else deal with this?"
- "anyone using X tool? Thoughts?"
- "how do you solve...?"

**Business context:**
- Describes a real pain point
- Implies need for solution but hasn't explicitly asked for help
- May be exploratory (asking for opinions/advice first)
- Shows frustration with current situation

**Language signals:**
- Reflective tone ("anyone else?", "how do you?")
- Problem-focused (describes issue more than solution)
- Audience-seeking ("would love to hear from others")
- Open-ended question format

**Examples:**
```
"Manual lead processing is killing us. We handle ~500 leads daily by hand. 
There has to be a better way. Anyone automated this successfully?"

"Our CRM setup is a mess. Data inconsistencies everywhere. 
Anyone recommend best practices or tools? What worked for your team?"

"We're losing time to repetitive tasks. How do you approach workflow automation in your company?"
```

---

### LOW INTENT (Ignore — No Business Need Signal)

**Content types to SKIP:**

1. **Learning/Educational**
   - "Here's how to learn automation"
   - "5 tips for better workflow"
   - "Python tutorial for beginners"
   - Pure teaching/knowledge share with no business problem

2. **Motivational/Celebration**
   - "Excited to announce I'm starting my new role!"
   - "Congrats to everyone at [company]!"
   - "Today I'm grateful for..."
   - Personal milestones with no business tie-in

3. **Memes/Humor**
   - Industry jokes, funny takes on problems (not serious)
   - Doesn't indicate real need

4. **Generic Spam**
   - "Follow for daily tips!"
   - "Link in bio for free course"
   - "DM for [vague offer]"
   - Recruitment spam (bulk hiring posts)

5. **Already Solved**
   - "We just implemented X solution, very happy!"
   - "Success story: how we automated..."
   - (They solved it already, no buy signal)

6. **Job Postings (unless hiring for external help)**
   - "Hiring 3 developers for our team"
   - Unless they're explicitly asking for agency/contractor help

7. **Unrelated Content**
   - Hobby/personal posts
   - Industry news with no business ask
   - Inspirational quotes

**Examples of LOW INTENT:**
```
"Just closed the best hire of my career! 🎉 #Blessed"

"Here's a meme about how devs feel about Monday mornings lol"

"Top 5 automation tools—check out this thread [link]"

"We successfully implemented HubSpot and saved 20 hours/week. Worth it!"
```

---

## Confidence Scoring

When classifying, indicate your **confidence level**:

### HIGH CONFIDENCE (Very sure)
- ✅ Multiple intent signals present
- ✅ Clear problem statement + explicit ask
- ✅ Author context matches (decision-maker)
- ✅ Service need aligns with offerings

### MEDIUM CONFIDENCE (Fairly sure)
- ⚠️ Problem is clear, but ask is indirect
- ⚠️ Could be exploratory vs. ready to buy
- ⚠️ Author role unclear
- ⚠️ Time to buy unknown

### LOW CONFIDENCE (Uncertain)
- ❌ Could go either way
- ❌ Ambiguous wording
- ❌ Missing context (no author info)
- ❌ Not enough detail to score

**Rule**: If LOW confidence → Mark as MEDIUM intent at best. Only HIGH confidence → HIGH intent.

---

## Decision Tree

```
┌─ Is there an EXPLICIT ASK or HIRING signal?
│  ├─ YES → HIGH INTENT
│  └─ NO → Continue
│
├─ Is there a CLEAR PROBLEM mentioned?
│  ├─ YES → Continue
│  └─ NO → LOW INTENT (skip)
│
├─ Does the problem involve your service area?
│  ├─ YES → Continue
│  └─ NO → LOW INTENT (skip)
│
├─ Is the author likely a decision-maker?
│  ├─ YES → MEDIUM or HIGH (depend on ask clarity)
│  └─ NO → LOW or MEDIUM (harder to close)
│
├─ Is there URGENCY language (ASAP, deadline, urgent)?
│  ├─ YES → MEDIUM intent (prob buy-ready)
│  └─ NO → MEDIUM intent (exploratory)
│
└─ Does post have BUYER SIGNALS (budget, timeline)?
   ├─ YES → HIGH INTENT (or MEDIUM + high score)
   └─ NO → MEDIUM INTENT (or LOW + context dependent)
```

---

## Post-Classification Filtering

After classifying, apply these filters:

### INCLUDE (Process further)
- ✅ Intent = HIGH
- ✅ Intent = MEDIUM + lead score >= 6
- ✅ Confidence = HIGH or MEDIUM
- ✅ Author seems real (not bot/spam)
- ✅ Problem relates to your services

### EXCLUDE (Skip)
- ❌ Intent = LOW
- ❌ Intent = MEDIUM + lead score < 5
- ❌ Looks like spam/bot
- ❌ Completely unrelated industry
- ❌ Already solved/implemented

---

## Common Edge Cases

### Case 1: "Hiring for an agency" 
**Status**: HIGH INTENT  
**Reason**: Hiring external agency means they need services (not just in-house hires)

### Case 2: "We're looking to improve, exploring options"
**Status**: MEDIUM INTENT  
**Reason**: Clear intent, but may not be ready to buy yet

### Case 3: "Frustrated about manual work" (no ask)
**Status**: MEDIUM INTENT  
**Reason**: Problem clear, but indirect ask. Good for nurturing.

### Case 4: "Successfully implemented automation"
**Status**: LOW INTENT  
**Reason**: Already bought/solved. Not a lead unless they're hiring other help.

### Case 5: Question asking for advice ("How do you do X?")
**Status**: MEDIUM INTENT  
**Reason**: Indicates problem awareness. Potential buyer in discovery phase.

### Case 6: Recruiter posting job ("Hiring: Automation engineer")
**Status**: LOW INTENT  
**Reason**: They're looking to hire talent, not buy your services. (Skip unless you're recruiting)

---

## Quality Check

Before marking as HIGH or MEDIUM:
- [ ] Can you quote the problem directly from the post?
- [ ] Is the author someone with buying power (not random employee)?
- [ ] Would YOUR specific service solve this problem?
- [ ] Is the post recent enough to take action on?
- [ ] Does the language suggest they're serious (or just venting)?

If you can't confidently check all boxes → Mark as MEDIUM or skip.
