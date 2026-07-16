
import difflib

def fuzzy_search(query, texts, cutoff=0.6):
    """Fuzzy text search"""
    matches = []
    for text in texts:
        ratio = difflib.SequenceMatcher(None, query.lower(), text.lower()).ratio()
        if ratio >= cutoff:
            matches.append((text, ratio))
    return sorted(matches, key=lambda x: x[1], reverse=True)
