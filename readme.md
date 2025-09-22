<img width="1536" height="1024" alt="ChatGPT Image Sep 22, 2025, 06_03_26 PM" src="https://github.com/user-attachments/assets/b6a6a73f-d999-47c2-ac8f-a81aa4ce3b8c" />
 
# PDF Unlocker Script (Python 3.13 Compatible)

A **powerful and lightweight Python script** to fully unlock PDF files using the **user/open password**, removing all restrictions including reading, editing, printing, and copying. This script is fully compatible with **Python 3.13**, supports **AES-encrypted PDFs**, and handles **Unicode/non-ASCII filenames** including Bangla or other international characters.

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [PDF Password Types](#pdf-password-types)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Troubleshooting](#troubleshooting)
* [Future Upgrades](#future-upgrades)
* [License](#license)

---

## Overview

Many PDF files are protected with passwords to restrict opening (reading) or editing. PDFs can have:

* **User/Reading Password** – Prevents opening the PDF without the correct password.
* **Owner/Editing Password** – Prevents editing, copying, printing, or other actions without permission.

This script allows you to:

1. Open PDFs with a known **reading/user password**.
2. Remove all encryption and restrictions.
3. Save an **unlocked copy** for full access.

> ⚠️ **Important:** Without the reading/open password, only owner restrictions can be removed. The PDF cannot be fully unlocked without the user password.

---

## Features

* Fully unlocks PDFs using **user/open password**.
* Supports **AES and standard PDF encryption**.
* Removes all **owner restrictions** (editing, copying, printing).
* Works with **Python 3.13**, no need for `pikepdf`.
* Handles **Unicode filenames** including Bangla, Arabic, Chinese, and other non-ASCII characters.
* Saves unlocked PDFs in the same folder as the original with `_unlocked.pdf` appended.
* Simple and lightweight, easily modifiable for batch operations.

---

## PDF Password Types

1. **User/Reading Password**

   * Protects the PDF from being opened without the correct password.
   * Required to fully unlock the PDF for reading and editing.

2. **Owner/Editing Password**

   * Restricts actions such as printing, copying, and editing.
   * Can often be removed if the PDF opens with or without the user password.

> Note: Your current script will only remove owner restrictions if the PDF opens without a reading password. For full unlocking, the reading password must be provided.

---

## Requirements

* **Python 3.13** (or higher)
* Python packages:

  * [PyPDF2](https://pypi.org/project/PyPDF2/)
  * [PyCryptodome](https://pypi.org/project/pycryptodome/)

Install the packages via pip:

```bash
python -m pip install PyPDF2 pycryptodome
```

---

## Installation

1. Download or clone the script into a folder:

```
D:\unlock pdf\
```

2. Ensure the Python packages (`PyPDF2` and `PyCryptodome`) are installed.
3. Open the script and set the PDF path and password:

```python
pdf_path = r"C:\Users\samii\Downloads\Documents\YourPDF.pdf"
pdf_password = "YourReadingPassword"
```

---

## Usage

1. Open **Command Prompt** and navigate to the script folder:

```cmd
cd "D:\unlock pdf"
```

2. Run the script:

```cmd
python unlock_single_pdf.py
```

3. The unlocked PDF will be saved in the same folder with `_unlocked.pdf` appended.

---

## Examples

Original PDF:

```
C:\Users\samii\Downloads\Documents\ইঞ্জিনিয়ারিং কনসেপ্ট বুক রসায়ন ১ম পত্র ২০২৫-২৬.pdf
```

Unlocked PDF:

```
C:\Users\samii\Downloads\Documents\ইঞ্জিনিয়ারিং কনসেপ্ট বুক রসায়ন ১ম পত্র ২০২৫-২৬_unlocked.pdf
```

---

## Troubleshooting

* **AES Decryption Error:** Make sure `PyCryptodome` is installed.

```bash
python -m pip install pycryptodome
```

* **File Not Found:** Ensure the path is correct and use `r""` for paths with spaces or Unicode characters.
* **PDF Still Locked for Reading:** Must provide the **user/open password**. Without it, only editing restrictions will be removed.
* **Unicode Issues:** This script fully supports Unicode filenames, including Bangla and other non-ASCII characters.

---

## Future Upgrades

* Batch unlocking multiple PDFs in a folder.
* Recursive directory scanning for subfolders.
* GUI drag-and-drop interface for easy use.
* Option to overwrite existing unlocked PDFs.
* Logging system to track successfully unlocked PDFs.

---

## License

This script is **free to use and modify**. Attribution appreciated but not required.

---

## Author

* Developed for **personal and professional use**.
* Compatible with modern Python environments.
* Maintains simplicity and reliability.

**Note:** Always respect copyright and legal restrictions when unlocking PDF files. This tool should only be used on files you have rights to access.


