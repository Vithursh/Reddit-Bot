![](https://github.com/Vithursh/Reddit-Bot/blob/48b60179752880f75243ef5311341e5b7e31940e/Reddit-Bot.png)

## Description
---

The Reddit-Bot is an automated script designed to fetch the latest memes from the "memes" subreddit and send them via email on a weekly basis. This bot utilizes the [Reddit API] to access subreddit content and employs a scheduling mechanism to automate the process of downloading images and sending emails.

---

## Inspiration
---

The inspiration for creating this project came from the desire to automate the process of staying updated with the latest memes without manually browsing Reddit. The project combines the power of web scraping, automation, and email services to deliver content directly to users' inboxes, making it a convenient tool for meme enthusiasts.

## Table of Contents

- Components
- Features
- Installation

## Components

- #### Reddit API Integration
  - **PRAW ([Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/))**
    - Authenticates and interacts with Reddit to fetch the latest posts from the "memes" subreddit.
    - Utilizes environment variables for secure storage of API credentials.

- #### Image Downloader
  - **[Requests Library](https://requests.readthedocs.io/en/latest/)**
    - Downloads images from the subreddit posts.
    - Ensures images are stored locally before sending.

- #### Email Sender
  - **SMTP and Email Libraries**
    - Sends the downloaded images as email attachments.
    - Utilizes environment variables for secure email credentials.

- #### Scheduler
  - **[Schedule Library](https://pypi.org/project/schedule/)**
    - Automates the weekly execution of the bot to download and send memes.

## Features
---
- Automated weekly meme delivery
- Secure handling of API and email credentials using environment variables
- Simple setup and configuration

## Installation
---

#### Running locally

##### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- Reddit API credentials
- Email account credentials

1. Clone the repository:
   ```bash
   git clone https://github.com/Vithursh/Reddit-Bot.git

2. Navigate to the project directory:
   ```bash
   cd Reddit-Bot

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Set up environment variables:
   - Create a .env file in the project directory.
   - Add your Reddit API and email credentials to the .env file.

5. Run the bot:
   ```bash
   python src/Scraper.py
