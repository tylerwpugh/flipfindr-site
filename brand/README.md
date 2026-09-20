# FlipFindr brand marks

**`build-mark.py` regenerates every size from geometry.** Nothing here is traced or cropped from a
screenshot, so the edges stay clean at any size and the colours are exact.

## Colours — these are the site's own tokens, not sampled from an image
| token | hex | where |
|---|---|---|
| `--ink`  | `#102132` | house outline, glass, handle |
| `--blue` | `#126ab0` | window panes, roof flag |

⚠️ Tyler's reference JPEG samples at `#181d23` because it is a **compressed photo of a logo**, not
the artwork. **Do not sample colours from it.** The consent-screen logo and the site must be
provably the same colours — that match is what Google checks.

## Files
**Mark only** (house + glass, no text):
- `flipfindr-mark-120.png` — **the Google OAuth consent screen size**
- `flipfindr-mark-512.png`, `flipfindr-mark-1024.png` — everything else

**Reversed mark** — for dark backgrounds:
- `flipfindr-mark-reversed-120.png`, `-512`, `-1024`

🚨 **The dark mark disappears on a dark ground.** The house and glass are `--ink` `#102132`, and the
site's dark sections are essentially that same navy — on those, only the four blue panes show.
**Always use the reversed file on anything dark.** This was caught by rendering at real sizes, not
by looking at the artwork.

⚠️ **16px (browser tab) is rough and cannot be fully fixed.** A house, a glass ring, a handle and
four separate panes cannot resolve in ~250 pixels — it reads as a smudge with a hint of blue. It is
clean from 32px up. Either accept it, or keep a simplified icon (the old **F**) for the 16px slot
only, which is what many brands do. **Not a design flaw; physics.**

**Lockups** (mark + wordmark), from `build-lockup.py`:
- `flipfindr-lockup-horizontal.png` — **site header**, mark left, wordmark right
- `flipfindr-lockup-stacked.png` — mark above, wordmark below; matches Tyler's chosen reference

Wordmark is **"Flip" in `--ink`, "Findr" in `--blue`**, set in **SF (`SFNS.ttf`) Heavy** — the
site's own `-apple-system` fallback, so the lockup and the page agree. ⛔ The site's first-choice
face is **Inter**; if it is ever installed locally, rebuild with it for an exact match.

## Why the mark has no wordmark
A square icon cannot hold "FlipFindr" underneath and stay legible at 120×120. **The mark alone is
the icon; the full lockup with text belongs in the site header** and anywhere with horizontal room.

## Regenerating
`python3 build-mark.py` — needs Pillow. Geometry is authored on a 1024 grid and supersampled 6×,
so new sizes cost nothing. Adjust stroke weight, the roof flag, or the glass position by editing the
numbers near the top of `build()`.
