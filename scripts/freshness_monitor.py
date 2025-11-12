#!/usr/bin/env python3
"""Freshness Monitor - Track content age and recommend updates"""
import re, sys, json
from datetime import datetime, timedelta

def analyze_freshness(html: str) -> dict:
    """Analyze content freshness indicators"""
    issues = []
    
    # Check dateModified
    date_match = re.search(r'"dateModified":\s*"([^"]+)"', html)
    if date_match:
        date_str = date_match.group(1)
        try:
            modified = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            days_old = (datetime.now() - modified.replace(tzinfo=None)).days
            if days_old > 30:
                issues.append(f"Content is {days_old} days old (>30 days = 3.2x fewer citations)")
        except:
            pass
    
    # Check for year mentions
    current_year = datetime.now().year
    old_years = [str(y) for y in range(2020, current_year)]
    for year in old_years:
        if year in html:
            issues.append(f"Contains reference to {year} (consider updating)")
    
    return {
        "freshness_score": 100 - min(len(issues) * 20, 100),
        "issues": issues,
        "recommendation": "Update every 2-3 days for Perplexity" if issues else "Content is fresh"
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python freshness_monitor.py <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        html = f.read()
    result = analyze_freshness(html)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
