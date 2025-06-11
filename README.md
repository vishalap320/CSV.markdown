# CSV/Excel to Markdown Converter

This project automates the conversion of structured data stored in an Excel (`.xlsx`) file into individual Markdown (`.md`) files. It's especially useful when working with large datasets like journaling entries, LLM-generated outputs, or stream-of-consciousness logs.

---

## Demo

Given an Excel file like this:

| Raw Text                        | JSON Text                                                   |
|--------------------------------|--------------------------------------------------------------|
| Stream of thought 1 for X.     | {"profile_name": "X", "thought_number": 1, ...}              |
| Stream of thought 2 for X.     | {"profile_name": "X", "thought_number": 2, ...}              |

This script will create:

`stream_thoughts_md/`
- `thought_0001.md`
- `thought_0002.md`
- ...
- `thought_1000.md`

Each file will contain the corresponding **Raw Text** content.

---

## Usage

This script is useful when:

 You have structured data (CSV or Excel) and need each entry as a separate file  
 You're building an NLP pipeline that uses text chunks from spreadsheets  
You want a simple way to batch convert structured inputs to Markdown format  

---

## How to Run This Code
Make sure Python 3.10+ is installed on your system.
You can check by running:
```python
python --version
```
If not installed, download it from: https://www.python.org/downloads/

1. ### Install dependencies
```bash
pip install pandas openpyxl
```
Save your Excel file ( stream_of_thoughts.xlsx\csv) to your desired folder.

Run the script
```python

python convert_to_markdown.py
```
## Output
Your Markdown files will appear in:

```bash
C:\Users\visha\Downloads\stream_thoughts_md
```

## Setting Up the Environment
Clone this repo:

```bash
git clone https://github.com/vishal320/CSV.markdown.git
cd CSV.markdown

```
Install dependencies:

```bash
pip install pandas openpyxl
```
Run the script:

```bash

python convert_to_markdown.py
```
## Testing
You can test with a sample Excel file structured like this:

Column A: "Raw Text"

Column B: "JSON Text" (optional for this script)

Make sure the file is saved in .xlsx format.

## How It Works
Loads the Excel file using pandas.read_excel()

Extracts each row from the “Raw Text” column

Creates a uniquely named .md file for each row


What Can This Code Do?
 Process 1000+ entries from Excel\csv files

Output cleanly named and structured Markdown files

Help convert datasets into file-based text corpora
