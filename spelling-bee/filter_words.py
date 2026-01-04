#!/usr/bin/env python3
"""
Filter words.txt to only include common English words that are 4+ letters long.
Uses Google's 10000 most common words as the reference.
"""

# Read the common words list
with open('google-10000-english.txt', 'r') as f:
    common_words = set(word.strip().lower() for word in f if len(word.strip()) >= 4)

print(f"Loaded {len(common_words)} common words (4+ letters)")

# Read the current word list
with open('words.txt', 'r') as f:
    all_words = [word.strip().lower() for word in f]

print(f"Original word list: {len(all_words)} words")

# Filter to only include common words that are 4+ letters
filtered_words = sorted(set(word for word in all_words if word in common_words and len(word) >= 4))

print(f"Filtered word list: {len(filtered_words)} words")

# Write the filtered list
with open('words_filtered.txt', 'w') as f:
    for word in filtered_words:
        f.write(word + '\n')

print(f"Saved filtered words to words_filtered.txt")

# Backup original
import shutil
shutil.copy('words.txt', 'words_backup.txt')
print("Backed up original to words_backup.txt")

# Replace original with filtered
shutil.copy('words_filtered.txt', 'words.txt')
print("Replaced words.txt with filtered version")
