import requests as req
from bs4 import BeautifulSoup as bs

git_user = input("Github Username :")
url = f"https://github.com/{git_user}"
response = req.get(url)
soup = bs(response.content, 'html.parser')
linkedin_profile = soup.find('a', attrs={'rel' : 'nofollow me'})['href']
profile_img = soup.find('img', {'class' : 'avatar avatar-user width-full border color-bg-default'})['src']
print(linkedin_profile)
print(profile_img)
