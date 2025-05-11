import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find("section" , class_="job_list")

python_jobs = results.find_all("a" , string=lambda text:"python" in text.lower())

