# piano-sheet
A personal collection of piano sheet music, including song titles and original sources.

## Folder Structure

```
📁 popular/      - Popular sheet music collection
📁 night-piano/  - Shi Jin's Night Piano series
📄 SOURCES.md    - Centralized source tracking for all sheet music
```

## File Naming Convention

### Popular Sheets (`popular/`)

**Practiced sheets:**
- Format: `[Emotion-Difficulty]~Artist - Title.ext`
- Example: `[憂傷-X]~周深 - 此生惟你.pdf`
- The `~` symbol indicates sheets that have been practiced

**Unpracticed sheets:**
- Format: `[Emotion-Difficulty]Artist - Title.ext`
- Example: `[憂傷-X]一支榴蓮 - 海底.pdf`
- No `~` symbol for sheets not yet practiced

### Night Piano Sheets (`night-piano/`)

- Format: `[Chapter]Number(Title).ext`
- Example: `[0]1(一個人).pdf`, `[Ⅰ]32(一個人的時光).pdf`
- Chapter markers:
  - `[0]` - Initial Demo version (網路連載版 1-31)
  - `[Ⅰ]` - Season 1 Album (第一季專輯)
  - `[Ⅱ]` - Season 2 Album (第二季專輯)
  - `[Ⅲ]` - Season 3 Album (第三季專輯)
  - `[Ⅳ]` - Season 4 Album (第四季專輯)
- No `~` marker as these are series collections

## Emotion Categories

- **平靜** (Calm) - Peaceful, soothing pieces
- **愉悅** (Joyful) - Upbeat, cheerful pieces
- **憂傷** (Melancholic) - Sad, touching pieces
- **激勵** (Inspiring) - Uplifting, energetic pieces
- **懷舊** (Nostalgic) - Memorial, reminiscent pieces

## Difficulty Levels

Current marker: `X` (未評估 / Not yet assessed)

Future options:
- `易` (Easy)
- `中` (Medium)
- `難` (Hard)

Or numerical levels (e.g., Lv1-Lv5)

## Source Management

All sheet music sources are documented in [SOURCES.md](SOURCES.md).

### For Popular Sheets
- Organized by emotion categories (平靜, 愉悅, 憂傷, 激勵, 懷舊)
- Each sheet includes:
  - **Source URLs** with labels (e.g., 貼文, 下載, 原網址)
  - **Availability status**: ✅ Available / ❌ Deleted / ⚠️ Moved
  - **Notes** for special conditions

### For Night Piano Series
- Organized by chapters (0, Ⅰ, Ⅱ, Ⅲ, Ⅳ)
  - Note: Chapters V and Ⅵ are documented in SOURCES.md but currently have no PDF files
- **General sources**: URLs applicable to entire chapters
- **Per-song sources**: Individual URLs for specific songs with their titles
- Special notes marked with italics (e.g., *無曲譜來源*, *暫無來源*)

### Adding New Sheets
When adding new sheet music:
1. Save the file following the naming convention
2. Add source information to `SOURCES.md` under the appropriate section
3. Include availability status and any relevant notes
