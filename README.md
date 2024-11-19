# Pararius Web Scraper

Are you tired of endlessly searching for a house in the Netherlands? Does it feel like every house has 40+ reactions within the first hour of being posted? Are you constantly refreshing Pararius?  

This web scraper automates the process by sending an email whenever a new house that meets your requirements is listed. Simply schedule it as a recurring task on your computer, and it will check Pararius every 5 minutes for updates.

## How It Works
1. **Custom Search**: The scraper monitors houses based on your specified search criteria (defined in the Pararius URL).
2. **Data Tracking**: It saves the top 10 house listings from your search results into a CSV file.
3. **Change Detection**: On the next run, the scraper compares the new top 10 listings to the previously saved ones. If there are new houses, it identifies them as updates.
4. **Email Notification**: When a new listing is detected, an email is sent to your account with the details.

## Features
- Automatically refreshes Pararius every 5 minutes.
- Sends email alerts only when new houses are found.
- Lightweight and easy to schedule as a task on any system.
