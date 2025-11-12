#!/usr/bin/env python3
"""Voice Search Optimizer - Generate featured snippet content and Speakable schema"""
import json, sys, re
from datetime import datetime

def generate_featured_snippet(text: str, max_words: int = 40) -> str:
    """Extract 30-40 word summary for featured snippets"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    words = []
    for s in sentences:
        words.extend(s.split())
        if len(words) >= 30:
            break
    return ' '.join(words[:max_words])

def add_speakable_schema(html: str, sections: list) -> str:
    """Add Speakable schema for 20-30 second segments"""
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": sections or [".tldr", "h2", "h3"]
        }
    }
    return html.replace('</head>', f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>\n</head>')

def main():
    if len(sys.argv) < 2:
        print("Usage: python voice_optimizer.py <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        html = f.read()
    optimized = add_speakable_schema(html, [".tldr", "h2"])
    output = sys.argv[1].replace('.html', '-voice.html')
    with open(output, 'w') as f:
        f.write(optimized)
    print(f"✓ Voice optimization complete: {output}")

if __name__ == '__main__':
    main()
