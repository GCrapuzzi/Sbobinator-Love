# Sbobinator Love App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-page HTML/JS app optimized for Safari (iOS/iPadOS) that allows uploading audio files and transcribing them via NVIDIA NIM Whisper Large v3 directly from the browser.

**Architecture:** A single `index.html` file containing HTML, embedded CSS, and Vanilla JS. The JS code directly handles file reading and `fetch` calls to the NVIDIA API.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, NVIDIA NIM APIs.

---

### Task 1: Basic HTML Structure & Styling

**Files:**
- Create: `index.html`

- [ ] **Step 1: Write the HTML skeleton**
  Include viewport tags preventing zooming for iOS Safari (`content="width=device-width, initial-scale=1, maximum-scale=1"`).
- [ ] **Step 2: Add CSS for the "Playful & Card-based" mobile-first layout**
  Make sure touch targets (buttons) are at least 44px tall. Use pastel colors, rounded borders.
- [ ] **Step 3: Add UI elements**
  File input (hidden), huge friendly visible trigger button ("Carica l'audio ❤️"), loading container, result container.
- [ ] **Step 4: Verify UI visually**
  Run: `python3 -m http.server 8000` (already running) and verify in browser.
- [ ] **Step 5: Commit UI changes**
  Run: `git add index.html && git commit -m "feat: basic UI structure and styling"`

### Task 2: JavaScript Logic for API Request

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Get the NVIDIA API Key from the human**
  We'll extract it dynamically or ask the user to input it directly into the file.
- [ ] **Step 2: Add event listeners for the file input**
- [ ] **Step 3: Implement the fetch call to NVIDIA API**
- [ ] **Step 4: Implement loading ("Sto sbobinando questo file per te...") and error state ("Ops, c'è stato un piccolo intoppo...") UI updates**
- [ ] **Step 5: Manually test end-to-end functionality**
  In the browser, select a short audio file and test it.
- [ ] **Step 6: Commit logic changes**
  Run: `git add index.html && git commit -m "feat: implement transcription logic"`
