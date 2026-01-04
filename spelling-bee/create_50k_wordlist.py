#!/usr/bin/env python3
"""
Create a 50,000 word list from Peter Norvig's frequency data.
Only includes words that are 4+ letters and alphabetic.
"""

import re

# Read the frequency list (word + tab + count)
words_with_freq = []
with open('count_1w.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            word = parts[0].lower()
            # Only include words that are:
            # - 4+ letters
            # - purely alphabetic (no numbers, apostrophes, hyphens)
            # - not all uppercase abbreviations
            if len(word) >= 4 and word.isalpha():
                try:
                    count = int(parts[1])
                    words_with_freq.append((word, count))
                except ValueError:
                    continue

# Sort by frequency (highest first)
words_with_freq.sort(key=lambda x: x[1], reverse=True)

print(f"Total valid words (4+ letters, alphabetic): {len(words_with_freq)}")

# Take top 50,000
top_50k = [word for word, _ in words_with_freq[:50000]]

print(f"Selected top {len(top_50k)} words")

# Remove duplicates and sort alphabetically
unique_words = sorted(set(top_50k))

print(f"Unique words: {len(unique_words)}")

# Save the list
with open('words_50k.txt', 'w') as f:
    for word in unique_words:
        f.write(word + '\n')

print(f"Saved to words_50k.txt")

# Show some stats
print(f"\nSample words (first 20):")
for word in unique_words[:20]:
    print(f"  {word}")

print(f"\nSample words (last 20):")
for word in unique_words[-20:]:
    print(f"  {word}")
