---
name: seo-geo-optimizer
description: |
  **WHAT**: Analyzes and optimizes content for traditional SEO, AI search engines (ChatGPT, Perplexity, Claude, Gemini), voice assistants (Google Assistant, Siri, Alexa), and social media previews (Open Graph, Twitter Cards, WhatsApp/iMessage).

  **WHEN**: Use when analyzing existing content, auditing SEO implementation, generating schema markup (FAQ, Article, HowTo), validating metadata completeness, extracting keywords, or optimizing for AI citation probability.

  **INPUT**: Any content file (HTML, Markdown, React/JSX, MDX) or content URL.

  **OUTPUT**: Comprehensive SEO/GEO audit report with:
  - SEO score (0-100)
  - Issues list with solutions
  - Platform-specific recommendations (ChatGPT, Perplexity, Claude, Gemini)
  - Generated schema markup (JSON-LD)
  - Keyword analysis (primary, semantic, LSI, long-tail)
  - Multi-format reports (Markdown, HTML, JSON, optionally PDF)

  **EXCLUSIONS**: Do NOT use for:
  - Website generation (use minimalist-website-mvp skill instead)
  - PDF creation (this skill generates reports, but invoke generating-pdf for final PDF)
  - Research synthesis (use deep-research skill instead)
  - General content writing (this analyzes/optimizes existing content)
allowed-tools: Read, Write, Bash, Grep, Glob, WebSearch, Task
---

<!-- ==================== CACHED CONTEXT START ==================== -->
<!--
  CONTEXT ENGINEERING NOTES:
  - This section optimized for prompt caching (target: 1800-2000 tokens)
  - Contains STATIC, REUSABLE content across all requests
  - Cache lifetime: 5 minutes (refreshed on use), up to 1 hour
  - 90% cost reduction, 85% latency reduction after first request
  - All methodology, patterns, and standards are cacheable
-->

# SEO/GEO Optimizer: AI-Native Content Analysis & Optimization Protocol

## Core Purpose

Analyze and optimize digital content for maximum visibility across traditional search engines (Google, Bing), AI search platforms (ChatGPT, Perplexity, Claude, Gemini), voice assistants (Google Assistant, Siri, Alexa), and social media previews (Facebook, Twitter/X, LinkedIn, WhatsApp, iMessage).

**2025 Context**: AI-referred traffic has grown 527% (Jan-May 2025), with 40.58% of AI citations coming from top 10 SERP results. Citation probability increases 33% for #1 ranking positions with proper optimization.

## Context Engineering Strategy

**Pattern**: Prompt caching + Progressive disclosure + Structured output
**Token budget**: 1800 tokens cached + 2000-5000 variable input + 1500-2500 output
**Expected reuse**: High (content audits are iterative)
**Cache efficiency**: 90% cost reduction, 85% latency reduction after first request

## When to Use This Skill

✅ **Use for:**
- Auditing existing content (HTML, Markdown, React/JSX, MDX files)
- Analyzing SEO implementation completeness
- Generating schema markup (FAQ, Article, HowTo, BreadcrumbList, Organization)
- Validating metadata (meta tags, Open Graph, Twitter Cards)
- Extracting keywords (primary, semantic, LSI, long-tail, question-based)
- Optimizing content for AI citation (ChatGPT, Perplexity, Claude, Gemini)
- Voice search optimization (29-word answers, Speakable schema)
- Social media preview optimization (1200×630px images, proper tags)
- Generating comprehensive audit reports (Markdown, HTML, JSON, PDF)
- Content rewriting recommendations for LLM visibility

✅ **Trigger patterns:**
- "Audit the SEO of [page/file]"
- "Optimize [content] for AI search"
- "Generate schema markup for [content]"
- "Check metadata completeness"
- "Analyze keywords in [file]"
- "How can I improve AI citation probability?"
- "Optimize for voice search"
- "Fix social media previews"

❌ **Don't use for:**
- **Website generation** → Use `minimalist-website-mvp` skill (already has comprehensive AI-native SEO built-in)
- **PDF creation** → This skill generates audit reports; invoke `generating-pdf` skill for professional PDF conversion
- **Research synthesis** → Use `deep-research` skill (different domain)
- **General content writing** → This skill analyzes and optimizes existing content, doesn't create new content from scratch
- **Real-time monitoring** → This is for on-demand audits, not continuous monitoring (would need MCP server)

## Decision Tree (Execute First)

```
1. Analyze Request Type
   ├─ "Build a website with SEO" → STOP: Use minimalist-website-mvp skill
   ├─ "Research [topic]" → STOP: Use deep-research skill
   ├─ "Create a report PDF" → STOP: Use generating-pdf skill
   └─ "Audit / Optimize / Analyze SEO/GEO" → CONTINUE

2. Select Analysis Mode
   ├─ Quick Audit (5-10 min)
   │   └─ Analyze content + Generate recommendations only
   │
   ├─ Standard Audit (10-20 min) ← MOST COMMON
   │   └─ Analyze + Extract keywords + Generate schema + Validate + Report (MD + HTML)
   │
   └─ Deep Audit (20-30 min)
       └─ Full analysis + Keyword extraction + Schema generation + Entity mapping +
           Multi-format reports (MD + HTML + JSON) + Optionally invoke generating-pdf

3. Identify Content Type
   ├─ HTML file (.html) → Use analyze_content.py (HTML parser)
   ├─ Markdown file (.md, .mdx) → Use analyze_content.py (Markdown parser)
   ├─ React/JSX file (.jsx, .tsx) → Use analyze_content.py (JSX parser)
   └─ URL → Fetch content first, then analyze

4. Determine Optimization Goals
   ├─ Traditional SEO → Meta tags + Schema + Technical SEO
   ├─ AI Citation (GEO/LLMO) → Content structure + E-E-A-T + Platform-specific
   ├─ Voice Search → Speakable schema + 29-word answers + FAQ
   ├─ Social Previews → Open Graph + Twitter Cards + Image optimization
   └─ Comprehensive → ALL OF THE ABOVE
```

## Workflow (Clarify → Plan → Act → Verify → Report)

### Phase 1: Clarify (User Input Processing)

**Goal**: Understand user request and gather requirements

**Steps**:
1. **Identify content source**
   - File path provided? Use Read tool
   - URL provided? Fetch content first
   - Multiple files? Process sequentially

2. **Determine content type**
   - Check file extension (.html, .md, .jsx, .tsx)
   - Inspect content structure
   - Select appropriate parser

3. **Clarify optimization goals**
   - Ask if not clear: "What are your primary goals? (Traditional SEO / AI Citation / Voice Search / Social Previews / All)"
   - Default: Comprehensive (all optimizations)

4. **Select analysis mode**
   - Ask if not clear: "What level of detail? (Quick / Standard / Deep)"
   - Default: Standard mode

**Stop Rules**:
- If request is for website generation → Recommend minimalist-website-mvp skill
- If request is for PDF creation only → Recommend generating-pdf skill
- If content source unclear → Ask user to specify file path or URL

### Phase 2: Plan (Analysis Strategy)

**Goal**: Outline execution plan and load necessary references

**Steps**:
1. **Load reference guides** (progressive disclosure)
   - For AI citation → Load `reference/citation-optimization-guide.md`
   - For schema generation → Load `reference/schema-library.md`
   - For voice search → Load `reference/voice-search-guide.md`
   - For social previews → Load `reference/social-preview-guide.md`
   - For platform-specific → Load `reference/platform-strategies.md`

2. **Plan script execution order**
   ```
   Standard Mode (most common):
   1. analyze_content.py → Extract metadata, structure, existing schema
   2. keyword_analyzer.py → Extract keywords (primary, semantic, LSI, long-tail)
   3. schema_generator.py → Generate recommended schemas (FAQ, Article, HowTo)
   4. metadata_validator.py → Validate completeness, calculate score
   5. audit_report.py → Generate reports (MD, HTML, JSON)
   ```

3. **Outline report structure**
   - Executive summary (score, top 3 issues, top 3 wins)
   - Detailed analysis (metadata, schema, content structure, keywords)
   - Platform-specific recommendations (ChatGPT, Perplexity, Claude, Gemini)
   - Action items (prioritized by impact)
   - Generated assets (schemas, meta tags, templates)

### Phase 3: Act (Execute Analysis)

**Goal**: Run scripts and gather data

**Steps**:
1. **Execute analyze_content.py**
   ```bash
   python ~/.claude/skills/seo-geo-optimizer/scripts/analyze_content.py [file_path]
   ```
   - Returns: JSON with metadata, structure, existing schema, issues, score

2. **Execute keyword_analyzer.py** (if Standard or Deep mode)
   ```bash
   python ~/.claude/skills/seo-geo-optimizer/scripts/keyword_analyzer.py [file_path]
   ```
   - Returns: JSON with primary, semantic, LSI, long-tail, question keywords

3. **Execute schema_generator.py** (if Standard or Deep mode)
   ```bash
   python ~/.claude/skills/seo-geo-optimizer/scripts/schema_generator.py \
     --content [file_path] \
     --types faq,article,howto
   ```
   - Returns: JSON-LD schemas ready for implementation

4. **Execute metadata_validator.py** (if Standard or Deep mode)
   ```bash
   python ~/.claude/skills/seo-geo-optimizer/scripts/metadata_validator.py [file_path]
   ```
   - Returns: Validation results, completeness score

5. **Execute entity_extractor.py** (if Deep mode)
   ```bash
   python ~/.claude/skills/seo-geo-optimizer/scripts/entity_extractor.py [file_path]
   ```
   - Returns: Extracted entities (people, organizations, places)

### Phase 4: Verify (Validation & Quality Check)

**Goal**: Ensure analysis completeness and accuracy

**Quality Standards**:
- [ ] **Analysis completeness**: All required data extracted (metadata, schema, structure)
- [ ] **Schema validity**: Generated JSON-LD passes validation (valid JSON, correct @type)
- [ ] **Score accuracy**: SEO score reflects actual issues (0-100 scale, evidence-based)
- [ ] **Recommendation quality**: Specific, actionable, prioritized by impact
- [ ] **Citation probability**: Recommendations target +30-40% citation boost (backed by research)

**Validation Checks**:
1. **Metadata validation**
   - Meta title: 50-60 characters? ✓
   - Meta description: 150-160 characters? ✓
   - Open Graph tags: title, description, image (1200×630px)? ✓
   - Twitter Cards: card type, title, description, image? ✓

2. **Schema validation**
   - JSON-LD syntax valid? ✓
   - Required properties present (@context, @type, mandatory fields)? ✓
   - Schema types appropriate for content (FAQ for Q&A, Article for blog)? ✓

3. **Content structure validation**
   - TL;DR in first 40-60 words? ✓
   - H1 exists and unique? ✓
   - H2→H3→bullet hierarchy? ✓
   - FAQ section present? ✓
   - Author credentials visible? ✓

**Stop Rules**:
- If validation fails → Identify issue, provide solution, re-run validation
- If score <60 → Flag as "Poor SEO implementation, urgent fixes needed"
- If critical issues found (missing meta title, no schema) → Highlight in report

### Phase 5: Report (Multi-Format Output)

**Goal**: Generate comprehensive, actionable reports

**Report Formats**:

1. **Markdown Report** (source of truth)
   - Save to: `~/Documents/SEO_Audit_[date]/seo_audit_report.md`
   - Structure: Executive Summary → Detailed Analysis → Recommendations → Action Items → Generated Assets

2. **HTML Dashboard** (visual, browser-friendly)
   - Save to: `~/Documents/SEO_Audit_[date]/seo_audit_dashboard.html`
   - Features: Color-coded scores, expandable sections, copy-paste code blocks
   - Auto-open in browser

3. **JSON Export** (automation-friendly)
   - Save to: `~/Documents/SEO_Audit_[date]/seo_audit_data.json`
   - Structure: Structured data for CI/CD integration, analytics

4. **PDF Report** (optional, for clients)
   - Invoke generating-pdf skill via Task tool
   - Professional formatting (McKinsey-style)
   - Only if user requests or Deep mode selected

**Report Structure**:

```markdown
# SEO/GEO Audit Report
**Site/Page**: [URL or file path]
**Audit Date**: [YYYY-MM-DD]
**SEO Score**: [0-100] ([Poor/Fair/Good/Excellent])

## Executive Summary
### Overall Assessment
[2-3 sentence summary of findings]

### Top 3 Wins ✅
1. [What's working well]
2. [What's working well]
3. [What's working well]

### Top 3 Issues ❌
1. [Critical issue] → [Quick fix]
2. [Important issue] → [Solution]
3. [Improvement opportunity] → [Recommendation]

## Detailed Analysis

### 1. Metadata Analysis
**Meta Title**: [Status] - [Findings]
**Meta Description**: [Status] - [Findings]
**Open Graph Tags**: [Status] - [Findings]
**Twitter Cards**: [Status] - [Findings]

### 2. Schema Markup Analysis
**Existing Schemas**: [List of found schemas]
**Missing Schemas**: [Recommended additions]
**Validation Results**: [Pass/Fail with details]

### 3. Content Structure Analysis
**Word Count**: [Number]
**TL;DR Present**: [Yes/No]
**Heading Structure**: [H1: X, H2: Y, H3: Z]
**FAQ Section**: [Yes/No]
**Author Attribution**: [Yes/No]

### 4. Keyword Analysis
**Primary Keywords**: [List]
**Semantic Keywords**: [List]
**LSI Keywords**: [List]
**Long-tail Keywords**: [List]
**Question Keywords**: [List]

### 5. AI Citation Optimization (GEO/LLMO)
**Current Citation Probability**: [Estimated %]
**Target with Fixes**: [Estimated %]

#### Platform-Specific Recommendations
**ChatGPT** (Depth-focused):
- [Recommendation 1]
- [Recommendation 2]

**Perplexity** (Freshness-focused):
- [Recommendation 1]
- [Recommendation 2]

**Claude** (Accuracy-focused):
- [Recommendation 1]
- [Recommendation 2]

**Gemini** (Community-focused):
- [Recommendation 1]
- [Recommendation 2]

### 6. Voice Search Optimization
**Speakable Schema**: [Present/Missing]
**29-word Answers**: [Count found]
**FAQ for Voice**: [Optimized/Needs work]

### 7. Social Media Preview Optimization
**Open Graph Image**: [Size, format]
**Twitter Card Image**: [Size, format]
**iMessage Preview**: [Optimized/Needs work]
**WhatsApp Preview**: [Optimized/Needs work]

## Action Items (Prioritized by Impact)

### Critical (Implement Immediately)
1. [ ] [Action item with expected impact]
2. [ ] [Action item with expected impact]

### High Priority (Implement This Week)
1. [ ] [Action item with expected impact]
2. [ ] [Action item with expected impact]

### Medium Priority (Implement This Month)
1. [ ] [Action item with expected impact]

### Low Priority (Nice to Have)
1. [ ] [Action item with expected impact]

## Generated Assets

### Recommended Schema Markup

#### FAQ Schema
```json
[Generated FAQ JSON-LD]
```

#### Article Schema
```json
[Generated Article JSON-LD]
```

#### HowTo Schema
```json
[Generated HowTo JSON-LD]
```

### Recommended Meta Tags
```html
[Complete meta tags with Open Graph and Twitter Cards]
```

### Optimized Content Snippets
[If content rewriting recommendations provided]

## Next Steps
1. Implement Critical action items
2. Test changes in staging environment
3. Validate with metadata_validator.py
4. Re-audit after implementation (target: +20 points)
5. Monitor AI citation rates (ChatGPT, Perplexity, Claude)

---

**Report Generated By**: Claude Code - SEO/GEO Optimizer Skill v1.0
**Analysis Time**: [Duration]
```

## Quality Standards (All Outputs Must Meet)

**1. Analysis Completeness**
- ✅ All metadata extracted (title, description, OG, Twitter, schema)
- ✅ Content structure analyzed (word count, headings, TL;DR, FAQ, author)
- ✅ Keywords extracted (minimum: 5 primary + 10 semantic + 5 long-tail)
- ✅ Issues identified with specific solutions
- ✅ Recommendations prioritized by impact

**2. Schema Generation**
- ✅ Valid JSON-LD syntax (passes JSON validation)
- ✅ Correct @type for content (FAQ for Q&A, Article for blog, HowTo for tutorials)
- ✅ All required properties present (as per schema.org specification)
- ✅ E-E-A-T signals included where applicable (author credentials, dateModified)
- ✅ Speakable schema for voice search

**3. Recommendation Quality**
- ✅ Specific and actionable (not vague "improve SEO")
- ✅ Evidence-based (cite research: "+40% citation probability with author credentials")
- ✅ Prioritized by impact (Critical > High > Medium > Low)
- ✅ Platform-specific where applicable (ChatGPT vs. Perplexity vs. Claude)
- ✅ Quantified targets (e.g., "Add FAQ schema → +35% citation boost")

**4. Report Accuracy**
- ✅ SEO score reflects actual issues (0-100, evidence-based)
- ✅ No false positives (if tag exists, don't report as missing)
- ✅ No false negatives (if tag missing, must report)
- ✅ Citations accurate (research findings, statistics)
- ✅ Code snippets ready to copy-paste (no placeholders)

**5. Information Density**
- ✅ Target: >1.5 claims per 100 tokens
- ✅ No hedging language ("might", "could", "possibly" without hypothesis flag)
- ✅ Quantified claims ("29-word answers", "1200×630px images", not "short answers", "proper images")
- ✅ Precise statistics with sources ("527% LLM traffic growth, Jan-May 2025")

## Output Format (Structured Multi-Format)

**Primary Output**: Markdown report (source of truth)
**Secondary Outputs**: HTML dashboard, JSON export
**Optional Output**: PDF report (via generating-pdf skill, only if requested or Deep mode)

**File Naming Convention**:
```
~/Documents/SEO_Audit_[YYYY-MM-DD]_[HHMM]/
├── seo_audit_report.md          # Markdown source
├── seo_audit_dashboard.html     # Visual dashboard
├── seo_audit_data.json          # Structured export
├── generated_schemas/           # Generated JSON-LD files
│   ├── faq_schema.json
│   ├── article_schema.json
│   └── howto_schema.json
└── seo_audit_report.pdf         # Optional PDF (via generating-pdf)
```

<!-- ==================== CACHED CONTEXT END ==================== -->

## Execution Instructions

**IMPORTANT**: The following steps use DYNAMIC content (varies per request)

### Input Processing

1. **Receive user request**
   - File path: Use Read tool to load content
   - URL: Fetch content first (WebSearch or WebFetch)
   - Multiple files: Process sequentially

2. **Validate input**
   - Check file exists (if file path)
   - Check content readable
   - Identify file type (.html, .md, .jsx, .tsx)

3. **Clarify requirements** (if unclear)
   - Use AskUserQuestion for:
     - Analysis mode (Quick / Standard / Deep)
     - Optimization goals (Traditional SEO / AI Citation / Voice / Social / All)
     - Output format (MD only, or MD + HTML + JSON, or also PDF)

### Analysis Execution

**Follow cached workflow above** (Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5)

1. **Clarify**: Process user input, identify content type, determine goals
2. **Plan**: Load reference guides (progressive), plan script execution
3. **Act**: Execute scripts (analyze_content.py, keyword_analyzer.py, schema_generator.py, etc.)
4. **Verify**: Validate outputs against quality standards
5. **Report**: Generate multi-format reports, save to ~/Documents/SEO_Audit_[date]/

### Output Generation

1. **Generate Markdown report** (always)
   - Follow cached report structure
   - Include all sections (Executive Summary → Detailed Analysis → Action Items → Generated Assets)
   - Save to ~/Documents/SEO_Audit_[date]/seo_audit_report.md

2. **Generate HTML dashboard** (if Standard or Deep mode)
   - Convert Markdown to HTML with styling
   - Add color-coded scores, expandable sections
   - Save to ~/Documents/SEO_Audit_[date]/seo_audit_dashboard.html
   - Open in browser automatically

3. **Generate JSON export** (if Deep mode)
   - Structured data with all findings
   - Save to ~/Documents/SEO_Audit_[date]/seo_audit_data.json

4. **Generate PDF report** (if requested or Deep mode)
   - Invoke generating-pdf skill via Task tool:
     ```
     Task(
       subagent_type="general-purpose",
       skill="generating-pdf",
       description="Generate professional PDF from SEO audit report",
       prompt=f"Convert this Markdown report to professional PDF: {report_md_path}"
     )
     ```

### Validation

**Before delivering output, verify**:
- [ ] All sections complete (no missing data)
- [ ] Schema JSON-LD valid (passes JSON validation)
- [ ] Recommendations specific and actionable
- [ ] SEO score evidence-based (matches issues found)
- [ ] Code snippets copy-paste ready (no placeholders)
- [ ] Reports saved to correct location

### Error Handling

**If script execution fails**:
1. Check file exists and is readable
2. Verify Python version (requires Python 3.7+)
3. Check script permissions (chmod +x if needed)
4. Provide clear error message with solution
5. Offer to retry or skip non-critical step

**If validation fails**:
1. Identify specific failure (schema syntax, missing field, etc.)
2. Provide fix or workaround
3. Re-run validation
4. Document issue in report

## Examples

### Example 1: Quick Audit (HTML File)

**User Request**:
> "Audit the SEO of my about page: ~/project/src/pages/about.html"

**Execution**:
1. Read ~/project/src/pages/about.html
2. Execute analyze_content.py
3. Generate quick recommendations
4. Output Markdown report only

**Output** (truncated):
```markdown
# SEO/GEO Audit Report - Quick Analysis
**SEO Score**: 72/100 (Good)

## Top 3 Issues ❌
1. Missing FAQ schema (highest AI citation probability) → Add FAQ JSON-LD
2. No author credentials visible → Add author bio with MD/PhD
3. Meta description too long (185 chars) → Shorten to 150-160 chars

## Top 3 Wins ✅
1. TL;DR present in first 50 words ✓
2. Open Graph tags complete ✓
3. Proper H1→H2→H3 hierarchy ✓

[Rest of report...]
```

### Example 2: Standard Audit (Markdown File)

**User Request**:
> "Optimize this blog post for AI citation: ~/blog/posts/longevity-tips.md"

**Execution**:
1. Read ~/blog/posts/longevity-tips.md
2. Execute analyze_content.py + keyword_analyzer.py + schema_generator.py + metadata_validator.py
3. Generate platform-specific recommendations (ChatGPT, Perplexity, Claude, Gemini)
4. Generate schemas (Article + FAQ + HowTo)
5. Output Markdown + HTML reports

**Output**:
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_report.md`
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_dashboard.html` (auto-opened in browser)
- `~/Documents/SEO_Audit_2025-11-11_2230/generated_schemas/` (article_schema.json, faq_schema.json, howto_schema.json)

### Example 3: Deep Audit (React/JSX Component)

**User Request**:
> "Deep analysis of my landing page for voice search and social previews: ~/app/pages/index.tsx"

**Execution**:
1. Read ~/app/pages/index.tsx
2. Execute ALL scripts (analyze_content.py, keyword_analyzer.py, schema_generator.py, metadata_validator.py, entity_extractor.py)
3. Load voice-search-guide.md + social-preview-guide.md references
4. Generate all schemas (FAQ, Article, HowTo, Speakable, Organization)
5. Analyze voice search optimization (29-word answers, Speakable schema)
6. Analyze social previews (OG images, Twitter Cards, WhatsApp/iMessage)
7. Output Markdown + HTML + JSON reports
8. Invoke generating-pdf for professional PDF

**Output**:
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_report.md`
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_dashboard.html`
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_data.json`
- `~/Documents/SEO_Audit_2025-11-11_2230/generated_schemas/` (5 schema files)
- `~/Documents/SEO_Audit_2025-11-11_2230/seo_audit_report.pdf` (via generating-pdf)

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| **Script not found** | Scripts not in correct location | Verify scripts are in `~/.claude/skills/seo-geo-optimizer/scripts/` |
| **Permission denied** | Scripts not executable | Run `chmod +x ~/.claude/skills/seo-geo-optimizer/scripts/*.py` |
| **Python version error** | Python <3.7 | Upgrade to Python 3.7+ or use `python3` command |
| **File not found** | Incorrect file path | Verify file path with `ls` command first |
| **Schema validation failed** | Invalid JSON-LD syntax | Check for missing commas, brackets, or quotes in generated JSON |
| **Score seems wrong** | Analysis incomplete | Re-run with Standard or Deep mode for full analysis |
| **No recommendations** | Content already optimized | Good! Report will show score >90 with minimal issues |
| **PDF generation failed** | generating-pdf skill not available | Skip PDF or install generating-pdf skill |

## Performance Notes

**Expected Performance** (with prompt caching):
- **First request (cold cache)**: 10-15s, ~$0.05
- **Subsequent requests (warm cache)**: 3-5s, ~$0.005 (90% cost reduction)
- **Token usage**: ~1800 cached + 3000-5000 input + 2000-3000 output

**Optimization Tips**:
- Use Quick mode for iterative testing (faster)
- Use Standard mode for most audits (good balance)
- Use Deep mode only when comprehensive analysis needed (slower but thorough)
- Reuse skill frequently to benefit from prompt caching

---

**Skill Version**: 1.0
**Last Updated**: 2025-11-11
**Maintainer**: 199 Biotechnologies
**License**: Internal use
