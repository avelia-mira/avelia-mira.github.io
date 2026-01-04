# Quick Start Guide 🚀

## Testing Locally

Run a local server (needed to load word list):

```bash
cd spelling-bee
python -m http.server 8000
```

Then open: http://localhost:8000

## Your Files

1. **index.html** - The game (open this in browser)
2. **puzzles.json** - Edit this to curate daily puzzles
3. **words.txt** - 370k+ English words (already downloaded)
4. **README.md** - Full documentation

## Quick Edit: Adding a Puzzle

Open `puzzles.json` and add:

```json
{
  "id": 6,
  "date": "2026-01-08",
  "centerLetter": "T",
  "outerLetters": ["H", "E", "R", "A", "P", "Y"],
  "title": "Daily Puzzle #6"
}
```

**That's it!** The game will:
- Auto-calculate all valid words from the word list
- Find all pangrams automatically
- Calculate total points
- Show the puzzle on Jan 8, 2026

## Tips

- Center letter = required in every word
- Outer letters = any amount you want!
- Date format must be: YYYY-MM-DD
- **Pangrams & points auto-calculated!** No manual work needed
- Check browser console to see pangram count when puzzle loads
- Test your puzzles before publishing

Have fun! 🐝✨
