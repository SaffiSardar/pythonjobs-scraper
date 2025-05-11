import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find("section" , class_="job_list")

python_jobs = results.find_all("a" , string=lambda text:"python" in text.lower())

python_jobs_cards = [a_element.parent.parent for a_element in python_jobs]

for job_card in python_jobs_cards:
    title_element = job_card.find_all("a")[1]
    location_element = job_card.find_all("span",class_="info")[0]
    company_element = job_card.find_all("span",class_="info")[3]
    link_url = job_card.find("a",class_="go_button")["href"]
    
    print()
    print(title_element.text.strip())
    print(location_element.text.strip())
    print(company_element.text.strip())
    link_concat = "https://pythonjobs.github.io"+link_url
    print(link_concat)
    