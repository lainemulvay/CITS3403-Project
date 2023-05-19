import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

faqList = []

def getFAQs(identifier):
    url = f'https://ipoint.uwa.edu.au/app/answers/detail/a_id/{identifier}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        faq = {
            'question': soup.select('#rn_PageContent #ans_desc')[0].text.strip(),
            'answer': soup.select('#rn_AnswerText')[0].text.strip()
        }
        faqList.append(faq)
        print(f"Added Answer ID {identifier}")
    except IndexError:
        print(f"Skipping Answer ID {identifier} - Page not found")

for x in range(1283, 1290):
    getFAQs(x)

df = pd.DataFrame(faqList)
df.to_csv('faq.csv', index=False, quoting=csv.QUOTE_ALL)
print(df.head())