# Staying out of the AI-generated look

This brand was reviewed once and rejected for feeling "AI generated". This document is the record of
exactly what was wrong and what replaced it. Read it before building and self-review against it before
committing.

---

## What got rejected, specifically

| Rejected | Why it reads as machine-made | What replaced it |
|---|---|---|
| Uppercase mono micro-labels on every block (`CATEGORY BREAKDOWN`, `ON TRACK`, `PRIMARY`) | Nobody labels their own work that thoroughly. It is documentation cosplay. | Italic serif asides in sentence case, used sparingly — and often no label at all |
| Everything in an evenly-spaced card with the same padding | Uniform rhythm is the strongest tell. Real design has hierarchy and dead space. | One dominant element per screen; supporting content deliberately smaller and quieter |
| Pill badges everywhere as decoration | Pills are a status component. Used decoratively they read as filler. | Pills only in the Loud edition, only for genuine status |
| Three-up metric boxes with a label above a big number | The single most generated-looking layout on the internet. | Kept only on *This month*, where those three numbers are the actual product. Nowhere else. |
| Spec-sheet framing (a swatch grid, a type ramp, a components board as the product) | That is a designer's working file, not a shop. | Documentation lives in the handoff. The product shows the product. |
| Aggressive gradients, glassmorphism, coloured drop shadows | Default generated decoration. | Flat paper grounds, one photo shadow, nothing else |
| Inter, Roboto, generic geometric sans | Framework defaults. | Bricolage Grotesque + Lora. Arial only where fonts cannot be installed. |

## The register that was approved

Photo-led and warm. A real product photographed on a real desk, with the brand as a whisper in the
corner rather than a header bar. Slight rotation on the product card (-1.2deg Calm, +1.4deg Loud) and
a subtle striped ground so the surface reads as physical.

**Approved, with one exclusion:** the owner explicitly ruled out handwriting fonts and hand-drawn
annotation. Keep the warmth, keep it clean.

## Rules for anything new you make

**Type**
- Two families, no more. Bricolage Grotesque for structure, Lora for the human voice.
- Never set an interface label in uppercase mono. If something needs naming, name it in a sentence.
- Sizes on the scale in `DESIGN-SYSTEM.md`. Do not add intermediate steps to make things fit.

**Layout**
- Every screen has **one** dominant element. If everything is the same size, it is wrong.
- Uneven is fine. Two columns at 1.6fr / 1fr beats three equal columns.
- Leave real empty space. Do not fill a gap with a stat, an icon, or a testimonial.

**Colour**
- Calm: one accent, and it must survive greyscale printing.
- Loud: one saturated fill per block, and colour always keeps its assigned job (coral spend, teal save,
  gold reward, grape debt, lime income).
- No gradient may span more than one flat step. Prefer none.

**Copy**
- Write like a person who has used a budget and hated most of them.
- Specific beats aspirational: *"The budget you'll still be using in June"* not *"Take control of your
  finances"*.
- One idea per sentence. No triplets ("simple, powerful, beautiful"). No em-dash-joined summaries of
  the whole value prop.
- Never "just", "simply", "all you have to do", "hack your brain", "fix your ADHD".
- Humour aimed at the situation, never at the user.

**Imagery**
- No AI-generated images. No stock photography of smiling people at laptops.
- No hand-drawn SVG illustration — geometric primitives only (circles, rects, real type).
- Where a real photo or screenshot is needed and does not exist yet, ship a **labelled placeholder**
  saying exactly what goes there. A visible gap is honest; a generated stand-in is not.

**Iconography**
- The Focus Ring is the only drawn mark in the system.
- Shapes for badges and confetti, not icons. No icon set, no emoji.

## Self-review before committing

Answer these honestly. Any "yes" in the first five is a rework.

1. Could I swap this brand's name for another and lose nothing? → rework
2. Is every block the same size with the same padding? → rework
3. Does any interface label appear in uppercase mono? → rework
4. Is there a gradient, glass effect, or coloured shadow? → rework
5. Does any copy line sound like a landing-page template? → rework
6. Would a person who has never seen a design system understand each screen in five seconds?
7. Does the Calm edition still work printed in black and white?
8. Does the Loud edition have exactly one saturated fill per block?
9. Is every currency symbol coming from the config value?
10. Does anything anywhere punish the user for a missed week?
