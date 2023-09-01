import requests
from bs4 import BeautifulSoup as bs

# Prompts user input for Github username and creates url for Github profile
github_user = input('Input Github user: ')
url = 'https://github.com/' +github_user
r = requests.get(url)

# Parse the HTML content
soup = bs (r.content, 'html.parser')

# Find the profile image element in the HTML using its 'alt' attribute value
# This assumes that the alt attribute of the image tag is set to 'Avatar' in GitHub profiles
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image )
