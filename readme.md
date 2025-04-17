### ✅ `README.md`

```markdown
# 🕵️‍♂️ Simulated Job Scraper – Python Project

**Author**: Takudzwa Mhanda  
**Course Project**: Python Automation & Data Handling  
**Submission Date**: April 2025

---

## 📌 Project Overview

This Python project simulates a job scraper that extracts the **10 most recent job listings** by generating paginated job data. Although the data is hardcoded for safety and simplicity, it mimics a real-world scraping experience, complete with logging, formatted output, and file export.

---

## 🎯 Features

- ✅ **Simulated Pagination**: Scrapes 10 job listings across multiple "pages"
- 🖥 **Terminal Preview**: Jobs are printed in a clean layout for review
- 💾 **Data Export**: Saves results to **CSV** and **Excel** formats
- 🧠 **Modular Design**: Clean and reusable function-based code
- 📜 **Logging**: Tracks scraper activity in a `scraper.log` file
- 🧹 **File Cleanup**: Deletes old data/log files before each run

---

## ⚙️ How to Use

### 1. ✅ Install Dependencies

Make sure you have Python installed, then install `pandas` and `openpyxl`:

```bash
pip install pandas openpyxl
```

---

### 2. ▶️ Run the Script

```bash
python web_scraper.py
```

You'll see the job listings printed in your terminal, and two files will be generated:
- `scrape_data.csv`
- `scrape_data.xlsx`

You'll also get a log file:
- `scraper.log`


## 📋 Output Example

**Terminal Output**:

```
📋 Scraped Job Listings:
======================================================================
1. Security Guard Patrol Officer (Page 1)
   🏢 Company    : Defcorp (Pvt) Ltd
   📍 Location   : Harare
   📅 Expiry Date: April 23, 2025
   📝 Description: Patrolling assigned sites, managing shifts and guard deployments.
...
10. Welder (Page 2)
   🏢 Company    : Green Fuel
   📍 Location   : Chipinge
   📅 Expiry Date: March 24, 2025
   📝 Description: Welding for industrial and development projects.
======================================================================
```


## 📁 File Structure

project-folder/
│
├── web_scraper.py         # Main script
├── scrape_data.csv        # Output: CSV format
├── scrape_data.xlsx       # Output: Excel format
├── scraper.log            # Output: Logs events and errors
└── README.md              # Project documentation (this file)



## 🧠 What You’ll Learn

- How to simulate data scraping across multiple pages
- How to structure Python scripts for clarity and reusability
- How to write logs and handle file outputs
- How to format output for user-friendly terminal display


## 📬 Contact

**Takudzwa Mhanda**  
📧 mhandatakudzwa07@gmail.com  
🌍 Zimbabwe  

> This project was developed as part of a course on Python Automation & Data Handling. It demonstrates the logic behind scraping, pagination, and clean data export using a safe, simulated dataset.
