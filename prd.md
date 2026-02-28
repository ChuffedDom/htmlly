## Purpose

To use what I am good at, presentations and talking on camera, to drive to content as fast and friction-free as possible.

## Vision

One place that speeds up the pipeline of idea (scribbling in markdown files) through to post.

## Goals

- To build a 'markdown to branded presentation' flow in this sprint.
- To use it for the next two weeks and gain an idea of what the worlflow looks like.
- To have LLMs shape my rough layouts and notes into slide ready to present.

## Context

Right now, I do a lot of presentations. That is webinars and live stream etc. A lot of my output is in the form of slides and this is something I am good at so I want to utilise it more.

Right now, my slides are in Figma as it is easier to maintain my branding and move between different aspect ratios.

My workflow really starts with me in Obsidian to just get my stream of thought down.

I tend to use the same 7 or 8 layouts for slides.

This content will be for LinkedIn, YouTube, and TikTok.

## Problem

Running Chuffed Coaching, it is clear that a large part of my marketing is in social media. This means I need to deliver value on my channels and pages in a format that I am good at, live/recorded presentations. But, right now I am not utilising this to the best of my ability because going into Figma and creating the presentation is a real friction point for me. Therefore, I only do presentations for my paying clients, which leaves me feeling like I am leaving good content on the table to grow my audience and hence no maximising my go-to-market.


## Hypothesis

If I could go from a stream of thought to a presentation, then I would be delivering high quality content to my audience and therefore grow my brand.

**Markdown to HTML presentation will get me to good content faster.**

## User Stories

- I need to open Obsidian, just get my thoughts down on a particular subject and, potentially with the help of LLMs, have a HTML ready presentation.
- I need to simply call a template with arguments using markdown and get a HTML presentation.
- I want to work in a file in markdown in Obsidian (VSCode with AI Chat) and see live changes as I work on the document in HTML.
- I need my AI chat to contextual understand the available template and how the application works from the markdown file.


## Acceptance Criteria

- When the final slides are produced they need to be responsive and viewable at a minimum of 3:4 ratio, through 1:1, 4:3, and finally at 16:9.
- When the presentation is rendered, the CSS of the styling of the slides is in a separate file.
- When the markdown file is processed to HTML, all slides are rendered into a single HTML page with all slides ordered top to bottom vertically.
- When I open the presentation, each slide is fixed to the viewport of the browser window.
- When I press space, down arrow, or right arrow, the page autoscrolls to the next slide, aka the distance of the viewport height.
- When I press left arrow, or up arrow, the page autoscrolls to the previous slide
- When I run the main app, I can select a file and the slide need to update on saves.
- When I write a formatting line this will indicate the slide layout, with the subsequent lines as arguments.
- When I type $lide followed by
	- cover
	- about Me
	- title_list
	- title_text
	- title_image
	- singular_paragraph
	- to-do
	- big_text
	- group_of_two
	- group_of_three
	- group_of_four
	- big_text_small_image
	- loop_list
	- just Image
	- sign_off
		- then the appropriate function is called, and the HTML is rendered with the template using the subsequent lines as arguments
- When I put an image into a folder then it is relatively reference from the markdown document and the html