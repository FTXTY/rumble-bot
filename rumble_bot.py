from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from fake_useragent import UserAgent

# Function to configure and launch the browser with proxy and user-agent
def configure_browser(proxy=None):
    options = webdriver.ChromeOptions()
    
    # Configure proxy
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    
    # Configure user-agent
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    
    # Enable headless mode for stealth
    options.add_argument('--headless')
    
    # Disable WebDriver detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    # Additional stealth settings
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-infobars')
    
    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Function to simulate watching a video
def watch_video(url, proxy=None):
    driver = configure_browser(proxy)
    driver.get(url)
    
    try:
        # Find the video container and click anywhere on it to start the video
        video_container = driver.find_element(By.CSS_SELECTOR, "div.bigPlayUI")  # Adjust selector if necessary
        video_container.click()
        print(f"Playing video: {url}")
        
        # Randomly scroll the page to simulate user activity
        for _ in range(random.randint(1, 3)):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(random.uniform(2, 5))
        
        # Simulate a random viewing time
        view_time = random.uniform(60, 180)  # Watch between 1 to 3 minutes
        time.sleep(view_time)
        print(f"Watched for {view_time} seconds")
    
    except Exception as e:
        print(f"Error watching video: {e}")
    
    finally:
        driver.quit()

# Function to load proxies from the proxies.txt file
def load_proxies(filename='proxies.txt'):
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

# List of video URLs
video_urls = [
    "https://rumble.com/v56qs3p-nosirwellidontwantobetheblameanymore.html",
    "https://rumble.com/v4f0ign-tryingtopassthislittlefuck.html"
]

# Load proxies from the file
proxies = load_proxies()

# Simulate views on each video
for url in video_urls:
    proxy = random.choice(proxies)  # Rotate proxies
    watch_video(url, proxy)
    time.sleep(random.uniform(10, 20))  # Pause between videos to simulate real browsing