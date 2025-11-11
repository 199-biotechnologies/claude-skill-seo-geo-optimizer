# SEO/GEO Optimizer - Claude Skill

**Version**: 1.0
**Status**: Production Ready
**Last Updated**: November 11, 2025

---

## Overview

A comprehensive Claude skill that analyzes and optimizes content for:

- 🔍 **Traditional SEO** - Meta tags, structured data, technical optimization
- 🤖 **AI Search (GEO/LLMO)** - ChatGPT, Perplexity, Claude, Gemini citation optimization
- 🎤 **Voice Search** - Google Assistant, Siri, Alexa optimization
- 📱 **Social Media Previews** - Open Graph, Twitter Cards, WhatsApp/iMessage

### Key Stats (2025)

- 📈 **527% growth** in AI-referred traffic (Jan-May 2025)
- 🎯 **40.58%** of AI citations from top 10 SERP results
- 🏆 **+33%** citation probability for #1 ranking with optimization
- 🎤 **29 words** average voice search answer length
- 📱 **1200×630px** optimal social preview image size

---

## Quick Start

### Installation

This skill is already installed at:
```
~/.claude/skills/seo-geo-optimizer/
```

### Basic Usage

**Audit an HTML file:**
```bash
claude-code "Audit the SEO of ~/project/pages/about.html"
```

**Optimize for AI search:**
```bash
claude-code "Optimize this blog post for AI citation: ~/blog/longevity-tips.md"
```

**Generate schema markup:**
```bash
claude-code "Generate FAQ and Article schema for ~/docs/guide.html"
```

**Deep analysis with voice search:**
```bash
claude-code "Deep SEO audit with voice optimization: ~/landing-page/index.tsx"
```

---

## Features

### 1. Content Analysis

**Supports multiple file types:**
- ✅ HTML files (`.html`)
- ✅ Markdown files (`.md`, `.mdx`)
- ✅ React/JSX components (`.jsx`, `.tsx`)

**Extracts:**
- Meta tags (title, description, keywords)
- Open Graph tags (og:title, og:description, og:image, etc.)
- Twitter Cards (twitter:card, twitter:title, etc.)
- Existing JSON-LD schema markup
- Content structure (headings, word count, TL;DR, FAQ, author)
- Heading hierarchy (H1, H2, H3)

### 2. Keyword Analysis

**Extracts 5 types of keywords:**
- **Primary** - Main topic keywords (H1, meta title, URL, first 100 words)
- **Semantic** - Related terms (H2/H3, body content)
- **LSI** - Co-occurring terms (natural language throughout)
- **Long-tail** - 3-8 word phrases (FAQ, H3 subheadings)
- **Question** - Who/what/where/when/why/how keywords (FAQ schema)

### 3. Schema Generation

**Generates JSON-LD schemas:**
- **FAQPage** - Highest AI citation probability
- **Article** - E-E-A-T signals (author credentials, dates)
- **HowTo** - Voice search optimized
- **BreadcrumbList** - Site hierarchy
- **Organization/LocalBusiness** - Entity recognition
- **Person** - Author profiles
- **Speakable** - Voice search enhancement

### 4. Platform-Specific Optimization

**ChatGPT** (Depth-focused):
- E-E-A-T content (Experience, Expertise, Authoritativeness, Trustworthiness)
- Named authors with credentials (MD, PhD = +40% citation probability)
- Educational/Wikipedia sources
- Original research

**Perplexity** (Freshness-focused):
- Transparent citations
- Specialized sources
- Current information (dateModified)
- Clear URL structure

**Claude** (Accuracy-focused):
- Credible sources
- Clear attribution
- Depth and accuracy
- Primary sources

**Gemini** (Community-focused):
- Google ecosystem integration
- Community-validated content
- Traditional authority signals
- Google My Business optimization

### 5. Voice Search Optimization

**Features:**
- Speakable schema generation
- 29-word answer optimization
- FAQ section analysis
- Featured snippet targeting
- Long-tail question keywords

**Stats:**
- 80%+ of answers from top 3 results
- 40.7% of voice answers from Featured Snippets
- 20.5% of people worldwide use voice search

### 6. Social Media Preview Optimization

**Analyzes and generates:**
- Open Graph tags (Facebook, LinkedIn, WhatsApp)
- Twitter Cards (summary, summary_large_image)
- iMessage optimization (og:title, og:image)
- Image specifications (1200×630px recommended)

### 7. Multi-Format Reports

**Generates:**
1. **Markdown report** - Source of truth, comprehensive details
2. **HTML dashboard** - Visual, browser-friendly, color-coded
3. **JSON export** - Structured data for automation
4. **PDF report** (optional) - Professional client-ready format

---

## Analysis Modes

### Quick Audit (5-10 minutes)
- Analyze content + Generate recommendations
- **Use for**: Rapid assessment, iterative testing
- **Output**: Markdown report only

### Standard Audit (10-20 minutes) ⭐ RECOMMENDED
- Full analysis + Keywords + Schema + Validation + Reports
- **Use for**: Most content audits
- **Output**: Markdown + HTML reports + Generated schemas

### Deep Audit (20-30 minutes)
- Comprehensive analysis + Entity mapping + Multi-format reports + PDF
- **Use for**: Client deliverables, comprehensive optimization
- **Output**: MD + HTML + JSON + PDF (optional) + All schemas

---

## How It Works

### 5-Phase Workflow

```
Phase 1: Clarify
  └─ Process user input, identify content type, determine goals

Phase 2: Plan
  └─ Load reference guides (progressive), plan script execution

Phase 3: Act
  └─ Execute analysis scripts, extract data, generate schemas

Phase 4: Verify
  └─ Validate outputs, check quality standards, calculate scores

Phase 5: Report
  └─ Generate multi-format reports, save to ~/Documents/
```

### Context Engineering

**Optimized for efficiency:**
- **Cached context**: 1800 tokens (90% cost reduction after first use)
- **Progressive disclosure**: Load reference files only when needed
- **Token budget**: ~7000 tokens per request (avg)
- **Performance**: 3-5s (cached), 10-15s (cold)

---

## Output Structure

### Report Location
```
~/Documents/SEO_Audit_[YYYY-MM-DD]_[HHMM]/
├── seo_audit_report.md          # Markdown source
├── seo_audit_dashboard.html     # Visual dashboard (auto-opens)
├── seo_audit_data.json          # Structured export
├── generated_schemas/           # Generated JSON-LD files
│   ├── faq_schema.json
│   ├── article_schema.json
│   └── howto_schema.json
└── seo_audit_report.pdf         # Optional PDF
```

### Report Sections

1. **Executive Summary**
   - Overall SEO score (0-100)
   - Top 3 wins (what's working)
   - Top 3 issues (critical fixes)

2. **Detailed Analysis**
   - Metadata (meta tags, OG, Twitter)
   - Schema markup (existing + recommendations)
   - Content structure (headings, TL;DR, FAQ, author)
   - Keyword analysis (primary, semantic, LSI, long-tail)
   - AI citation optimization (platform-specific)
   - Voice search readiness
   - Social preview quality

3. **Action Items** (Prioritized)
   - Critical (implement immediately)
   - High priority (this week)
   - Medium priority (this month)
   - Low priority (nice to have)

4. **Generated Assets**
   - Recommended schema markup (copy-paste ready)
   - Meta tags template
   - Optimized content snippets

---

## Examples

### Example 1: Blog Post Optimization

**Request:**
```bash
claude-code "Optimize my blog post for AI search: ~/blog/posts/longevity-guide.md"
```

**Result:**
- SEO score: 78/100 (Good)
- Missing FAQ schema → +35% citation boost
- Add author credentials → +40% citation boost
- Generated: Article schema + FAQ schema
- Output: Markdown + HTML reports

### Example 2: Landing Page Audit

**Request:**
```bash
claude-code "Deep audit of landing page with voice search: ~/app/pages/index.tsx"
```

**Result:**
- SEO score: 85/100 (Excellent)
- Voice-optimized FAQ present ✓
- Speakable schema recommended
- Social previews perfect (OG 1200×630px) ✓
- Generated: 5 schemas (FAQ, Article, HowTo, Speakable, Organization)
- Output: MD + HTML + JSON + PDF

### Example 3: Quick Check

**Request:**
```bash
claude-code "Quick SEO audit: ~/docs/about.html"
```

**Result:**
- SEO score: 72/100
- Top issue: Missing FAQ schema
- Top win: Perfect heading hierarchy
- Output: Markdown report only

---

## Technical Details

### Scripts (Python 3.7+)

Located in `~/.claude/skills/seo-geo-optimizer/scripts/`:

1. **analyze_content.py** - Core analysis engine
   - Parses HTML, Markdown, React/JSX
   - Extracts metadata, schema, content structure
   - Calculates SEO score

2. **schema_generator.py** - JSON-LD generation
   - FAQ, Article, HowTo, BreadcrumbList
   - Organization, Person, Speakable
   - Valid JSON-LD output

3. **metadata_validator.py** - Validation
   - Meta tags (title, description)
   - Open Graph (og:title, og:image, etc.)
   - Twitter Cards
   - Schema completeness

4. **keyword_analyzer.py** - Keyword extraction
   - Primary, semantic, LSI, long-tail
   - Question keywords (Who/what/where/when/why/how)
   - Keyword density calculation

5. **entity_extractor.py** - Entity recognition
   - People (names, credentials, job titles)
   - Organizations (company names, types)
   - Places (locations, service areas)
   - Relationship mapping

6. **audit_report.py** - Report generation
   - Markdown (source of truth)
   - HTML dashboard (visual)
   - JSON export (automation)
   - PDF (via generating-pdf skill)

### Reference Guides

Located in `~/.claude/skills/seo-geo-optimizer/reference/`:

- **platform-strategies.md** - ChatGPT, Perplexity, Claude, Gemini
- **schema-library.md** - All schema types with examples
- **voice-search-guide.md** - Voice optimization techniques
- **social-preview-guide.md** - Open Graph, Twitter Cards
- **citation-optimization-guide.md** - Content structure for AI
- **entity-seo-guide.md** - Knowledge Graph optimization

### Templates

Located in `~/.claude/skills/seo-geo-optimizer/templates/`:

- **meta-tags-template.html** - Complete meta tags
- **faq-schema.json** - FAQ JSON-LD template
- **article-schema.json** - Article with E-E-A-T
- **howto-schema.json** - HowTo for voice
- **breadcrumb-schema.json** - Site hierarchy
- **organization-schema.json** - Entity schema
- **person-schema.json** - Author profile

---

## Integration with Other Skills

### Works With:

**minimalist-website-mvp**
- Use this skill to audit websites generated by minimalist-website-mvp
- Complements (doesn't duplicate) built-in SEO features
- Can invoke minimalist-website-mvp for fixes

**generating-pdf**
- Automatically invoked for PDF reports (Deep mode)
- McKinsey-style professional formatting
- Client-ready deliverables

**deep-research**
- Similar workflow pattern (Clarify → Plan → Act → Verify → Report)
- Can analyze research content for SEO optimization
- Entity extraction works with research synthesis

---

## Troubleshooting

### Common Issues

**"Script not found"**
- **Cause**: Scripts not in correct location
- **Solution**: Verify `~/.claude/skills/seo-geo-optimizer/scripts/` exists

**"Permission denied"**
- **Cause**: Scripts not executable
- **Solution**: Run `chmod +x ~/.claude/skills/seo-geo-optimizer/scripts/*.py`

**"Python version error"**
- **Cause**: Python <3.7
- **Solution**: Upgrade to Python 3.7+ or use `python3` command

**"File not found"**
- **Cause**: Incorrect file path
- **Solution**: Verify path with `ls` command first

**"Schema validation failed"**
- **Cause**: Invalid JSON-LD syntax
- **Solution**: Check generated JSON for missing commas, brackets, quotes

**"Score seems wrong"**
- **Cause**: Analysis incomplete (Quick mode)
- **Solution**: Re-run with Standard or Deep mode

**"No recommendations"**
- **Cause**: Content already optimized
- **Solution**: Good! Score >90 means excellent SEO

---

## Performance

### Expected Performance (with prompt caching)

**First request (cold cache)**:
- Time: 10-15 seconds
- Cost: ~$0.05
- Tokens: ~1800 cached + 3000-5000 input + 2000-3000 output

**Subsequent requests (warm cache)**:
- Time: 3-5 seconds
- Cost: ~$0.005 (90% reduction)
- Cache lifetime: 5 minutes (refreshed on use), up to 1 hour

### Optimization Tips

- Use **Quick mode** for iterative testing (fastest)
- Use **Standard mode** for most audits (good balance) ⭐
- Use **Deep mode** only when comprehensive analysis needed (slowest but thorough)
- Reuse skill frequently to benefit from prompt caching

---

## Roadmap

### Phase 1 (Months 1-2): Core Functionality ✅ CURRENT
- Audit existing content
- Generate schema markup
- Validate metadata
- Basic recommendations

### Phase 2 (Months 3-4): AI Optimization
- Content rewriting for AI citation
- Platform-specific optimization
- Voice search enhancement
- Entity extraction and mapping

### Phase 3 (Months 5-6): Advanced Features
- Competitive analysis (compare to top 10 results)
- Automated monitoring (track metrics over time)
- A/B testing recommendations
- Integration with analytics tools

### Phase 4 (Months 7+): Ecosystem Integration
- Seamless workflow with minimalist-website-mvp
- Automatic PDF generation
- Export to SEO tools (Ahrefs, SEMrush)
- API mode for CI/CD pipelines

---

## Support

**Documentation**: See `PLAN.md` for comprehensive implementation details

**Issues**: Report issues to 199 Biotechnologies

**Updates**: Skill follows semantic versioning (major.minor.patch)

---

## License

Internal use - 199 Biotechnologies

---

**Version**: 1.0
**Last Updated**: November 11, 2025
**Maintainer**: 199 Biotechnologies
