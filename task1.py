import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

def scrape_bbc_headlines():
    url = 'https://www.bbc.com/news'  # URL of the BBC News website
    response = requests.get(url)

    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements that contain headlines (specific to the BBC structure)
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

        # Extract text from the headline elements
        headline_texts = [headline.get_text(strip=True) for headline in headlines]

        return headline_texts

    else:
        print("Failed to retrieve data")

# Test the function
headlines = scrape_bbc_headlines()
if headlines:
    for idx, headline in enumerate(headlines, start=1):
        print(f"Headline {idx}: {headline}")
else:
    print("No headlines found")


# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the scraping function to run every hour (you can change the interval as needed)
scheduler.add_job(scrape_bbc_headlines, 'interval', hours=1)

try:
    # Start the scheduler
    scheduler.start()
except KeyboardInterrupt:
    # If you want to stop the scheduler manually (Ctrl+C)
    pass
