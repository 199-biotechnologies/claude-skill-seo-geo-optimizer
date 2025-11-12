#!/usr/bin/env python3
"""
Platform Optimizer - Phase 2
Apply platform-specific optimizations based on 2025 research

Platforms:
- ChatGPT: Depth, authority, credentials (40-60% of LLM traffic)
- Perplexity: Freshness, inline citations (update every 2-3 days)
- Claude: Primary sources, accuracy (91.2% attribution accuracy)
- Gemini: Community validation, Google ecosystem

Research: ChatGPT favors Wikipedia (1.3M citations), Perplexity = 3.2x citations for fresh content
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Optional
import sys

def optimize_for_chatgpt(html_content: str, config: Dict) -> tuple[str, List[str]]:
    """
    ChatGPT optimization: Authority, credentials, depth
    
    Preferences:
    - 1500-2500 words
    - Author credentials prominent (MD, PhD = +40% citation boost)
    - Citations to primary sources (PubMed, arXiv)
    - Answer-first, listicles, how-to guides (+35% citations)
    - FAQPage and Article schema
    
    Args:
        html_content: HTML content
        config: Platform configuration
        
    Returns:
        (optimized_html, changes_list)
    """
    changes = []
    optimized = html_content
    
    # 1. Add author credentials (schema only, or subtle byline)
    if config.get('author'):
        author_name = config['author']['name']
        credentials = config['author'].get('credentials', '')

        # Add subtle author byline (no label, natural)
        if '<h1>' in optimized:
            # Add subtle "By Author Name" after H1
            byline = f'<p class="author"><em>By {author_name}'
            if credentials:
                byline += f', {credentials}'
            byline += f'</em></p>\n\n'

            if 'class="author"' not in optimized:
                optimized = optimized.replace('</h1>', f'</h1>\n\n{byline}', 1)
                changes.append(f"Added author: {author_name} {credentials}")
    
    # 2. Update dateModified in schema (no visible date banner)
    today_iso = datetime.now().isoformat()
    today_display = datetime.now().strftime('%B %d, %Y')

    # Update schema if present, otherwise will be added later
    if '"dateModified"' in optimized:
        optimized = re.sub(
            r'"dateModified":\s*"[^"]+"',
            f'"dateModified": "{today_iso}"',
            optimized
        )
        changes.append(f"Updated dateModified to {today_display}")
    
    # 3. Add Article schema if not present
    if 'schema.org/Article' not in optimized:
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": config.get('title', 'Article'),
            "author": {
                "@type": "Person",
                "name": config.get('author', {}).get('name', ''),
                "honorificSuffix": config.get('author', {}).get('credentials', '')
            },
            "datePublished": datetime.now().isoformat(),
            "dateModified": datetime.now().isoformat()
        }
        
        schema_tag = f'\n<script type="application/ld+json">\n{json.dumps(article_schema, indent=2)}\n</script>\n'
        
        if '</head>' in optimized:
            optimized = optimized.replace('</head>', f'{schema_tag}</head>')
            changes.append("Added Article schema with author credentials")
    
    # 4. Add "References" section if citations exist
    if 'References' not in optimized and config.get('add_references'):
        references = '\n<h2>References</h2>\n<ol class="references">\n'
        references += '  <li>Add primary source citations (PubMed, arXiv, academic journals)</li>\n'
        references += '  <li>Include publisher and year for each citation</li>\n'
        references += '</ol>\n\n'
        
        optimized = optimized.replace('</body>', f'{references}</body>')
        changes.append("Added References section placeholder")
    
    return optimized, changes

def optimize_for_perplexity(html_content: str, config: Dict) -> tuple[str, List[str]]:
    """
    Perplexity optimization: Freshness, inline citations, structure
    
    Critical: Freshness (3.2x citations for content updated within 30 days)
    - Update every 2-3 days (aggressive) or minimum 90 days
    - H2→H3→bullets (40% more citations)
    - Inline citations with [1], [2] format
    - dateModified to current date
    
    Args:
        html_content: HTML content
        config: Platform configuration
        
    Returns:
        (optimized_html, changes_list)
    """
    changes = []
    optimized = html_content
    
    # 1. Update dateModified to TODAY (critical for Perplexity)
    today_iso = datetime.now().isoformat()
    today_display = datetime.now().strftime('%B %d, %Y')

    # Update in schema (metadata only, no visible banner)
    if '"dateModified"' in optimized:
        optimized = re.sub(
            r'"dateModified":\s*"[^"]+"',
            f'"dateModified": "{today_iso}"',
            optimized
        )
        changes.append(f"Updated dateModified to {today_display} (schema)")

    # 2. Remove any existing prominent banners (clean up)
    if '<div class="last-updated-prominent">' in optimized:
        optimized = re.sub(
            r'<div class="last-updated-prominent"[^>]*>.*?</div>\s*',
            '',
            optimized,
            flags=re.DOTALL
        )
    
    # 3. Note citation opportunities (don't add placeholders to HTML)
    if config.get('add_inline_citations'):
        # Count paragraphs with statistics that could use citations
        stat_paragraphs = len(re.findall(r'<p>[^<]*\d+[^<]*</p>', optimized))
        if stat_paragraphs > 0:
            changes.append(f"Found {stat_paragraphs} paragraphs that could use inline citations [1], [2]")
    
    # 4. Ensure H2→H3→bullet structure hint
    if '<h2>' in optimized and '<h3>' not in optimized:
        changes.append("Note: Consider adding H3 subheadings under H2s for better structure")
    
    return optimized, changes

def optimize_for_claude(html_content: str, config: Dict) -> tuple[str, List[str]]:
    """
    Claude optimization: Primary sources, transparent methodology
    
    Preferences:
    - 5-8 primary source citations (publisher + year)
    - Transparent methodology section
    - Acknowledge limitations
    - Inline citations with clickable links
    - 91.2% attribution accuracy (high standards)
    
    Args:
        html_content: HTML content
        config: Platform configuration
        
    Returns:
        (optimized_html, changes_list)
    """
    changes = []
    optimized = html_content
    
    # 1. Add "Methodology" section
    if 'Methodology' not in optimized and config.get('add_methodology'):
        methodology = '\n<h2>Methodology</h2>\n'
        methodology += '<p>This content is based on [describe sources and approach]. '
        methodology += 'Primary sources include peer-reviewed research, clinical guidelines, '
        methodology += 'and expert consensus statements.</p>\n\n'
        
        # Insert before references or before closing body
        if '<h2>References</h2>' in optimized:
            optimized = optimized.replace('<h2>References</h2>', f'{methodology}<h2>References</h2>')
        else:
            optimized = optimized.replace('</body>', f'{methodology}</body>')
        changes.append("Added Methodology section")
    
    # 2. Add "Limitations" section
    if 'Limitations' not in optimized and config.get('add_limitations'):
        limitations = '\n<h2>Limitations</h2>\n'
        limitations += '<p>This information is current as of [date]. Readers should consult '
        limitations += 'primary sources and healthcare professionals for specific guidance. '
        limitations += 'Individual circumstances may vary.</p>\n\n'
        
        optimized = optimized.replace('</body>', f'{limitations}</body>')
        changes.append("Added Limitations section")
    
    # 3. Add "Data Sources" section
    if 'Data Sources' not in optimized and config.get('add_data_sources'):
        sources = '\n<h2>Data Sources</h2>\n'
        sources += '<ul>\n'
        sources += '  <li>Primary research: [Specify journals, databases]</li>\n'
        sources += '  <li>Clinical guidelines: [Specify organizations]</li>\n'
        sources += '  <li>Expert consensus: [Specify authorities]</li>\n'
        sources += '</ul>\n\n'
        
        optimized = optimized.replace('</body>', f'{sources}</body>')
        changes.append("Added Data Sources section")
    
    # 4. Format citations as clickable links
    if config.get('make_citations_clickable'):
        # Convert [1], [2] style to clickable if references exist
        changes.append("Note: Ensure citations are clickable links to references")
    
    return optimized, changes

def optimize_for_gemini(html_content: str, config: Dict) -> tuple[str, List[str]]:
    """
    Gemini optimization: Community validation, Google ecosystem
    
    Preferences:
    - User reviews/testimonials
    - Google Business Profile integration
    - Local citations (NAP consistency)
    - Community validation signals
    - Traditional authority signals (awards, press)
    
    Args:
        html_content: HTML content
        config: Platform configuration
        
    Returns:
        (optimized_html, changes_list)
    """
    changes = []
    optimized = html_content
    
    # 1. Add testimonials section if provided
    if config.get('testimonials') and 'Testimonials' not in optimized:
        testimonials = '\n<h2>What Our Clients Say</h2>\n'
        for t in config['testimonials'][:3]:  # Max 3
            testimonials += f'<blockquote>\n'
            testimonials += f'  <p>"{t.get("text", "")}"</p>\n'
            testimonials += f'  <footer>— {t.get("name", "Client")}</footer>\n'
            testimonials += f'</blockquote>\n\n'
        
        # Insert before contact section or before closing body
        if '<h2>Contact</h2>' in optimized:
            optimized = optimized.replace('<h2>Contact</h2>', f'{testimonials}<h2>Contact</h2>')
        else:
            optimized = optimized.replace('</body>', f'{testimonials}</body>')
        changes.append(f"Added testimonials section ({len(config['testimonials'])} reviews)")
    
    # 2. Ensure NAP (Name, Address, Phone) consistency
    if config.get('business_info'):
        # Add Organization schema for GMB
        org_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": config['business_info'].get('name', ''),
            "address": {
                "@type": "PostalAddress",
                "streetAddress": config['business_info'].get('address', {}).get('street', ''),
                "addressLocality": config['business_info'].get('address', {}).get('city', ''),
                "addressRegion": config['business_info'].get('address', {}).get('state', ''),
                "postalCode": config['business_info'].get('address', {}).get('zip', '')
            },
            "telephone": config['business_info'].get('phone', '')
        }
        
        schema_tag = f'\n<script type="application/ld+json">\n{json.dumps(org_schema, indent=2)}\n</script>\n'
        
        if '</head>' in optimized and 'LocalBusiness' not in optimized:
            optimized = optimized.replace('</head>', f'{schema_tag}</head>')
            changes.append("Added LocalBusiness schema for Google Business Profile")
    
    # 3. Add awards/recognition if provided
    if config.get('awards') and 'Awards' not in optimized:
        awards = '\n<h2>Awards & Recognition</h2>\n<ul>\n'
        for award in config['awards'][:5]:
            awards += f'  <li>{award}</li>\n'
        awards += '</ul>\n\n'
        
        optimized = optimized.replace('</body>', f'{awards}</body>')
        changes.append(f"Added Awards & Recognition ({len(config['awards'])} awards)")
    
    return optimized, changes

def optimize_multi_platform(html_content: str, platforms: List[str], config: Dict) -> tuple[str, List[str]]:
    """
    Apply optimizations for multiple platforms with conflict resolution
    
    Args:
        html_content: HTML content
        platforms: List of platforms ['chatgpt', 'perplexity', 'claude', 'gemini']
        config: Configuration
        
    Returns:
        (optimized_html, combined_changes_list)
    """
    optimized = html_content
    all_changes = []
    
    # Apply optimizations in priority order
    platform_funcs = {
        'chatgpt': optimize_for_chatgpt,
        'perplexity': optimize_for_perplexity,
        'claude': optimize_for_claude,
        'gemini': optimize_for_gemini
    }
    
    for platform in platforms:
        if platform in platform_funcs:
            optimized, changes = platform_funcs[platform](optimized, config)
            all_changes.extend([f"[{platform.upper()}] {c}" for c in changes])
    
    return optimized, all_changes

def main():
    """CLI interface"""
    if len(sys.argv) < 3:
        print("Usage: python platform_optimizer.py <file_path> <platform> [output_path]")
        print("\nPlatforms:")
        print("  chatgpt    - Authority, credentials, depth")
        print("  perplexity - Freshness, inline citations (3.2x citations if fresh)")
        print("  claude     - Primary sources, methodology")
        print("  gemini     - Community validation, Google ecosystem")
        print("  multi      - Optimize for all platforms")
        print("\nExample:")
        print("  python platform_optimizer.py page.html perplexity")
        sys.exit(1)
    
    file_path = sys.argv[1]
    platform = sys.argv[2].lower()
    output_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Basic config (user can customize)
    config = {
        'author': {
            'name': 'Expert Author',
            'credentials': 'PhD'
        },
        'title': 'Article Title',
        'add_references': True,
        'add_methodology': True,
        'add_limitations': True,
        'add_data_sources': True,
        'add_inline_citations': True,
        'make_citations_clickable': True
    }
    
    print(f"Optimizing for: {platform.upper()}")
    print("=" * 60)
    
    # Apply optimization
    if platform == 'multi':
        optimized, changes = optimize_multi_platform(
            html_content,
            ['chatgpt', 'perplexity', 'claude', 'gemini'],
            config
        )
    elif platform == 'chatgpt':
        optimized, changes = optimize_for_chatgpt(html_content, config)
    elif platform == 'perplexity':
        optimized, changes = optimize_for_perplexity(html_content, config)
    elif platform == 'claude':
        optimized, changes = optimize_for_claude(html_content, config)
    elif platform == 'gemini':
        optimized, changes = optimize_for_gemini(html_content, config)
    else:
        print(f"Unknown platform: {platform}")
        sys.exit(1)
    
    # Determine output path
    if output_path is None:
        base = file_path.rsplit('.', 1)[0]
        output_path = f"{base}-{platform}.html"
    
    # Write optimized file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(optimized)
    
    print(f"✓ Optimization complete")
    print(f"  Output: {output_path}")
    print(f"\nChanges applied ({len(changes)}):")
    for change in changes:
        print(f"  - {change}")

if __name__ == '__main__':
    main()
