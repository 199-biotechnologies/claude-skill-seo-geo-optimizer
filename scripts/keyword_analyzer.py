#!/usr/bin/env python3
"""
SEO/GEO Keyword Analyzer

Extracts and analyzes keywords from content files for SEO/GEO optimization.
Identifies primary, semantic, LSI, long-tail, and question-based keywords.

Usage:
    python keyword_analyzer.py <file_path>
    python keyword_analyzer.py --help

Requirements:
    Python 3.7+ (stdlib only)

Output:
    JSON with categorized keywords and density analysis
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Set
from collections import Counter

# Import analyze_content functions
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
from analyze_content import analyze_file, extract_html_content, extract_markdown_frontmatter


# Common stop words (English)
STOP_WORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are',
    'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but',
    'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for',
    'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself',
    'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just',
    'me', 'might', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on',
    'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 's', 'same',
    'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them',
    'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too',
    'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while',
    'who', 'whom', 'why', 'will', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves'
}


def extract_text_content(file_path: str) -> Dict:
    """Extract clean text content from file"""

    path = Path(file_path)
    suffix = path.suffix.lower()

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    text = ""
    title = ""
    headings = []

    if suffix in ['.html', '.htm']:
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()

        # Extract all headings
        for level in range(1, 7):
            matches = re.findall(rf'<h{level}[^>]*>(.*?)</h{level}>', content, re.IGNORECASE | re.DOTALL)
            headings.extend([re.sub(r'<[^>]+>', '', h).strip() for h in matches])

        # Extract clean text
        html_analysis = extract_html_content(content)
        text = html_analysis['full_text']

    elif suffix in ['.md', '.mdx', '.markdown']:
        # Extract frontmatter
        frontmatter, body = extract_markdown_frontmatter(content)
        title = frontmatter.get('title', '')

        # Extract headings
        headings = re.findall(r'^#{1,6}\s+(.+)$', body, re.MULTILINE)

        # Clean text
        text = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
        text = re.sub(r'`[^`]+`', '', text)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        text = re.sub(r'[#*_`]', '', text)

    elif suffix in ['.jsx', '.tsx', '.js', '.ts']:
        # Extract from JSX/TSX
        title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
        if title_match:
            title = title_match.group(1)

        # Extract headings from JSX
        for level in range(1, 7):
            matches = re.findall(rf'<h{level}[^>]*>([^<]+)</h{level}>', content)
            headings.extend(matches)

        # Extract text
        text = re.sub(r'import\s+.*?from\s+["\'].*?["\'];?', '', content)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\{[^\}]+\}', ' ', text)

    # Clean text
    text = re.sub(r'\s+', ' ', text).strip()

    return {
        'title': title,
        'headings': headings,
        'text': text,
        'word_count': len(text.split())
    }


def tokenize_text(text: str) -> List[str]:
    """Tokenize text into words"""
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation except hyphens in words
    text = re.sub(r'[^\w\s-]', ' ', text)

    # Split into words
    words = text.split()

    # Filter out stop words and very short words
    words = [w for w in words if w not in STOP_WORDS and len(w) > 2]

    return words


def extract_ngrams(words: List[str], n: int) -> List[str]:
    """Extract n-grams from words"""
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams


def extract_primary_keywords(content: Dict, top_n: int = 10) -> List[Dict]:
    """
    Extract primary keywords from title, H1, H2, and first 100 words
    These are the main topic keywords
    """
    # Combine high-priority text
    priority_text = ' '.join([
        content['title'],
        ' '.join(content['headings'][:3]),  # First 3 headings
        ' '.join(content['text'].split()[:100])  # First 100 words
    ])

    words = tokenize_text(priority_text)

    # Count single words
    word_counts = Counter(words)

    # Count 2-grams
    bigrams = extract_ngrams(words, 2)
    bigram_counts = Counter(bigrams)

    # Combine and rank
    keywords = []

    # Top single words
    for word, count in word_counts.most_common(top_n):
        keywords.append({
            'keyword': word,
            'type': '1-gram',
            'frequency': count,
            'score': count
        })

    # Top 2-grams
    for bigram, count in bigram_counts.most_common(top_n // 2):
        keywords.append({
            'keyword': bigram,
            'type': '2-gram',
            'frequency': count,
            'score': count * 1.5  # Boost multi-word keywords
        })

    # Sort by score
    keywords.sort(key=lambda x: x['score'], reverse=True)

    return keywords[:top_n]


def extract_semantic_keywords(content: Dict, primary: List[Dict], top_n: int = 15) -> List[Dict]:
    """
    Extract semantic keywords (related terms)
    Found in H2/H3 headings and body content
    """
    # Extract from H2/H3 and body
    semantic_text = ' '.join([
        ' '.join(content['headings'][1:]),  # All headings except H1
        content['text']
    ])

    words = tokenize_text(semantic_text)

    # Remove primary keywords to avoid duplication
    primary_words = set()
    for kw in primary:
        primary_words.update(kw['keyword'].split())

    words = [w for w in words if w not in primary_words]

    # Count words
    word_counts = Counter(words)

    # Count 2-grams
    bigrams = extract_ngrams(words, 2)
    bigram_counts = Counter(bigrams)

    keywords = []

    # Top single words
    for word, count in word_counts.most_common(top_n):
        keywords.append({
            'keyword': word,
            'type': '1-gram',
            'frequency': count,
            'context': 'semantic'
        })

    # Top 2-grams
    for bigram, count in bigram_counts.most_common(top_n // 2):
        keywords.append({
            'keyword': bigram,
            'type': '2-gram',
            'frequency': count,
            'context': 'semantic'
        })

    return keywords[:top_n]


def extract_longtail_keywords(content: Dict, top_n: int = 10) -> List[Dict]:
    """
    Extract long-tail keywords (3-8 word phrases)
    Found in FAQ sections and H3 headings
    """
    words = tokenize_text(content['text'])

    longtail = []

    # Extract 3-grams
    trigrams = extract_ngrams(words, 3)
    trigram_counts = Counter(trigrams)

    for trigram, count in trigram_counts.most_common(top_n):
        if count >= 2:  # Must appear at least twice
            longtail.append({
                'keyword': trigram,
                'type': '3-gram',
                'frequency': count,
                'length': 'long-tail'
            })

    # Extract 4-grams
    fourgrams = extract_ngrams(words, 4)
    fourgram_counts = Counter(fourgrams)

    for fourgram, count in fourgram_counts.most_common(top_n // 2):
        if count >= 2:
            longtail.append({
                'keyword': fourgram,
                'type': '4-gram',
                'frequency': count,
                'length': 'long-tail'
            })

    return longtail[:top_n]


def extract_question_keywords(content: Dict) -> List[Dict]:
    """
    Extract question-based keywords
    Critical for voice search and FAQ schema
    """
    questions = []

    # Question patterns
    question_words = ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'whose', 'can', 'does', 'is', 'are']

    # Extract from text
    sentences = re.split(r'[.!?]', content['text'])

    for sentence in sentences:
        sentence = sentence.strip()
        first_word = sentence.lower().split()[0] if sentence else ''

        if first_word in question_words or sentence.endswith('?'):
            if len(sentence.split()) >= 3:  # Minimum 3 words
                questions.append({
                    'question': sentence,
                    'type': 'natural',
                    'word_count': len(sentence.split()),
                    'voice_search_optimized': len(sentence.split()) <= 10
                })

    # Extract from headings
    for heading in content['headings']:
        first_word = heading.lower().split()[0] if heading else ''
        if first_word in question_words or '?' in heading:
            questions.append({
                'question': heading,
                'type': 'heading',
                'word_count': len(heading.split()),
                'voice_search_optimized': len(heading.split()) <= 10
            })

    return questions


def calculate_keyword_density(content: Dict, keywords: List[Dict]) -> List[Dict]:
    """Calculate keyword density percentage"""
    total_words = content['word_count']

    for keyword in keywords:
        frequency = keyword.get('frequency', 0)
        word_count = len(keyword['keyword'].split())
        # Density = (keyword frequency * word count) / total words * 100
        density = (frequency * word_count) / total_words * 100 if total_words > 0 else 0
        keyword['density'] = round(density, 2)

    return keywords


def analyze_keywords(file_path: str) -> Dict:
    """Main keyword analysis function"""

    # Extract content
    content = extract_text_content(file_path)

    if content['word_count'] == 0:
        return {
            'error': 'No text content found in file',
            'file': file_path
        }

    # Extract different keyword types
    primary = extract_primary_keywords(content, top_n=10)
    semantic = extract_semantic_keywords(content, primary, top_n=15)
    longtail = extract_longtail_keywords(content, top_n=10)
    questions = extract_question_keywords(content)

    # Calculate densities
    primary = calculate_keyword_density(content, primary)
    semantic = calculate_keyword_density(content, semantic)
    longtail = calculate_keyword_density(content, longtail)

    # Analysis summary
    summary = {
        'total_words': content['word_count'],
        'unique_words': len(set(tokenize_text(content['text']))),
        'primary_keywords': len(primary),
        'semantic_keywords': len(semantic),
        'longtail_keywords': len(longtail),
        'question_keywords': len(questions),
        'voice_search_questions': len([q for q in questions if q.get('voice_search_optimized')])
    }

    # Recommendations
    recommendations = []

    if len(questions) == 0:
        recommendations.append("Add question-based content for voice search optimization")
    elif len(questions) < 3:
        recommendations.append(f"Add more FAQ content ({len(questions)} questions found, 5+ recommended)")
    else:
        recommendations.append(f"✅ Good FAQ coverage ({len(questions)} questions found)")

    if len(longtail) < 5:
        recommendations.append("Add more long-tail keyword phrases (3-5 word combinations)")

    # Check keyword density (should be 1-3% for primary keywords)
    if primary:
        top_keyword = primary[0]
        if top_keyword['density'] > 3:
            recommendations.append(f"Primary keyword '{top_keyword['keyword']}' density too high ({top_keyword['density']}%), risk of keyword stuffing")
        elif top_keyword['density'] < 0.5:
            recommendations.append(f"Primary keyword '{top_keyword['keyword']}' density too low ({top_keyword['density']}%), increase usage")

    return {
        'file': file_path,
        'summary': summary,
        'primary_keywords': primary,
        'semantic_keywords': semantic,
        'longtail_keywords': longtail,
        'question_keywords': questions,
        'recommendations': recommendations
    }


def main():
    """Main entry point"""

    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h']:
        print(__doc__)
        print("\nExamples:")
        print("  python keyword_analyzer.py ~/project/about.html")
        print("  python keyword_analyzer.py ~/blog/post.md")
        sys.exit(0 if len(sys.argv) >= 2 else 1)

    file_path = sys.argv[1]

    try:
        analysis = analyze_keywords(file_path)

        # Pretty print JSON
        print(json.dumps(analysis, indent=2, ensure_ascii=False))

        # Exit code
        if 'error' in analysis:
            sys.exit(1)
        else:
            sys.exit(0)

    except Exception as e:
        print(json.dumps({
            'error': str(e),
            'file': file_path
        }, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
