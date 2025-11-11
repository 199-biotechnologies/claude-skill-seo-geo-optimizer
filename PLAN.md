# SEO/GEO Optimizer Skill - Implementation Plan

**Created**: November 11, 2025
**Version**: 1.0
**Status**: In Progress

---

## Executive Summary

**Purpose**: Create a standalone Claude skill that analyzes and optimizes content for:
- Traditional SEO (meta tags, structured data)
- Generative Engine Optimization (GEO) - AI search engines (ChatGPT, Perplexity, Claude, Gemini)
- Large Language Model Optimization (LLMO) - Citation probability enhancement
- Voice Search (Google Assistant, Siri, Alexa)
- Social Media Previews (Open Graph, Twitter Cards, WhatsApp/iMessage)

**Key Differentiator**: Works with ANY content (HTML, Markdown, React/JSX), not just website generation.

**Complements Existing Skills**:
- `minimalist-website-mvp` - Website generator with built-in SEO (this skill audits existing content)
- `deep-research` - Research synthesis (this skill optimizes content structure)
- `generating-pdf` - PDF generation (this skill produces audit reports that can be converted to PDF)

---

## Research Findings (2025)

### LLM Traffic Growth
- **527% increase** in AI-referred sessions (Jan-May 2025)
- **1,200% growth** in generative AI traffic (Jul 2024-Feb 2025)
- **40.58%** of AI citations come from top 10 SERP results
- **33.07%** citation probability for #1 ranking position

### Platform Market Share
- **ChatGPT**: 40-60% of LLM traffic (dominant)
- **Perplexity**: 0.073%+ specialized traffic
- **Claude**: Growing, prioritizes credible sources
- **Gemini**: Google integration, community validation

### Platform-Specific Preferences

**ChatGPT**:
- High E-E-A-T content (Experience, Expertise, Authoritativeness, Trustworthiness)
- Named authors with credentials (MD, PhD = +40% citation probability)
- Educational/Wikipedia sources preferred
- Original research valued
- Schema-enhanced data

**Perplexity**:
- Transparent citations required
- Specialized sources preferred
- YouTube content indexed
- Clear URL structure important
- Current information (dateModified critical)

**Claude**:
- Credible sources mandatory
- Clear attribution required
- Depth and accuracy prioritized
- Well-structured content
- Primary sources preferred over secondary

**Gemini**:
- Google ecosystem integration
- Community-validated content (Reddit-style)
- Traditional authority signals
- Google My Business optimization
- Local Pack integration

### Voice Search Statistics
- **20.5%** of people worldwide use voice search
- **8.4 billion** voice assistants globally
- **80%+** of answers come from top 3 results
- **29 words** average voice answer length
- **52%** faster page load required
- **40.7%** of voice answers from Featured Snippets

**Platform Breakdown (US)**:
- Google Assistant: 92M users (GMB + Local Pack sources)
- Siri: 86.5M users (Yelp as primary source)
- Alexa: Growing (Bing + Yelp + Yext sources)

---

## Implementation Phases

### Phase 1: Core Structure (Week 1) ✅ IN PROGRESS

**Deliverables**:
1. Directory structure created
2. `skill.md` with:
   - Frontmatter (name, description, allowed-tools)
   - Cacheable static context (>1024 tokens)
   - Decision tree (when to use / not use)
   - Progressive reference loading
   - Clear workflow (Clarify → Plan → Act → Verify → Report)
3. `README.md` with quick start guide
4. `analyze_content.py` basic script (HTML parser, meta extraction)

**Context Engineering Principles**:
- Cached section: 1500-2000 tokens (90% cost reduction after first use)
- Progressive disclosure (load references on-demand)
- Clear boundaries (CACHED CONTEXT START/END markers)
- Offline operation (Python stdlib only)

### Phase 2: Reference Guides (Week 2)

**Deliverables** (`reference/` directory):

1. **platform-strategies.md** - Platform-specific optimization
   - ChatGPT optimization (E-E-A-T, author credentials, educational content)
   - Perplexity optimization (citations, freshness, specialized sources)
   - Claude optimization (credibility, attribution, primary sources)
   - Gemini optimization (Google ecosystem, community validation)

2. **schema-library.md** - Comprehensive schema reference
   - FAQPage (highest citation probability)
   - Article (E-E-A-T signals)
   - HowTo (voice search optimized)
   - BreadcrumbList (site hierarchy)
   - Organization/LocalBusiness (entity recognition)
   - Person (author profiles)
   - Speakable (voice search enhancement)

3. **voice-search-guide.md** - Voice optimization
   - Speakable schema implementation
   - 29-word answer optimization
   - Featured snippet targeting
   - Long-tail question keywords
   - Natural language conversational tone

4. **social-preview-guide.md** - Social media optimization
   - Open Graph protocol (Facebook, LinkedIn, WhatsApp)
   - Twitter Cards (summary, summary_large_image)
   - iMessage optimization (og:title, og:image only)
   - Image specifications (1200×630px landscape, 400×400px square)
   - Preview testing tools

5. **citation-optimization-guide.md** - Content structure for AI
   - TL;DR in first 40-60 words (35% citation boost)
   - First 150 words highest weight
   - H2→H3→bullet structure (+40% citation probability)
   - Statistics every 150-200 words
   - FAQ section with natural language
   - Author credentials visible (40% boost)
   - Short paragraphs (3-4 sentences)

6. **entity-seo-guide.md** - Knowledge Graph optimization
   - Entity recognition (people, organizations, places)
   - Relationship mapping (parent company, affiliates)
   - Structured data markup
   - Authority signals
   - (Leverage content from minimalist-website-mvp skill)

### Phase 3: Scripts & Automation (Week 2-3)

**Deliverables** (`scripts/` directory):

1. **analyze_content.py** - Core analysis engine
   - Parse HTML files (extract meta tags, headings, content structure)
   - Parse Markdown files (extract frontmatter, YAML, content)
   - Parse React/JSX files (extract component metadata, props)
   - Extract existing schema markup (JSON-LD)
   - Analyze content structure (TL;DR, FAQ, author info)
   - Calculate SEO score (0-100)
   - Generate issue list and recommendations

2. **schema_generator.py** - JSON-LD generation
   - generate_faq_schema(faqs) → FAQ JSON-LD
   - generate_article_schema(...) → Article with E-E-A-T
   - generate_howto_schema(...) → HowTo for voice
   - generate_breadcrumb_schema(items) → BreadcrumbList
   - generate_organization_schema(...) → Organization/LocalBusiness
   - generate_person_schema(...) → Person/author profile

3. **metadata_validator.py** - Meta tag validation
   - validate_meta_tags() - Title (50-60 chars), description (150-160 chars)
   - validate_open_graph() - og:title, og:description, og:image (1200×630)
   - validate_twitter_cards() - twitter:card, twitter:image
   - validate_schema() - JSON-LD structure and completeness
   - calculate_validation_score()

4. **keyword_analyzer.py** - Keyword extraction
   - extract_primary_keywords() - Main topic keywords
   - extract_semantic_keywords() - Related terms (H2/H3, body)
   - extract_lsi_keywords() - Co-occurring terms (natural language)
   - extract_longtail_keywords() - 3-8 word phrases (FAQ, H3)
   - extract_question_keywords() - Who/what/where/when/why/how
   - calculate_keyword_density()

5. **entity_extractor.py** - Entity recognition
   - extract_person_entities() - Names, credentials, job titles
   - extract_organization_entities() - Company names, types
   - extract_place_entities() - Locations, service areas
   - map_relationships() - Parent companies, affiliates
   - generate_entity_schema()

6. **audit_report.py** - Report generation
   - generate_markdown_report() - Comprehensive Markdown report
   - generate_html_dashboard() - Visual dashboard (McKinsey-style)
   - generate_json_export() - Structured data for automation
   - generate_pdf_report() - Professional PDF (via generating-pdf skill)
   - Open report in browser automatically

**Technical Requirements**:
- Python stdlib only (no external dependencies)
- Offline operation (no API calls)
- Clear error messages with solutions
- JSON output for automation
- Modular functions for composability

### Phase 4: Templates (Week 3)

**Deliverables** (`templates/` directory):

1. **meta-tags-template.html** - Complete meta tags
```html
<!-- SEO Meta Tags -->
<title>{{TITLE}} | {{SITE_NAME}}</title>
<meta name="description" content="{{DESCRIPTION}}">
<meta name="keywords" content="{{KEYWORDS}}">

<!-- Open Graph -->
<meta property="og:title" content="{{OG_TITLE}}">
<meta property="og:description" content="{{OG_DESCRIPTION}}">
<meta property="og:image" content="{{OG_IMAGE_URL}}">
<meta property="og:url" content="{{PAGE_URL}}">
<meta property="og:type" content="{{OG_TYPE}}">
<meta property="og:site_name" content="{{SITE_NAME}}">

<!-- Twitter Cards -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{TWITTER_TITLE}}">
<meta name="twitter:description" content="{{TWITTER_DESCRIPTION}}">
<meta name="twitter:image" content="{{TWITTER_IMAGE_URL}}">
```

2. **faq-schema.json** - FAQ template
3. **article-schema.json** - Article with E-E-A-T
4. **howto-schema.json** - HowTo for voice
5. **breadcrumb-schema.json** - Site hierarchy
6. **organization-schema.json** - Entity schema
7. **person-schema.json** - Author profile
8. **audit-report-template.md** - Report structure

**Template Features**:
- Variable placeholders ({{VARIABLE}})
- Comments explaining each field
- 2025 best practices built-in
- Copy-paste ready
- Validation-friendly

### Phase 5: Examples & Testing (Week 4)

**Deliverables** (`examples/` directory):

1. **medical-clinic/**
   - `before-audit.html` - Original content
   - `audit-report.md` - Generated audit with issues/recommendations
   - `recommended-schema.json` - FAQ + Article schemas
   - `after-optimization.html` - Optimized content
   - `voice-optimization.md` - Speakable implementation guide

2. **consulting-firm/**
   - `before-audit.html` - Original content
   - `audit-report.md` - Generated audit
   - `entity-seo-implementation.md` - Knowledge Graph setup
   - `knowledge-graph-setup.json` - Organization + Person schemas
   - `llmo-strategy.md` - Platform-specific tactics

3. **saas-landing-page/**
   - `before-audit.html` - Original content
   - `audit-report.md` - Generated audit
   - `llmo-optimization.md` - AI citation optimization
   - `voice-search-setup.json` - FAQ + HowTo schemas
   - `conversion-optimization.md` - CTA + technical SEO

**Testing Checklist**:
- [ ] Audit HTML file (meta tags, schema, content structure)
- [ ] Audit Markdown file (frontmatter, YAML, content)
- [ ] Audit React/JSX file (components, props, metadata)
- [ ] Generate FAQ schema from content
- [ ] Generate Article schema with E-E-A-T signals
- [ ] Generate complete meta tags (OG + Twitter)
- [ ] Extract semantic keywords (primary, LSI, long-tail)
- [ ] Validate existing schema markup
- [ ] Generate multi-format reports (MD, HTML, JSON)
- [ ] Invoke generating-pdf skill for PDF output
- [ ] Test with minimalist-website-mvp integration
- [ ] Verify offline operation (no network required)
- [ ] Check Python stdlib-only requirement

---

## Technical Architecture

### Context Engineering Strategy

**Cached Static Context** (1500-2000 tokens):
- Core methodology
- Decision tree (when to use / not use)
- Workflow overview (Clarify → Plan → Act → Verify → Report)
- Quality standards

**Progressive Reference Loading**:
- Load platform-strategies.md only when needed
- Load schema-library.md only for schema generation
- Load voice-search-guide.md only for voice optimization
- Load social-preview-guide.md only for social media work

**Benefits**:
- 90% cost reduction after first request
- 85% latency reduction (warm cache)
- Efficient token budget management
- Fast execution for simple tasks

### Workflow Architecture

```
User Request
    ↓
Decision Tree (Mode Selection)
    ├─ Quick Audit Mode (analyze, recommend)
    ├─ Standard Mode (analyze, extract, recommend, validate)
    └─ Deep Mode (analyze, extract, recommend, validate, generate assets)
    ↓
Phase 1: Clarify
    - Understand user request
    - Identify file type (HTML, Markdown, React/JSX)
    - Determine optimization goals
    ↓
Phase 2: Plan
    - Select appropriate scripts
    - Load relevant reference guides
    - Outline report structure
    ↓
Phase 3: Act
    - Execute analyze_content.py
    - Run keyword_analyzer.py
    - Generate schema with schema_generator.py
    - Validate with metadata_validator.py
    ↓
Phase 4: Verify
    - Check output completeness
    - Validate schema JSON-LD
    - Calculate SEO score
    - Generate issue list
    ↓
Phase 5: Report
    - Generate Markdown report
    - Create HTML dashboard
    - Export JSON data
    - Optionally generate PDF (via generating-pdf skill)
    - Open report in browser
```

### Integration with Existing Skills

**minimalist-website-mvp**:
- Invoke seo-geo-optimizer for auditing generated websites
- Leverage entity-seo-guide.md content
- Share schema-library.md reference
- Complementary, not overlapping

**generating-pdf**:
- Export audit reports to professional PDF
- Use block-based composition
- McKinsey-style formatting
- Invoked via Task tool

**deep-research**:
- Similar workflow pattern (Clarify → Plan → Act → Verify → Report)
- Similar validation gate system
- Similar progressive disclosure
- Different domain (research vs. SEO)

---

## Success Metrics

### Functional Requirements
- ✅ Can audit any file type (HTML, Markdown, React/JSX)
- ✅ Generates all schema types (FAQ, Article, HowTo, Breadcrumb, Organization, Person)
- ✅ Validates metadata completeness (meta tags, Open Graph, Twitter Cards)
- ✅ Extracts semantic keywords (primary, LSI, long-tail, question)
- ✅ Provides platform-specific recommendations (ChatGPT, Perplexity, Claude, Gemini)
- ✅ Generates multi-format reports (Markdown, HTML, PDF, JSON)
- ✅ Works offline (Python stdlib only, no external dependencies)
- ✅ Fast loading (30-50 tokens until activated)

### Performance Metrics
- **First request (cold cache)**: <15s, ~$0.05
- **Subsequent requests (warm cache)**: <5s, ~$0.005 (90% cost reduction)
- **SEO score accuracy**: >90% alignment with manual audit
- **Schema validation**: 100% valid JSON-LD output
- **Report generation**: <10s for complete audit

### Quality Metrics
- **Citation probability improvement**: Target +30-40% with recommendations
- **Voice search optimization**: 29-word answer compliance
- **Social preview quality**: All OG/Twitter tags present and valid
- **Schema completeness**: FAQ + Article minimum, HowTo for applicable content
- **Keyword coverage**: Primary + 10+ semantic + 5+ long-tail per page

---

## Long-Term Vision

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
- Competitive analysis (compare to top 10 SERP results)
- Automated monitoring (track SEO metrics over time)
- A/B testing recommendations
- Integration with analytics tools (Google Search Console, Plausible)

### Phase 4 (Months 7+): Ecosystem Integration
- Seamless workflow with minimalist-website-mvp
- Automatic PDF report generation via generating-pdf
- Export to common SEO tools (Ahrefs, SEMrush format)
- API mode for automation and CI/CD pipelines
- MCP server for persistent monitoring (if needed)

---

## Decision Log

### Why Standalone Skill (Not MCP Server)?
- ✅ Single-purpose, focused domain (SEO/GEO optimization)
- ✅ No need for persistent state or database
- ✅ File-based analysis (Read, Grep existing content)
- ✅ Self-contained scripts (Python stdlib only)
- ✅ Fast loading (30-50 tokens until activated)
- ✅ Composable with other skills

**MCP Server only if:**
- Need persistent database of SEO metrics over time
- External API integrations (Google Search Console, SEMrush)
- Real-time monitoring across multiple sites
- Shared service across multiple projects

### Why Single Skill (Not Multiple)?
- ❌ Don't split into `seo-traditional` + `seo-ai` + `seo-voice`
- ✅ **Single unified skill** with reference files for each area
- **Reason**: Context efficiency, simpler UX, natural workflow

### Why Complement (Not Extend) minimalist-website-mvp?
- ✅ Different use case: Audit existing vs. generate new
- ✅ Works with ANY content (not just Next.js/React)
- ✅ Standalone value (can be used independently)
- ✅ Follows single-responsibility principle

---

## References

### Research Sources
- **Anthropic Context Engineering Guide** - arXiv 2510.26493v1
- **Anthropic MCP Code Execution** - https://www.anthropic.com/engineering/code-execution-with-mcp
- **LLMO White Paper** - Shane H. Tepper, June 2025
- **GEO Overview** - Andreessen Horowitz (a16z)
- **AI Traffic Study** - Superprompt.com (400+ sites, 527% growth)
- **Voice Search Statistics** - Multiple sources (2025 data)
- **Platform Market Share** - Various industry reports

### Existing Skills Analyzed
- `minimalist-website-mvp` - AI-native SEO foundation
- `deep-research` - Workflow patterns, validation gates
- `generating-pdf` - Report generation, professional formatting
- `obsidian-vault-manager` - Documentation patterns
- `longevity-report` - Multi-format output, clinical design

### GitHub Examples
- `alirezarezvani/claude-skills` - 42 production-ready skills
- `BehiSecc/awesome-claude-skills` - Community curated list
- `travisvn/awesome-claude-skills` - Claude Code workflows
- `anthropics/skills` - Official patterns

---

## Next Steps (After Implementation)

1. **Documentation**
   - Write comprehensive README.md
   - Create CONTRIBUTING.md for community extensions
   - Document all scripts with docstrings
   - Add inline comments for complex logic

2. **Testing**
   - Unit tests for each script
   - Integration tests with existing skills
   - Performance benchmarks
   - Validation against real-world sites

3. **Community**
   - Share on GitHub (199-biotechnologies org)
   - Add to awesome-claude-skills lists
   - Write blog post about implementation
   - Create video tutorial

4. **Iteration**
   - Gather user feedback
   - Add requested features
   - Optimize performance
   - Expand platform support (TikTok, Instagram, etc.)

---

**Status**: ✅ Plan approved, implementation in progress
**Current Phase**: Phase 1 - Core Structure (Week 1)
**Next Milestone**: Complete skill.md with cacheable context
**Target Completion**: 4 weeks from start date
