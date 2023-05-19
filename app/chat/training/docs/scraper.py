import requests
from bs4 import BeautifulSoup

url = 'https://ipoint.uwa.edu.au/app/answers/list/st/5/page/2'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

questionBox = soup.find_all('div', {'id': 'rn_Multiline_12_Content'})

for question in questionBox:
    questions = question.find_all('h3')
    for q in questions:
        faqs = {
        'question': q.text.strip(),
        'link': 'https://ipoint.uwa.edu.au/' + q.find('a')['href']
        }
        print(faqs)


