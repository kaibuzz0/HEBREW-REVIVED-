#!/usr/bin/env python3
"""
Performance Cache System
Speeds up repeated queries
"""

import json
import hashlib
import os
from functools import wraps

CACHE_DIR = '/tmp/bible_cache'

def cached(func):
    """Decorator to cache function results"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        
        # Create cache key from arguments
        key = hashlib.md5(str(args).encode()).hexdigest()
        cache_file = os.path.join(CACHE_DIR, f"{func.__name__}_{key}.json")
        
        if os.path.exists(cache_file):
            with open(cache_file) as f:
                return json.load(f)
        
        result = func(*args, **kwargs)
        
        with open(cache_file, 'w') as f:
            json.dump(result, f)
        
        return result
    return wrapper
