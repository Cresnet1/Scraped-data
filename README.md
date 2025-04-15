# 💼 Zimbabwe Job Scraper

This Python project is a web scraper that collects job listings from [VacancyMail Zimbabwe](https://vacancymail.co.zw/jobs/) and filters them based on user input for **location** and **keywords**. The filtered results are saved in a CSV file called `filtered_jobs.csv`.

## ✨ Features

- 🔍 Real-time scraping of Zimbabwean job listings.
- 📍 Filter jobs by **location** and/or **keywords**.
- 📄 Extracts:
  - Job Title
  - Company Name
  - Job Description
  - Location
  - Expiry Date
- 📁 Saves results to a clean and organized CSV file.

## 🧰 Technologies Used

- **Python 3**
- **requests** – To fetch the web page.
- **BeautifulSoup** – To parse and extract HTML content.
- **pandas** – To organize data and export it as a CSV.

## 🖥️ How It Works

When you run the script:

1. It opens the job listings page on VacancyMail.
2. Extracts information for each job:
   - Title
   - Company
   - Description
   - Location
   - Expiry Date
3. Prompts the user to optionally enter:
   - A **location** (e.g., "Harare")
   - A **keyword** (e.g., "developer")
4. Filters the results using your input.
5. Saves matching results in a file named `filtered_jobs.csv`.
