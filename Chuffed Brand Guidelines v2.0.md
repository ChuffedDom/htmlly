# Chuffed Brand Guidelines v3.0
## The CORE.120 Muted System
This document outlines the architectural standards for the **CORE.120 Muted** design system. The system is a "Chromatic Monochrome" aesthetic, utilising a desaturated 120° hue (Green) to create a high-fidelity, technical environment focused on clarity, professional depth, and precision.
## 1. Colour Palette
### 1.1 The Primary Atmospheric Base (Hue 120°)
The palette is strictly constrained to **Saturation 4–10%**. Do not use vibrant greens or pure blacks/whites.

| Role               | HEX       | Description                                      | HSL            |
| ------------------ | --------- | ------------------------------------------------ | -------------- |
| **Background**     | `#0a0b0a` | "Forest Charcoal" - Deepest base layer.          | `120, 4%, 4%`  |
| **Surface**        | `#181a18` | "Deep Timber" - Header strips, card backgrounds. | `120, 4%, 10%` |
| **Border**         | `#2c2e2c` | "Moss Slate" - UI outlines, dividers, inputs.    | `120, 4%, 18%` |
| **Secondary Text** | `#a1a4a1` | "Sage Grey" - Body copy and descriptions.        | `120, 4%, 65%` |
| **Primary Text**   | `#e4e6e4` | "Mist White" - Headings and active states.       | `120, 4%, 90%` |
| **Highlight**      | `#f8f9f8` | "Frost" - Buttons and high-contrast text.        | `120, 4%, 98%` |
### 1.2 The High-Visibility Accent (Hue 300°)
Used only for focal points and core transformations.
- **Accent Magenta:** `hsl(343, 93%, 52%)`
- **Usage:** Small markers (dots), specific keywords (e.g., "Entrepreneur"), and interactive hover states.
## 2. Typography
The system pairs high-precision Monospace with high-performance Sans-Serif.
### **JetBrains Mono** (Headings & UI Labels)
- **Use Case:** All `H1–H6`, Navigation, Labels, and Metadata.
- **Style:** `text-transform: uppercase`, `letter-spacing: 0.15em`.
- **Weight:** `Bold (700)` for headings; `Medium (500)` for labels.
### **Inter** (Body & Documentation)
- **Use Case:** Paragraphs, lead-in text, and lists.
- **Style:** `line-height: 1.6`.
- **Weight:** `Light (300)` for lead text; `Regular (400)` for standard body.
## 3. UI Components
### 3.1 The Structured Panel
Panels replace traditional "Terminal" windows to lean into a professional IDE look rather than a "hacker" look.
- **Structure:** `#2c2e2c` border (1px) with a `#0a0b0a` background.
- **Header:** A `#181a18` strip containing a label in `JetBrains Mono` (uppercase).
- **Labelling:** Use clear, professional descriptors (e.g., "Project Overview", "Ideation"). **Avoid** file extensions like `.log` or `.exe`.
### 3.2 Buttons
- **Primary CTA:** Mist White (`#e4e6e4`) background with Charcoal (`#0a0b0a`) text.
- **Hover State:** Translate `-1px` vertically and add a solid shadow of the **Accent Magenta** (`4px`).
- **Radius:** 2px (sharp but not aggressive).
## 4. Design Principles
### 1. Atmospheric Neutrality
The design should feel "Professional Grayscale" at first glance. The 120° green tint provides a subconscious "atmospheric" depth that feels high-fidelity and easy on the eyes for long sessions.
### 2. Flat Aesthetic (No Gradients)
Avoid all gradients, glows, or blurs. Depth is achieved purely through color value (Lightness) and structural borders.
### 3. Precision Markers
Instead of large splashes of color, use "Markers" to draw the eye:
- A single `6px` dot in a panel header.
- A period `.` at the end of a heading in the Magenta accent.
- A change in color for exactly one word in a headline.
### 4. No Technical Flourishes
**Strict Rule:** Avoid "Hacker" clichés.
- No "Scan lines" or glitch effects.
- No system logs or faux-terminal commands.
- No glowing text. The goal is to feel like a **High-End Professional Tool**, not a game interface.
## 5. Spacing System
Use a strict **16px** (4-unit) grid.
- **Internal Padding:** `calc(16px * 1.5)` or `24px`.
- **Section Gap:** `calc(16px * 6)` or `96px`.
- **Component Gap:** `calc(16px * 2)` or `32px`.