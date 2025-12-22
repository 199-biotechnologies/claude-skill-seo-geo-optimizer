# Code Quality Improvement Plan

**Created:** 2025-12-22
**Status:** In Progress

## Overview

Analysis of 13 Python scripts (~4,500 lines) identified the following improvements.

## Phase 1: Critical Fixes (Error Handling)

### Files to Fix:
1. `freshness_monitor.py:19` - Replace `except: pass` with specific exception
2. `content_optimizer.py:127` - Replace bare `except:` with specific exception
3. `auto_implementer.py:127-128` - Replace `except: pass` with warning log

## Phase 2: Create Shared Utilities

Create `scripts/shared/` directory with:

### shared/__init__.py
```python
from .schema_utils import has_schema_type, get_schema_by_type
from .text_utils import count_words, tokenize, extract_sentences
from .config import LIMITS, SCORES
```

### shared/schema_utils.py
- `has_schema_type(schemas, type)` - Check if schema type exists
- `get_schema_by_type(schemas, type)` - Get schema by type
- `validate_schema(schema)` - Validate JSON-LD structure

### shared/text_utils.py
- `count_words(text)` - Count words in text
- `tokenize(text)` - Tokenize text into words
- `extract_sentences(text)` - Split into sentences

### shared/config.py
- `LIMITS` - Character/word limits for meta tags, content
- `SCORES` - Scoring thresholds and weights
- `PATTERNS` - Pre-compiled regex patterns

## Phase 3: Enhance Minimal Scripts

### voice_optimizer.py (41 → ~150 lines)
- Add sentence length validation (20-30 second segments)
- Add question-answer pattern detection
- Add error handling and JSON output
- Validate speakable content quality

### freshness_monitor.py (45 → ~120 lines)
- Check datePublished vs dateModified gap
- Detect stale statistics patterns ("2020 study")
- Check for outdated technology references
- Add content decay scoring algorithm

### citation_enhancer.py (45 → ~100 lines)
- Identify claim statements without evidence
- Suggest citation placement locations
- Check for unsupported superlatives
- Add credibility gap analysis

## Phase 4: Extract Constants

Move all magic numbers to `shared/config.py`:

```python
LIMITS = {
    'meta_title': {'min': 30, 'optimal_min': 50, 'optimal_max': 60, 'max': 70},
    'meta_description': {'min': 100, 'optimal_min': 150, 'optimal_max': 160, 'max': 170},
    'tldr_words': {'min': 40, 'max': 60},
    'paragraph_words': {'min': 60, 'max': 100},
    'content_min_words': 300,
    'content_optimal_words': 800,
}

SCORES = {
    'thresholds': {'excellent': 90, 'good': 80, 'fair': 70, 'poor': 60},
    'weights': {
        'meta_title': 0.15,
        'meta_description': 0.15,
        'open_graph': 0.20,
        'twitter_cards': 0.15,
        'schema': 0.20,
        'content_structure': 0.15
    }
}
```

## Phase 5: Pre-compile Regex Patterns

Move to `shared/config.py`:

```python
import re

PATTERNS = {
    'credentials': re.compile(r'\b(MD|PhD|Ph\.D\.|M\.D\.|MBA|MSc|MPH|DDS|JD|RN)\b'),
    'tldr': re.compile(r'TL;?DR:?\s*', re.IGNORECASE),
    'faq_heading': re.compile(r'<h[1-3][^>]*>.*?FAQ.*?</h[1-3]>', re.IGNORECASE),
    'date_iso': re.compile(r'\d{4}-\d{2}-\d{2}'),
    'statistics': re.compile(r'(\d+(?:,\d{3})*(?:\.\d+)?)\s*(%|percent|years?|months?)'),
}
```

## Phase 6: Standardize CLI Output

Add to all CLI scripts:
- `--format json|text|html` flag
- `--verbose` flag for progress messages
- `--quiet` flag for minimal output
- Consistent exit codes (0=success, 1=error, 2=warnings)

## Files Changed Summary

| File | Changes |
|------|---------|
| `scripts/shared/__init__.py` | NEW |
| `scripts/shared/schema_utils.py` | NEW |
| `scripts/shared/text_utils.py` | NEW |
| `scripts/shared/config.py` | NEW |
| `scripts/freshness_monitor.py` | Enhanced |
| `scripts/voice_optimizer.py` | Enhanced |
| `scripts/citation_enhancer.py` | Enhanced |
| `scripts/content_optimizer.py` | Fix + refactor |
| `scripts/auto_implementer.py` | Fix + refactor |
| `scripts/analyze_content.py` | Use shared utils |
| `scripts/metadata_validator.py` | Use shared utils |
| `scripts/keyword_analyzer.py` | Use shared utils |

## Testing

After each phase:
1. Run existing tests if any
2. Test each script with sample HTML files
3. Verify JSON output format consistency
4. Check exit codes
