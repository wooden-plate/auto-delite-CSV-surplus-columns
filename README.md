# Order Data CSV Cleaner

A lightweight Python tool that extracts only essential business fields from messy EDI CSV files and outputs a clean, standardized `YYYYMMDD_orderData.csv` ready for downstream processing.

---

## Features
- Removes all unnecessary EDI surplus columns
- Extracts only required fields:
  - `PRID`
  - `OrderNumber`
  - `ItemID`
  - `ItemName`
  - `Quantity`
  - `DeliveryDate`
  - `DeliveryPlace`
- Automatically names the output file as `YYYYMMDD_orderData.csv`
- Robust against:
  - Extra/unexpected columns  
  - Column order changes  
  - Messy or malformed EDI data  
- Works with **Python standard library only** (no pandas required)
- Simple interactive CLI suitable for non-technical users

---

## Requirements
- Python 3.x  
(No external libraries needed)

---

## Usage

1. Place the script and the target CSV in the **same folder**.
2. Run the script:

python AutoDeliteCSVSurplusColumns.py

less
コードをコピーする

3. Enter the CSV file name when prompted:

対象CSVファイル名を入力してください: sample.csv

csharp
コードをコピーする

4. The cleaned file will be generated as:

20251207_orderData.csv

yaml
コードをコピーする

---

## Example

**Input (messy EDI CSV):**
- Surplus columns present: `SurplusA`, `SurplusC`, `SurplusD`, ...
- Column order inconsistent

**Output:**
A clean CSV containing only the required business fields.

---

## Purpose

This tool is designed for manufacturing, logistics, and purchasing workflows where EDI systems often output inconsistent or noisy CSV files. It enables rapid, reliable data sanitization without manual Excel cleanup.

---

## License
MIT