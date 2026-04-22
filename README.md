# AStrip

AStrip is a lightweight text preprocessing tool for preparing word lists and phrases for Anki import.

It provides a safe and deterministic pipeline for cleaning raw text data.

---

## Pipeline

### 1. Prepare
- Creates input and output workspace files
- Validates file ownership using a security marker
- Prevents processing of unrelated files
- Resets workspace for a new session

### 2. Process
- Reads input file line by line
- Normalizes text:
  - lowercase conversion
  - whitespace cleanup (spaces, tabs, newlines)
- Removes empty lines
- Removes duplicates (after normalization)
- Writes clean output to file

---

## Safety Model

- Input file is never modified during processing
- Files are validated using a marker system
- Foreign files are not processed

---

## Usage

1. Run prepare step
2. Add raw text to input file
3. Run process step
4. Get cleaned output file

---

## Release

📦 Latest version: v1.0  
👉 See Release Notes for changes and details

---

## Purpose

To simplify preparation of large word and phrase lists for efficient Anki learning workflows.
