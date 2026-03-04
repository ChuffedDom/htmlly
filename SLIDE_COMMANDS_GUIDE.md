# Htmlly Presentation Slide Commands Guide

## Overview

Htmlly is a markdown-to-HTML presentation framework that converts specially formatted markdown files into interactive slide presentations. This guide documents all available slide commands and how to use them.

### General Syntax

All slides start with the command `$lide <slide_type>` on its own line, followed by the content for that slide. The parser collects all lines after the command until it encounters a blank line, which marks the end of that slide's content.

```
$lide <slide_type>
[content for the slide]
[more content]

```

### Navigation Controls

- **Next Slide**: Space, Down Arrow, or Right Arrow
- **Previous Slide**: Up Arrow or Left Arrow

---

## Available Slide Types

### 1. Cover Slide

**Command**: `$lide cover`

**Purpose**: Title/opening slide for your presentation.

**Content**: Uses markdown heading syntax:
- `# Text` renders as large heading 1 (9vh font size, coral background)
- `## Text` renders as heading 2 (6vh font size, gold text)

**Example**:
```
$lide cover
# My Awesome Presentation
# By
# Your Name
## Subtitle or tagline here
```

**Best For**: Opening slide with multiple title elements

---

### 2. About Me Slide

**Command**: `$lide about me`

**Purpose**: Predefined About Me slide with built-in layout.

**Content**: Does not consume any lines from the markdown file - it displays a hardcoded template with your bio, image, and social information.

**Example**:
```
$lide about me

```

**Note**: The template currently has hardcoded content. Modify `templates/about_me.html` directly to change the content.

**Best For**: Presenter introduction slide

---

### 3. Title List Slide

**Command**: `$lide title list`

**Purpose**: Display a heading with a bulleted list of items.

**Content**:
- First line: `## Title` (heading 2)
- Following lines: Markdown list items starting with `- `

**Example**:
```
$lide title list
## Key Points
- First important point
- Second important point
- Third important point
- Final point
```

**Best For**: Listing key information with a title

---

### 4. Title Text Slide

**Command**: `$lide title text`

**Purpose**: Display a heading followed by paragraph text.

**Content**:
- First line: `## Title` (heading 2, gold color)
- Following lines: Paragraph content

**Example**:
```
$lide title text
## Why This Matters
This is a paragraph explaining your point. You can write multiple sentences here to expand on your idea. The text will flow naturally on the slide.
```

**Best For**: Adding explanation or context with a title

---

### 5. Title Image Slide

**Command**: `$lide title image`

**Purpose**: Display a heading with an image below it.

**Content**:
- First line: `## Title` (heading 2, gold color)
- Following line: Image markdown: `![](image_url)`

**Example**:
```
$lide title image
## Check This Out
![](https://example.com/image.jpg)
```

**Best For**: Showing visual content with a descriptive title

---

### 6. Singular Paragraph Slide

**Command**: `$lide singular paragraph`

**Purpose**: Full-screen text for a single paragraph or quote.

**Content**: Plain text paragraph (no markdown formatting needed)

**Example**:
```
$lide singular paragraph
This is a powerful quote or key message that should be displayed prominently across the slide. Use this for impactful statements that deserve their own space.
```

**Best For**: Highlighting quotes, key takeaways, or powerful statements

---

### 7. To-Do Slide

**Command**: `$lide to do`

**Purpose**: Display a checklist with support for nested items.

**Content**:
- First line: `## Title` (heading 2)
- Following lines: Checkbox lists using `- [ ]` syntax
- Nested items: Use tab indentation before `- [ ]`

**Example**:
```
$lide to do
## Project Roadmap
- [ ] Phase 1: Planning
  - [ ] Define requirements
  - [ ] Design system
- [ ] Phase 2: Development
- [ ] Phase 3: Testing
  - [ ] Unit tests
  - [ ] Integration tests
```

**Best For**: Roadmaps, task lists, action items

---

### 8. Big Text Slide

**Command**: `$lide big text`

**Purpose**: Display a single emphasized text statement (10vh font size).

**Content**: Plain text that should be emphasized

**Example**:
```
$lide big text
This is the key message you want everyone to remember
```

**Best For**: Emphasis, call-to-action, or memorable takeaway

---

### 9. Group of Two Slide

**Command**: `$lide group of two`

**Purpose**: Split slide with two side-by-side cards separated by a connector word.

**Content**: Four parts in this order:
1. `### Left Title` (heading 3)
2. Left content (paragraph)
3. Connector word or phrase (typically "vs", "and", "or")
4. `### Right Title` (heading 3)
5. Right content (paragraph)

**Example**:
```
$lide group of two
### Option A
Explanation of first option with benefits and details
vs
### Option B
Explanation of second option with benefits and details
```

**Best For**: Comparisons, pros/cons, two viewpoints

---

### 10. Group of Three Slide

**Command**: `$lide group of three`

**Purpose**: Three side-by-side cards, each with a title and content.

**Content**: Alternating titles and content (6 items total):
1. `### Title 1` → Content 1
2. `### Title 2` → Content 2
3. `### Title 3` → Content 3

**Example**:
```
$lide group of three
### Strategy
Focus on long-term goals and planning
### Tactics
Execute daily actions to reach goals
### Measurement
Track progress and iterate accordingly
```

**Best For**: Three-part processes, frameworks, categories

---

### 11. Group of Four Slide

**Command**: `$lide group of four`

**Purpose**: Four cards in a 2x2 grid layout, each with title and content.

**Content**: Eight alternating titles and content (4 cards, each with heading and text)

**Example**:
```
$lide group of four
### First Pillar
Description of the first pillar
### Second Pillar
Description of the second pillar
### Third Pillar
Description of the third pillar
### Fourth Pillar
Description of the fourth pillar
```

**Best For**: Four core pillars, strategic framework, skill assessment

---

### 12. Big Text Small Image Slide

**Command**: `$lide big text small image`

**Purpose**: Large text on left, smaller image on right.

**Content**:
- First item: `## Text` (heading 2)
- Second item: Image markdown: `![](image_url)`

**Example**:
```
$lide big text small image
## Here is the text
![](https://example.com/image.jpg)
```

**Best For**: Text-image combinations where text is primary

---

### 13. Just Image Slide

**Command**: `$lide just image`

**Purpose**: Full-screen image display.

**Content**: Image markdown: `![](image_url)`

**Example**:
```
$lide just image
![](https://example.com/large-image.jpg)
```

**Best For**: Visual breaks, full-screen imagery, background photos

---

### 14. Sign Off Slide

**Command**: `$lide sign off`

**Purpose**: Predefined closing slide with presenter contact information and social links.

**Content**: Does not consume any lines - displays hardcoded template.

**Example**:
```
$lide sign off

```

**Note**: The template has hardcoded content. Modify `templates/sign_off.html` directly to customize.

**Best For**: Final slide with contact information

---

### 15. Loop List Slide

**Command**: `$lide loop list`

**Purpose**: Generic list display (similar to loop functionality).

**Content**: Multiple items that will be looped through

**Example**:
```
$lide loop list
Item 1
Item 2
Item 3
```

**Best For**: Dynamic lists of content

---

## Content Formatting Rules

### Markdown Support

All slide content supports markdown formatting:

- `# Heading 1` / `## Heading 2` / `### Heading 3` etc.
- `**Bold text**`
- `*Italic text*`
- `[Link text](https://url.com)`
- `![Alt text](https://image-url.com)`
- `- Bullet point list`
- `1. Numbered list`

### Line Breaks and Spacing

- **Blank lines end a slide**: A completely blank line after content marks the end of a slide
- **Line continuations**: Multiple consecutive non-blank lines are part of the same slide
- **Indentation**: Used for nested list items (to-do slides) and code blocks

### Special Characters

- Image URLs must be valid URLs: `![](https://...)`
- Avoid using raw HTML unless modifying templates directly
- The parser converts markdown to HTML automatically using the Python markdown library

---

## Complete Example Presentation

```
$lide cover
# My Project
# Presentation
## Q1 2026 Update

$lide about me

$lide title list
## Agenda
- Project Overview
- Key Achievements
- Challenges
- Next Steps

$lide title text
## Our Mission
We are building tools that make it easy for presenters to create beautiful slides using simple markdown syntax.

$lide big text
50% faster presentation creation

$lide group of three
### Before
Manual HTML editing is slow and error-prone
### With Htmlly
Write markdown, get beautiful slides automatically
### Result
More time on content, less on formatting

$lide singular paragraph
The future of presentations is markdown - simple, version-controllable, and accessible to everyone.

$lide sign off

```

---

## Tips for LLM Integration

When using an LLM to generate slides:

1. **Structure clearly**: Instruct the LLM to use the exact `$lide <type>` syntax
2. **Content mapping**: Map your desired content to appropriate slide types
3. **Validation**: Verify markdown syntax is correct (list items, headings, image URLs)
4. **Templates**: Reference this guide when prompting the LLM to generate slides
5. **Example format**: Provide existing slides as context for the LLM to follow

---

## Troubleshooting

### Slide not appearing

- Check that there's a blank line after your slide content
- Verify the `$lide` command is on its own line
- Ensure the slide type name is correctly spelled with underscores for spaces (e.g., `singular_paragraph`)

### Content appearing in wrong place

- Verify content follows immediately after the `$lide` command
- Check for proper markdown syntax (e.g., `##` for headings)
- Ensure blank line properly terminates the slide

### Image not loading

- Verify URLs are complete (include `https://`)
- Test the URL in a browser
- Ensure image format is supported (JPG, PNG, GIF, WebP)

### Styling looks off

- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- The HTML auto-reloads when the markdown file is saved
- Check templates in `/templates` folder if customization is needed

---

## File Structure

```
htmlly/
├── main.py              # Main application and file watcher
├── slide_generator.py   # Slide rendering functions
├── test_presentation.md # Your markdown presentation file
├── test_presentation.html # Generated HTML output
├── templates/           # HTML templates for each slide type
│   ├── main.html
│   ├── cover.html
│   ├── title_list.html
│   └── ... (other slide templates)
└── SLIDE_COMMANDS_GUIDE.md # This file
```

---

## Keyboard Shortcuts When Presenting

| Action | Key |
|--------|-----|
| Next Slide | Space, ↓, → |
| Previous Slide | ↑, ← |

---

Last updated: March 4, 2026
