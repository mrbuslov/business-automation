# Receipt Scanner: Automated Receipt Data Extraction

This directory contains a **receipt scanner script** that automates the process of extracting data from receipt images
and generates a structured **DOCX report**. The program uses the **Anthropic AI model** to accurately extract text and
tabular data from receipts, making expense tracking and record-keeping effortless.

## How It Works

1. Place your receipt images in the designated folder.
2. Run the script to automatically process all images.
3. The script extracts relevant data and compiles it into a formatted DOCX file with a table of receipts.

## Requirements

- Python 3.x
- Anthropic API access
- Dependencies listed in `requirements.txt`

## Getting Started

1. Set up your Anthropic API key.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your receipt images in the `receipts/` folder.
4. Run the script:
   ```bash
   python receipts_scanner.py
   ```
5. Find the generated DOCX report in the output directory.

## Features

- **OCR for receipts** using Anthropic AI
- Batch processing of all receipt images in the provided folder
- Automated extraction of key fields: date, merchant, items, prices, total
- **DOCX report generation** with a clean, structured table of all extracted data
- Ideal for **expense tracking, bookkeeping, and accounting automation**

## Benefits

- Save time on manual receipt entry
- Improve accuracy of expense reports
- Simplify tax preparation and auditing
- Scalable for personal, small business, or enterprise use

## Use Cases

- Small businesses looking for **automated receipt scanning**
- Freelancers needing **expense report automation**
- Accountants seeking faster **data extraction from receipts**
- Anyone managing large volumes of receipts for reimbursement or compliance

---

**Keywords:** receipt scanner, automated receipt data extraction, OCR for receipts, receipt to DOCX, expense tracking
automation, bookkeeping script, accounting automation, Anthropic OCR script, extract text from receipts, business
expense report automation, Python receipt scanner, AI-powered receipt processing.
