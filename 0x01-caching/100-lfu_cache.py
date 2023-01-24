#!/usr/bin/env python3

"""
Module 2-hypermedia_pagination
"""
import csv
import math
from typing import List

def put(self, key, item):
    if key is None or item is None:
        return None
    if key in self.cache_data:
        self.frequency[key] += 1
    else:
        self.frequency[key] = 1
    self.cache_data[key] = item
    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
        lfu = min(self.frequency, key=self.frequency.get)
        self.frequency.pop(lfu)
        self.cache_data.pop(lfu)
        print("DISCARD: " + lfu)
        
def get(self, key):
    if key is None or key not in self.cache_data:
        return None
    self.frequency[key] += 1
    return self.cache_data[key]
