# 🐝 Cute Spelling Bee Game

A cute, customizable spelling bee game with daily puzzles and word validation!

## Features

✨ **Daily Puzzles** - Curated puzzles via JSON configuration
🎨 **Custom Mode** - Create your own puzzles with any number of letters
📖 **Word Validation** - Uses a comprehensive English word list
⭐ **Pangram Detection** - Special highlighting for words using all letters
🌸 **Cute Design** - Pastel colors, fun animations, and playful UI
⌨️ **Keyboard Support** - Type letters or click hexagons

## Files

- `index.html` - Main game file
- `puzzles.json` - Daily puzzle configuration
- `words.txt` - English word list (370k+ words)

## How to Curate Daily Puzzles

Edit `puzzles.json` to add your own puzzles:

```json
{
  "puzzles": [
    {
      "id": 1,
      "date": "2026-01-03",
      "centerLetter": "A",
      "outerLetters": ["P", "D", "E", "H", "I", "N"],
      "title": "Daily Puzzle #1"
    }
  ]
}
```

### Puzzle Fields:

- **id**: Unique identifier for the puzzle
- **date**: Date in YYYY-MM-DD format (game shows puzzle for this date)
- **centerLetter**: The required letter (must be in all words)
- **outerLetters**: Array of additional letters (any amount!)
- **title**: Display title for the puzzle

**Note:** Pangrams and total points are auto-calculated from the word list! No need to include them.

## Game Rules

1. Words must be at least 4 letters long
2. Words must include the center letter (shown in pink)
3. Words can only use the available letters
4. Letters can be used multiple times
5. Pangrams (using all letters) get special recognition ⭐

## Modes

### 📅 Daily Puzzle
- Click "Today's Puzzle" on the home screen
- Loads the puzzle for today's date from `puzzles.json`
- If no puzzle for today, shows the first puzzle
- Validates words against the word list
- Tracks pangrams

### 🎨 Custom Game
- Click "Custom Game" on the home screen
- Enter your own center letter and outer letters
- Accepts any number of letters (minimum 3 total)
- Validates words against the word list
- No pangram tracking (since puzzles are random)

## Keyboard Shortcuts

- **Type letters** - Add to current word
- **Enter** - Submit word
- **Backspace** - Delete last letter
- **Escape** - Clear current word

## Tips for Curating Puzzles

1. **Pick a good center letter** - Vowels or common consonants work well
2. **Test your puzzle** - The game auto-calculates valid words and pangrams from the word list
3. **Balance difficulty** - Mix common and uncommon letters
4. **Check the console** - When loading a puzzle, check browser console to see pangram count
5. **Plan ahead** - Set dates in advance for daily releases

## Scoring System

Points are calculated automatically:
- **4-letter words**: 1 point
- **5+ letter words**: Points equal to word length
- **Pangrams**: Word length + 7 bonus points

Example: "THERAPY" (7 letters, pangram) = 7 + 7 = 14 points

## Word List

The game uses the `words_alpha.txt` file containing 370,000+ English words. Words are:
- Filtered to 4+ letters minimum
- Converted to lowercase for matching
- Validated on every submission

## Running Locally

Simply open `index.html` in a web browser! No server needed for basic functionality.

**Note:** If you get CORS errors loading `words.txt` or `puzzles.json`, you'll need to run a local server:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (with http-server)
npx http-server
```

Then visit `http://localhost:8000`

## Customization Ideas

- Adjust scoring based on word length
- Add timer challenges
- Track high scores with localStorage
- Add hints system
- Create themed puzzle collections
- Add difficulty ratings

## Credits

- Word list from [dwyl/english-words](https://github.com/dwyl/english-words)
- Inspired by the NYT Spelling Bee

Enjoy making words! 🐝✨
