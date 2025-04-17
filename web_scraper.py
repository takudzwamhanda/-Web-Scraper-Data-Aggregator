# # # import csv
# # # import json

# # # # Job data
# # # jobs = [
# # #     {
# # #         "title": "Security Guard Patrol Officer",
# # #         "company": "Defcorp (Pvt) Ltd",
# # #         "location": "Harare",
# # #         "expiry_date": "April 23, 2025",
# # #         "description": (
# # #             "Responsible for patrolling assigned sites using a motorbike, overseeing guard deployments, "
# # #             "managing shift schedules, and ensuring that all guards are present."
# # #         )
# # #     },
# # #     {
# # #         "title": "Research Assistant",
# # #         "company": "CeSHHAR Zimbabwe",
# # #         "location": "Harare/Mt Darwin",
# # #         "expiry_date": "April 21, 2025",
# # #         "description": (
# # #             "Involves population health research and programming, including on sexual and reproductive "
# # #             "health and HIV/AIDS."
# # #         )
# # #     },
# # #     {
# # #         "title": "Projects Sales Manager",
# # #         "company": "Saint-Gobain Gyproc Zimbabwe",
# # #         "location": "Harare",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Drive project sales by developing and managing systems and processes for project pipeline "
# # #             "sales growth, customer relationship management, and technical point of sale material development."
# # #         )
# # #     },
# # #     {
# # #         "title": "Cash Transfer Services",
# # #         "company": "Development Aid from People to People Zimbabwe (DAPP)",
# # #         "location": "Harare",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Seeking experienced cash transfer service providers for a four-month project in Epworth District, "
# # #             "Harare, involving mobile cash transfers for 1,585 beneficiaries."
# # #         )
# # #     },
# # #     {
# # #         "title": "Project Administration Assistant",
# # #         "company": "Biomedical Research and Training Institute (BRTI)",
# # #         "location": "Manicaland",
# # #         "expiry_date": "May 12, 2025",
# # #         "description": (
# # #             "Support scientific population-based research on the incidence and control of HIV and other "
# # #             "communicable and non-communicable diseases in east Zimbabwe."
# # #         )
# # #     },
# # #     {
# # #         "title": "Registered General Nurse",
# # #         "company": "AIDS Healthcare Foundation",
# # #         "location": "Beitbridge",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Provide HIV management in health facilities, partnering with the Ministry of Health and Child Care "
# # #             "and local authorities to create Centers of Excellence."
# # #         )
# # #     },
# # #     {
# # #         "title": "Digital Marketing Attachee",
# # #         "company": "Golden Knot Group",
# # #         "location": "Harare",
# # #         "expiry_date": "April 16, 2025",
# # #         "description": (
# # #             "Support the existing team in digital marketing, content creation, and social media management."
# # #         )
# # #     },
# # #     {
# # #         "title": "Boiler Maker",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Responsible for boiler making tasks within the Land Development Department, reporting to the Projects Manager."
# # #         )
# # #     },
# # #     {
# # #         "title": "Artisan-Carpenter",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Responsible for building foundations, joining wood materials, and fitting and installing trim items for "
# # #             "industrial and residential structures."
# # #         )
# # #     },
# # #     {
# # #         "title": "Welder",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Perform welding tasks within the Land Development Department, reporting to the Projects Manager."
# # #         )
# # #     },
# # # ]

# # # # Print jobs to terminal
# # # print("=== RECENT JOB LISTINGS ===\n")
# # # for idx, job in enumerate(jobs, start=1):
# # #     print(f"{idx}. {job['title']} - {job['company']}")
# # #     print(f"   Location: {job['location']}")
# # #     print(f"   Expiry Date: {job['expiry_date']}")
# # #     print(f"   Description: {job['description']}\n")

# # # # Save to CSV
# # # csv_filename = "vacancymail_jobs.csv"
# # # with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
# # #     fieldnames = ["title", "company", "location", "expiry_date", "description"]
# # #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #     writer.writeheader()
# # #     writer.writerows(jobs)
# # # print(f"✅ Jobs saved to {csv_filename}")

# # # # Save to JSON
# # # json_filename = "vacancymail_jobs.json"
# # # with open(json_filename, "w", encoding="utf-8") as jsonfile:
# # #     json.dump(jobs, jsonfile, indent=4)
# # # print(f"✅ Jobs saved to {json_filename}")









# # # import csv
# # # import pandas as pd
# # # import logging
# # # import os

# # # # Configure logging
# # # logging.basicConfig(
# # #     filename="scraper.log",
# # #     level=logging.INFO,
# # #     format="%(asctime)s - %(levelname)s - %(message)s",
# # # )

# # # # Job data (limited to 10 jobs)
# # # jobs = [
# # #     {
# # #         "title": "Security Guard Patrol Officer",
# # #         "company": "Defcorp (Pvt) Ltd",
# # #         "location": "Harare",
# # #         "expiry_date": "April 23, 2025",
# # #         "description": (
# # #             "Responsible for patrolling assigned sites using a motorbike, overseeing guard deployments, "
# # #             "managing shift schedules, and ensuring that all guards are present."
# # #         )
# # #     },
# # #     {
# # #         "title": "Research Assistant",
# # #         "company": "CeSHHAR Zimbabwe",
# # #         "location": "Harare/Mt Darwin",
# # #         "expiry_date": "April 21, 2025",
# # #         "description": (
# # #             "Involves population health research and programming, including on sexual and reproductive "
# # #             "health and HIV/AIDS."
# # #         )
# # #     },
# # #     {
# # #         "title": "Projects Sales Manager",
# # #         "company": "Saint-Gobain Gyproc Zimbabwe",
# # #         "location": "Harare",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Drive project sales by developing and managing systems and processes for project pipeline "
# # #             "sales growth, customer relationship management, and technical point of sale material development."
# # #         )
# # #     },
# # #     {
# # #         "title": "Cash Transfer Services",
# # #         "company": "Development Aid from People to People Zimbabwe (DAPP)",
# # #         "location": "Harare",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Seeking experienced cash transfer service providers for a four-month project in Epworth District, "
# # #             "Harare, involving mobile cash transfers for 1,585 beneficiaries."
# # #         )
# # #     },
# # #     {
# # #         "title": "Project Administration Assistant",
# # #         "company": "Biomedical Research and Training Institute (BRTI)",
# # #         "location": "Manicaland",
# # #         "expiry_date": "May 12, 2025",
# # #         "description": (
# # #             "Support scientific population-based research on the incidence and control of HIV and other "
# # #             "communicable and non-communicable diseases in east Zimbabwe."
# # #         )
# # #     },
# # #     {
# # #         "title": "Registered General Nurse",
# # #         "company": "AIDS Healthcare Foundation",
# # #         "location": "Beitbridge",
# # #         "expiry_date": "April 25, 2025",
# # #         "description": (
# # #             "Provide HIV management in health facilities, partnering with the Ministry of Health and Child Care "
# # #             "and local authorities to create Centers of Excellence."
# # #         )
# # #     },
# # #     {
# # #         "title": "Digital Marketing Attachee",
# # #         "company": "Golden Knot Group",
# # #         "location": "Harare",
# # #         "expiry_date": "April 16, 2025",
# # #         "description": (
# # #             "Support the existing team in digital marketing, content creation, and social media management."
# # #         )
# # #     },
# # #     {
# # #         "title": "Boiler Maker",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Responsible for boiler making tasks within the Land Development Department, reporting to the Projects Manager."
# # #         )
# # #     },
# # #     {
# # #         "title": "Artisan-Carpenter",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Responsible for building foundations, joining wood materials, and fitting and installing trim items for "
# # #             "industrial and residential structures."
# # #         )
# # #     },
# # #     {
# # #         "title": "Welder",
# # #         "company": "Green Fuel",
# # #         "location": "Chipinge",
# # #         "expiry_date": "March 24, 2025",
# # #         "description": (
# # #             "Perform welding tasks within the Land Development Department, reporting to the Projects Manager."
# # #         )
# # #     },
# # # ]

# # # # Function to remove existing files
# # # def remove_existing_file(filename):
# # #     if os.path.exists(filename):
# # #         try:
# # #             os.remove(filename)
# # #             logging.info(f"Removed existing file: {filename}")
# # #         except Exception as e:
# # #             logging.error(f"Error removing file {filename}: {e}")

# # # # Remove existing jobs.csv and jobs.xlsx
# # # remove_existing_file("jobs.csv")
# # # remove_existing_file("jobs.xlsx")

# # # # Save to CSV in 'web_scraper.csv'
# # # csv_filename = "web_scraper.csv"
# # # try:
# # #     with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
# # #         fieldnames = ["title", "company", "location", "expiry_date", "description"]
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(jobs[:10])  # Limit to 10 jobs
# # #     logging.info(f"✅ Jobs successfully saved to {csv_filename}")
# # # except Exception as e:
# # #     logging.error(f"❌ Error saving jobs to {csv_filename}: {e}")

# # # # Save to Excel in 'web_scraper.xlsx'
# # # excel_filename = "web_scraper.xlsx"
# # # try:
# # #     df = pd.DataFrame(jobs[:10])  # Limit to 10 jobs
# # #     df.to_excel(excel_filename, index=False)
# # #     logging.info(f"✅ Jobs successfully saved to {excel_filename}")
# # # except Exception as e:
# # #     logging.error(f"❌ Error saving jobs to {excel_filename}: {e}")

# # # print("✅ Scraper process completed. Check scraper.log for details.")






# # import csv
# # import pandas as pd
# # import logging
# # import os
# # import json

# # # Configure logging
# # logging.basicConfig(
# #     filename="scraper.log",
# #     level=logging.INFO,
# #     format="%(asctime)s - %(levelname)s - %(message)s",
# # )

# # # Sample job data (limit to 10 jobs)
# # jobs = [
# #     {
# #         "title": "Security Guard Patrol Officer",
# #         "company": "Defcorp (Pvt) Ltd",
# #         "location": "Harare",
# #         "expiry_date": "April 23, 2025",
# #         "description": (
# #             "Responsible for patrolling assigned sites using a motorbike, overseeing guard deployments, "
# #             "managing shift schedules, and ensuring that all guards are present."
# #         )
# #     },
# #     {
# #         "title": "Research Assistant",
# #         "company": "CeSHHAR Zimbabwe",
# #         "location": "Harare/Mt Darwin",
# #         "expiry_date": "April 21, 2025",
# #         "description": (
# #             "Involves population health research and programming, including on sexual and reproductive "
# #             "health and HIV/AIDS."
# #         )
# #     },
# #     {
# #         "title": "Projects Sales Manager",
# #         "company": "Saint-Gobain Gyproc Zimbabwe",
# #         "location": "Harare",
# #         "expiry_date": "April 25, 2025",
# #         "description": (
# #             "Drive project sales by developing and managing systems and processes for project pipeline "
# #             "sales growth, customer relationship management, and technical point of sale material development."
# #         )
# #     },
# #     {
# #         "title": "Cash Transfer Services",
# #         "company": "Development Aid from People to People Zimbabwe (DAPP)",
# #         "location": "Harare",
# #         "expiry_date": "April 25, 2025",
# #         "description": (
# #             "Seeking experienced cash transfer service providers for a four-month project in Epworth District, "
# #             "Harare, involving mobile cash transfers for 1,585 beneficiaries."
# #         )
# #     },
# #     {
# #         "title": "Project Administration Assistant",
# #         "company": "Biomedical Research and Training Institute (BRTI)",
# #         "location": "Manicaland",
# #         "expiry_date": "May 12, 2025",
# #         "description": (
# #             "Support scientific population-based research on the incidence and control of HIV and other "
# #             "communicable and non-communicable diseases in east Zimbabwe."
# #         )
# #     },
# #     {
# #         "title": "Registered General Nurse",
# #         "company": "AIDS Healthcare Foundation",
# #         "location": "Beitbridge",
# #         "expiry_date": "April 25, 2025",
# #         "description": (
# #             "Provide HIV management in health facilities, partnering with the Ministry of Health and Child Care "
# #             "and local authorities to create Centers of Excellence."
# #         )
# #     },
# #     {
# #         "title": "Digital Marketing Attachee",
# #         "company": "Golden Knot Group",
# #         "location": "Harare",
# #         "expiry_date": "April 16, 2025",
# #         "description": (
# #             "Support the existing team in digital marketing, content creation, and social media management."
# #         )
# #     },
# #     {
# #         "title": "Boiler Maker",
# #         "company": "Green Fuel",
# #         "location": "Chipinge",
# #         "expiry_date": "March 24, 2025",
# #         "description": (
# #             "Responsible for boiler making tasks within the Land Development Department, reporting to the Projects Manager."
# #         )
# #     },
# #     {
# #         "title": "Artisan-Carpenter",
# #         "company": "Green Fuel",
# #         "location": "Chipinge",
# #         "expiry_date": "March 24, 2025",
# #         "description": (
# #             "Responsible for building foundations, joining wood materials, and fitting and installing trim items for "
# #             "industrial and residential structures."
# #         )
# #     },
# #     {
# #         "title": "Welder",
# #         "company": "Green Fuel",
# #         "location": "Chipinge",
# #         "expiry_date": "March 24, 2025",
# #         "description": (
# #             "Perform welding tasks within the Land Development Department, reporting to the Projects Manager."
# #         )
# #     },
# # ]

# # # Function to remove existing files
# # def remove_existing_file(filename):
# #     if os.path.exists(filename):
# #         try:
# #             os.remove(filename)
# #             logging.info(f"Removed existing file: {filename}")
# #         except Exception as e:
# #             logging.error(f"Error removing file {filename}: {e}")

# # # Remove existing files
# # remove_existing_file("vacancymail_jobs.csv")
# # remove_existing_file("vacancymail_jobs.xlsx")
# # remove_existing_file("vacancymail_jobs.json")
# # remove_existing_file("web_scraper.csv")
# # remove_existing_file("web_scraper.xlsx")

# # # Save to CSV as 'web_scraper.csv'
# # csv_filename = "web_scraper.csv"
# # try:
# #     with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
# #         fieldnames = ["title", "company", "location", "expiry_date", "description"]
# #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #         writer.writeheader()
# #         writer.writerows(jobs[:10])  # limit to 10 jobs
# #     logging.info(f"✅ Jobs successfully saved to {csv_filename}")
# # except Exception as e:
# #     logging.error(f"❌ Error saving jobs to {csv_filename}: {e}")

# # # Save to Excel as 'web_scraper.xlsx'
# # excel_filename = "web_scraper.xlsx"
# # try:
# #     df = pd.DataFrame(jobs[:10])
# #     df.to_excel(excel_filename, index=False)
# #     logging.info(f"✅ Jobs successfully saved to {excel_filename}")
# # except Exception as e:
# #     logging.error(f"❌ Error saving jobs to {excel_filename}: {e}")

# # # Rename files to 'scrape_data.csv' and 'scrape_data.xlsx'
# # try:
# #     os.rename("web_scraper.csv", "scrape_data.csv")
# #     print("Renamed 'web_scraper.csv' to 'scrape_data.csv'")
# # except Exception as e:
# #     print(f"Error renaming 'web_scraper.csv': {e}")

# # try:
# #     os.rename("web_scraper.xlsx", "scrape_data.xlsx")
# #     print("Renamed 'web_scraper.xlsx' to 'scrape_data.xlsx'")
# # except Exception as e:
# #     print(f"Error renaming 'web_scraper.xlsx': {e}")

# # print("✅ All processes completed.")





# import csv
# import pandas as pd
# import logging
# import os

# # List of files to delete at start
# files_to_delete = [
#     "vacancymail_jobs.csv",
#     "vacancymail_jobs.xlsx",
#     "vacancymail_jobs.json",
#     "web_scraper.csv",
#     "web_scraper.xlsx",
#     "scraper.log"
# ]

# # Remove existing files including log
# def remove_existing_files(file_list):
#     for filename in file_list:
#         if os.path.exists(filename):
#             try:
#                 os.remove(filename)
#                 print(f"Removed old file: {filename}")
#             except Exception as e:
#                 print(f"Error removing {filename}: {e}")

# remove_existing_files(files_to_delete)

# # Configure logging to overwrite previous log
# logging.basicConfig(
#     filename="scraper.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filemode='w'  # Overwrite log file each run
# )

# # Sample job data (limit to 10 jobs)
# jobs = [
#     {
#         "title": "Security Guard Patrol Officer",
#         "company": "Defcorp (Pvt) Ltd",
#         "location": "Harare",
#         "expiry_date": "April 23, 2025",
#         "description": (
#             "Responsible for patrolling assigned sites using a motorbike, overseeing guard deployments, "
#             "managing shift schedules, and ensuring that all guards are present."
#         )
#     },
#     {
#         "title": "Research Assistant",
#         "company": "CeSHHAR Zimbabwe",
#         "location": "Harare/Mt Darwin",
#         "expiry_date": "April 21, 2025",
#         "description": (
#             "Involves population health research and programming, including on sexual and reproductive "
#             "health and HIV/AIDS."
#         )
#     },
#     {
#         "title": "Projects Sales Manager",
#         "company": "Saint-Gobain Gyproc Zimbabwe",
#         "location": "Harare",
#         "expiry_date": "April 25, 2025",
#         "description": (
#             "Drive project sales by developing and managing systems and processes for project pipeline "
#             "sales growth, customer relationship management, and technical point of sale material development."
#         )
#     },
#     {
#         "title": "Cash Transfer Services",
#         "company": "Development Aid from People to People Zimbabwe (DAPP)",
#         "location": "Harare",
#         "expiry_date": "April 25, 2025",
#         "description": (
#             "Seeking experienced cash transfer service providers for a four-month project in Epworth District, "
#             "Harare, involving mobile cash transfers for 1,585 beneficiaries."
#         )
#     },
#     {
#         "title": "Project Administration Assistant",
#         "company": "Biomedical Research and Training Institute (BRTI)",
#         "location": "Manicaland",
#         "expiry_date": "May 12, 2025",
#         "description": (
#             "Support scientific population-based research on the incidence and control of HIV and other "
#             "communicable and non-communicable diseases in east Zimbabwe."
#         )
#     },
#     {
#         "title": "Registered General Nurse",
#         "company": "AIDS Healthcare Foundation",
#         "location": "Beitbridge",
#         "expiry_date": "April 25, 2025",
#         "description": (
#             "Provide HIV management in health facilities, partnering with the Ministry of Health and Child Care "
#             "and local authorities to create Centers of Excellence."
#         )
#     },
#     {
#         "title": "Digital Marketing Attachee",
#         "company": "Golden Knot Group",
#         "location": "Harare",
#         "expiry_date": "April 16, 2025",
#         "description": (
#             "Support the existing team in digital marketing, content creation, and social media management."
#         )
#     },
#     {
#         "title": "Boiler Maker",
#         "company": "Green Fuel",
#         "location": "Chipinge",
#         "expiry_date": "March 24, 2025",
#         "description": (
#             "Responsible for boiler making tasks within the Land Development Department, reporting to the Projects Manager."
#         )
#     },
#     {
#         "title": "Artisan-Carpenter",
#         "company": "Green Fuel",
#         "location": "Chipinge",
#         "expiry_date": "March 24, 2025",
#         "description": (
#             "Responsible for building foundations, joining wood materials, and fitting and installing trim items for "
#             "industrial and residential structures."
#         )
#     },
#     {
#         "title": "Welder",
#         "company": "Green Fuel",
#         "location": "Chipinge",
#         "expiry_date": "March 24, 2025",
#         "description": (
#             "Perform welding tasks within the Land Development Department, reporting to the Projects Manager."
#         )
#     },
# ]

# # Save to CSV
# try:
#     with open("web_scraper.csv", "w", newline="", encoding="utf-8") as csvfile:
#         fieldnames = ["title", "company", "location", "expiry_date", "description"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(jobs[:10])
#     logging.info("Saved jobs to web_scraper.csv")
# except Exception as e:
#     logging.error(f"Error saving CSV: {e}")

# # Save to Excel
# try:
#     df = pd.DataFrame(jobs[:10])
#     df.to_excel("web_scraper.xlsx", index=False)
#     logging.info("Saved jobs to web_scraper.xlsx")
# except Exception as e:
#     logging.error(f"Error saving Excel: {e}")

# # Rename files to final filenames
# try:
#     os.rename("web_scraper.csv", "scrape_data.csv")
#     print("Renamed 'web_scraper.csv' to 'scrape_data.csv'")
# except Exception as e:
#     print(f"Error renaming 'web_scraper.csv': {e}")

# try:
#     os.rename("web_scraper.xlsx", "scrape_data.xlsx")
#     print("Renamed 'web_scraper.xlsx' to 'scrape_data.xlsx'")
# except Exception as e:
#     print(f"Error renaming 'web_scraper.xlsx': {e}")

# print("✅ All processes completed.")











import csv
import pandas as pd
import logging
import os

# List of files to delete at start
files_to_delete = [
    "vacancymail_jobs.csv",
    "vacancymail_jobs.xlsx",
    "vacancymail_jobs.json",
    "web_scraper.csv",
    "web_scraper.xlsx",
    "scraper.log",
    "data_scrape.csv",
    "data_scrape.xlsx"
]

# Remove existing files including log
def remove_existing_files(file_list):
    for filename in file_list:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"Removed old file: {filename}")
            except Exception as e:
                print(f"Error removing {filename}: {e}")

remove_existing_files(files_to_delete)

# Configure logging to overwrite previous log
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w'  # Overwrite log file each run
)

# Sample job data (limit to 10 jobs)
jobs = [
    {
        "title": "Security Guard Patrol Officer",
        "company": "Defcorp (Pvt) Ltd",
        "location": "Harare",
        "expiry_date": "April 23, 2025",
        "description": (
            "Responsible for patrolling assigned sites using a motorbike, overseeing guard deployments, "
            "managing shift schedules, and ensuring that all guards are present."
        )
    },
    {
        "title": "Research Assistant",
        "company": "CeSHHAR Zimbabwe",
        "location": "Harare/Mt Darwin",
        "expiry_date": "April 21, 2025",
        "description": (
            "Involves population health research and programming, including on sexual and reproductive "
            "health and HIV/AIDS."
        )
    },
    {
        "title": "Projects Sales Manager",
        "company": "Saint-Gobain Gyproc Zimbabwe",
        "location": "Harare",
        "expiry_date": "April 25, 2025",
        "description": (
            "Drive project sales by developing and managing systems and processes for project pipeline "
            "sales growth, customer relationship management, and technical point of sale material development."
        )
    },
    {
        "title": "Cash Transfer Services",
        "company": "Development Aid from People to People Zimbabwe (DAPP)",
        "location": "Harare",
        "expiry_date": "April 25, 2025",
        "description": (
            "Seeking experienced cash transfer service providers for a four-month project in Epworth District, "
            "Harare, involving mobile cash transfers for 1,585 beneficiaries."
        )
    },
    {
        "title": "Project Administration Assistant",
        "company": "Biomedical Research and Training Institute (BRTI)",
        "location": "Manicaland",
        "expiry_date": "May 12, 2025",
        "description": (
            "Support scientific population-based research on the incidence and control of HIV and other "
            "communicable and non-communicable diseases in east Zimbabwe."
        )
    },
    {
        "title": "Registered General Nurse",
        "company": "AIDS Healthcare Foundation",
        "location": "Beitbridge",
        "expiry_date": "April 25, 2025",
        "description": (
            "Provide HIV management in health facilities, partnering with the Ministry of Health and Child Care "
            "and local authorities to create Centers of Excellence."
        )
    },
    {
        "title": "Digital Marketing Attachee",
        "company": "Golden Knot Group",
        "location": "Harare",
        "expiry_date": "April 16, 2025",
        "description": (
            "Support the existing team in digital marketing, content creation, and social media management."
        )
    },
    {
        "title": "Boiler Maker",
        "company": "Green Fuel",
        "location": "Chipinge",
        "expiry_date": "March 24, 2025",
        "description": (
            "Responsible for boiler making tasks within the Land Development Department, reporting to the Projects Manager."
        )
    },
    {
        "title": "Artisan-Carpenter",
        "company": "Green Fuel",
        "location": "Chipinge",
        "expiry_date": "March 24, 2025",
        "description": (
            "Responsible for building foundations, joining wood materials, and fitting and installing trim items for "
            "industrial and residential structures."
        )
    },
    {
        "title": "Welder",
        "company": "Green Fuel",
        "location": "Chipinge",
        "expiry_date": "March 24, 2025",
        "description": (
            "Perform welding tasks within the Land Development Department, reporting to the Projects Manager."
        )
    },
]

# Save to CSV as 'scrape_data.csv'
try:
    with open("scrape_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "company", "location", "expiry_date", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs[:10])
    logging.info("Saved jobs to scrape_data.csv")
except Exception as e:
    logging.error(f"Error saving CSV: {e}")

# Save to Excel as 'scrape_data.xlsx'
try:
    df = pd.DataFrame(jobs[:10])
    df.to_excel("scrape_data.xlsx", index=False)
    logging.info("Saved jobs to scrape_data.xlsx")
except Exception as e:
    logging.error(f"Error saving Excel: {e}")

# Rename files to final filenames
try:
    os.rename("scrape_data.csv", "scrape_data.csv")
    print("Confirmed: 'scrape_data.csv' is ready.")
except Exception as e:
    print(f"Error confirming 'scrape_data.csv': {e}")

try:
    os.rename("scrape_data.xlsx", "scrape_data.xlsx")
    print("Confirmed: 'scrape_data.xlsx' is ready.")
except Exception as e:
    print(f"Error confirming 'scrape_data.xlsx': {e}")

print("✅ All processes completed.")
