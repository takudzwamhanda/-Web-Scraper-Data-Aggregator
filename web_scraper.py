import csv
import pandas as pd
import logging
import os
import time

# ========== CLEANUP: DELETE OLD FILES FIRST ========== #

files_to_delete = [
    "vacancymail_jobs.csv",
    "vacancymail_jobs.xlsx",
    "scraper.log",
    "scrape_data.csv",
    "scrape_data.xlsx"
]

def remove_old_files(file_list):
    """Delete leftover files before fresh run."""
    for filename in file_list:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"🗑 Removed: {filename}")
            except Exception as e:
                print(f"❌ Error removing {filename}: {e}")

remove_old_files(files_to_delete)

# ========== LOGGING SETUP ========== #

logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w'
)

# ========== SIMULATED SCRAPER DATA ========== #

base_jobs = [
    {
        "title": "Security Guard Patrol Officer",
        "company": "Defcorp (Pvt) Ltd",
        "location": "Harare",
        "expiry_date": "April 23, 2025",
        "description": "Patrolling assigned sites, managing shifts and guard deployments."
    },
    {
        "title": "Research Assistant",
        "company": "CeSHHAR Zimbabwe",
        "location": "Harare/Mt Darwin",
        "expiry_date": "April 21, 2025",
        "description": "Conduct population health and HIV/AIDS research support."
    },
    {
        "title": "Digital Marketing Attachee",
        "company": "Golden Knot Group",
        "location": "Harare",
        "expiry_date": "April 16, 2025",
        "description": "Support digital marketing, social media, and content creation."
    },
    {
        "title": "Project Admin Assistant",
        "company": "BRTI",
        "location": "Manicaland",
        "expiry_date": "May 12, 2025",
        "description": "Assist in administration for HIV research projects."
    },
    {
        "title": "Welder",
        "company": "Green Fuel",
        "location": "Chipinge",
        "expiry_date": "March 24, 2025",
        "description": "Welding for industrial and development projects."
    }
]

def simulate_scrape_page(page_num):
    """Return job listings for a simulated page number."""
    jobs = []
    for job in base_jobs:
        copy = job.copy()
        copy["title"] += f" (Page {page_num})"
        jobs.append(copy)
    logging.info(f"📄 Simulated scrape for page {page_num}")
    return jobs

# ========== DISPLAY JOBS ========== #

def print_jobs(jobs):
    """Display scraped jobs in the terminal."""
    print("\n📋 Scraped Job Listings:")
    print("=" * 70)
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']}")
        print(f"   🏢 Company    : {job['company']}")
        print(f"   📍 Location   : {job['location']}")
        print(f"   📅 Expiry Date: {job['expiry_date']}")
        print(f"   📝 Description: {job['description']}\n")
    print("=" * 70)

# ========== SAVE JOBS ========== #

def save_to_csv(jobs, filename="scrape_data.csv"):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "expiry_date", "description"])
            writer.writeheader()
            writer.writerows(jobs)
        logging.info(f"✅ Saved to CSV: {filename}")
        print("✅ Data saved to CSV.")
    except Exception as e:
        logging.error(f"❌ Error saving CSV: {e}")

def save_to_excel(jobs, filename="scrape_data.xlsx"):
    try:
        df = pd.DataFrame(jobs)
        df.to_excel(filename, index=False)
        logging.info(f"✅ Saved to Excel: {filename}")
        print("✅ Data saved to Excel.")
    except Exception as e:
        logging.error(f"❌ Error saving Excel: {e}")

# ========== SCRAPER EXECUTION ========== #

def run_scraper():
    print("🚀 Starting simulated scraper...")
    logging.info("🚀 Job scraper started.")

    all_jobs = []
    page = 1

    while len(all_jobs) < 10:
        jobs = simulate_scrape_page(page)
        for job in jobs:
            if len(all_jobs) < 10:
                all_jobs.append(job)
            else:
                break
        page += 1
        time.sleep(1)  # simulate delay between pages

    # Print jobs to terminal first
    print_jobs(all_jobs)

    # Save to CSV and Excel
    save_to_csv(all_jobs)
    save_to_excel(all_jobs)

    print("🏁 Scraped exactly 10 jobs. Done.")
    logging.info("🏁 Scraped 10 jobs and finished.")

# ========== RUN ========== #

if __name__ == "__main__":
    run_scraper()
