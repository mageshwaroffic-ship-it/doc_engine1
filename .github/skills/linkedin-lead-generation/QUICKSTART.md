# LinkedIn Lead Generation - Quick Start Guide

Get your first leads qualified in 5 minutes!

## Option A: Single Post Analysis (Fastest)

### 1. Copy a LinkedIn Post

Find any LinkedIn post about business problems (automation, development, CRM, etc.)

Example:
```
"We're manually processing 200 leads daily. This is killing productivity. 
Need to automate. Budget approved. ASAP."
```

### 2. Invoke the Skill

In VS Code Chat, type:
```
/linkedin-lead-generation

Post: [paste the LinkedIn post here]
Author: [name if visible]
```

### 3. Get Your Lead

Agent returns JSON with:
- ✅ Intent: HIGH / MEDIUM / LOW
- ✅ Lead Score: 1-10
- ✅ Problem extracted
- ✅ Personalized reply ready to send

**Time:** 30 seconds

---

## Option B: Bulk Process CSV (Most Powerful)

### 1. Install Dependencies

```bash
# One time only
pip install -r requirements.txt
```

### 2. Prepare CSV File

Create `posts.csv` with columns:
```
author,post,url,date
Sarah Chen,We're processing 200 leads manually...,https://linkedin.com/feed/...,2024-04-20
Mike Johnson,Our CRM is a mess...,https://linkedin.com/feed/...,2024-04-19
```

Or use the sample file included:
```bash
cp sample_posts.csv my_posts.csv
```

### 3. Run Analyzer

```bash
python scripts/lead_analyzer.py \
  --input my_posts.csv \
  --output leads.xlsx
```

### 4. Open Excel File

`leads.xlsx` has:
- ✅ All posts analyzed
- ✅ Color-coded by score
- ✅ Intent classification
- ✅ Extracted problems
- ✅ Ready-to-send replies

**Time:** 2 minutes

---

## Option C: Test with Sample Data (Recommended First Step)

### 1. Run with Sample Posts

```bash
# Already included in this folder
python scripts/lead_analyzer.py \
  --input sample_posts.csv \
  --output sample_results.xlsx
```

### 2. View Results

Opens `sample_results.xlsx` with 10 real example posts analyzed.

### 3. See What Works

Check which posts scored HIGH (8-10) vs MEDIUM (6-7) vs LOW (<5).

**Time:** 1 minute

---

## Quick Commands Reference

```bash
# Basic (all posts)
python lead_analyzer.py --input posts.csv --output leads.xlsx

# High priority only (score 8+)
python lead_analyzer.py --input posts.csv --output hot.xlsx --min-score 8

# Only HIGH intent posts
python lead_analyzer.py --input posts.csv --output high_intent.xlsx --filter HIGH

# Combine filters
python lead_analyzer.py \
  --input posts.csv \
  --output best_leads.xlsx \
  --filter HIGH \
  --min-score 8

# Help/options
python lead_analyzer.py --help
```

---

## 🎯 Next Steps

After you have leads in Excel:

1. **Filter**: Sort by `lead_score` (highest first)
2. **Review**: Check HIGH intent + score 8+ leads
3. **Copy**: Use the `reply` column text
4. **Send**: Paste into LinkedIn messages
5. **Track**: Add a `replied` column to track outreach

---

## 📊 CSV Format

**Minimum (required):**
```csv
author,post
```

**Recommended (for best results):**
```csv
author,post,url,date
```

**Full format (optional):**
```csv
author,post,url,date,title,company,industry
```

### Example Rows:
```csv
Sarah Chen,We're processing 200 leads daily manually...,https://linkedin.com/feed/1234,2024-04-20
Mike Johnson,Our CRM data has duplicates everywhere,https://linkedin.com/feed/5678,2024-04-19
Lisa Wang,Looking for a developer to build our website,https://linkedin.com/feed/9012,2024-04-19
```

---

## 🎓 Understanding Your Results

### Columns in Excel Output:

| Column | Meaning |
|--------|---------|
| `author` | Who wrote the post |
| `post` | First 200 characters of post (sample) |
| `intent` | HIGH / MEDIUM / LOW classification |
| `problem` | What problem they mentioned |
| `urgency` | High / Medium / Low |
| `keywords` | Top pain/buyer keywords matched |
| `lead_score` | 1-10 (8+='hot', 6-7='warm', <5='skip') |
| `suggested_service` | What you can offer them |
| `reply` | Copy+paste ready message |
| `confidence` | How sure we are (70-99%) |

### Score Meaning:

- **8-10 🔥**: HOT LEAD → Message immediately
- **6-7 🔄**: WARM LEAD → Send helpful content first
- **5-6 📌**: QUALIFIED → Add to nurture sequence
- **<5 ❌**: SKIP → Low fit or no real need

---

## ⚡ Pro Tips

### Get More Posts
- Search LinkedIn: "manual" + "struggling" + "automation"
- Use LinkedIn Sales Navigator for targeted searches
- Export all results to CSV

### Better Results
- Include author title/company if visible
- Include exact quote if multiple problems mentioned
- Use posts from last 7 days (fresher = more responsive)

### Maximize Conversions
1. Personalize reply: Replace generic text with specific problem quote
2. Send within 2 hours of post (higher engagement)
3. Track responses: Update `replied` and `result` columns
4. Improve over time: Adjust keywords/weights based on response rates

### Batch Processing
```bash
# Process multiple files
for file in posts_*.csv; do
  output="${file%.csv}_results.xlsx"
  python lead_analyzer.py --input "$file" --output "$output"
done
```

---

## 🐛 Troubleshooting

**"No module named pandas"**
```bash
pip install pandas openpyxl
```

**"No leads found"**
- Lower `--min-score` (try 3 or 4)
- Check CSV columns: must have `author` and `post`
- Make sure posts are > 10 characters

**"Excel file looks plain (no formatting)"**
```bash
pip install openpyxl --upgrade
```

**"Posts being skipped"**
- Some LOW intent posts are auto-skipped (memes, celebrations, spam)
- Try with `--min-score 0` to include everything
- Check Classification rules in [classification.md](references/classification.md)

---

## 📚 Learn More

- **Full workflow**: [SKILL.md](SKILL.md)
- **Real examples**: [examples.md](references/examples.md)
- **Intent rules**: [classification.md](references/classification.md)
- **Keywords**: [keywords.md](references/keywords.md)
- **Prompts**: [prompts.md](references/prompts.md)

---

## ✅ Checklist: Your First Lead Gen Campaign

- [ ] Read this QUICKSTART (2 min)
- [ ] Install dependencies: `pip install -r requirements.txt` (1 min)
- [ ] Test with sample: `python lead_analyzer.py --input sample_posts.csv --output test.xlsx` (1 min)
- [ ] Export real LinkedIn posts to CSV (10 min)
- [ ] Process your posts: `python lead_analyzer.py --input my_posts.csv --output my_leads.xlsx` (1 min)
- [ ] Open Excel, sort by score (1 min)
- [ ] Message top 5 HIGH intent leads (15 min)
- [ ] Track responses (ongoing)

**Total time to first leads: ~30 minutes**

---

## 🚀 You're Ready!

Start with the sample file, see how it works, then process your first real LinkedIn posts.

**Next step:** Run this command right now:
```bash
python scripts/lead_analyzer.py --input sample_posts.csv --output sample_results.xlsx
```

Then open `sample_results.xlsx` and see what HIGH, MEDIUM, LOW intent looks like!

---

**Questions?** Check [README.md](README.md) for full documentation.
