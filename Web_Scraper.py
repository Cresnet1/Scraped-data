
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs(location_filter=None, keyword_filter=None):
    url = "https://vacancymail.co.zw/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('a', class_='job-listing')

    job_data = []

    for job in job_listings:
        job_title = job.find('h3', class_='job-listing-title')
        company = job.find('h4', class_='job-listing-company')
        description = job.find('p', class_='job-listing-text')
        location_icon = job.find('i', class_='icon-material-outline-location-on')
        expiry_icon = job.find('i', class_='icon-material-outline-access-time')

        job_title_text = job_title.get_text(strip=True) if job_title else 'No job title found'
        company_text = company.get_text(strip=True) if company else 'No company found'
        description_text = description.get_text(strip=True) if description else 'No description found'
        location_text = location_icon.parent.get_text(strip=True) if location_icon else 'No location found'

        expiry_date = 'No expiry date found'
        if expiry_icon:
            expiry_li = expiry_icon.find_parent('li')
            if expiry_li and 'Expires' in expiry_li.get_text():
                expiry_date = expiry_li.get_text(strip=True).replace('Expires', '').strip()

        # Apply filters
        if location_filter and location_filter.lower() not in location_text.lower():
            continue
        if keyword_filter:
            keyword = keyword_filter.lower()
            if keyword not in job_title_text.lower() and keyword not in description_text.lower():
                continue

        job_data.append({
            'Job Title': job_title_text,
            'Company': company_text,
            'Description': description_text,
            'Location': location_text,
            'Expiry Date': expiry_date
        })

    if job_data:
        df = pd.DataFrame(job_data)
        df.to_csv('filtered_jobs.csv', index=False)
        print("Filtered job data saved to 'filtered_jobs.csv'")
    else:
        print("No jobs matched your filters.")

# 🔍 Ask the user for filters
location = input("Enter a location to filter by (or leave blank for all): ").strip()
keyword = input("Enter a keyword to filter by (or leave blank for all): ").strip()

scrape_jobs(location_filter=location if location else None,
            keyword_filter=keyword if keyword else None)
