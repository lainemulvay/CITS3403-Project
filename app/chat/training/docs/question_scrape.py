import requests
from bs4 import BeautifulSoup

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

for x in range(1283, 1300):
    getFAQs(x)

print(len(faqList))
print(faqList)




  # Replace 
    #     answerContainer = soup2.find_all('div', {'id': 'rn_AnswerText'})


    #     faqs = {
    #     'question': q.text.strip(),
    #     'link': 'https://ipoint.uwa.edu.au/' + q.find('a')['href']
    #     }
    #     faqList.append(faqs)


    #     r2 = requests.get(link, headers=headers)
    #     soup2 = BeautifulSoup(r2.text, 'html.parser')
    #     answerContainer = soup2.find_all('div', {'id': 'rn_AnswerText'})
    #     print(answerContainer)

    #     answer = []
    #     answer.extend(answerContainer.find_all(lambda tag: tag.name in ['p', 'ul', 'ol']))
    #     print(answer)

    #     for paragraph in questionAnswer:
    #         paragraphs = paragraph.find_all('p')
    #         for p in paragraphs:
    #             answer += p.text.strip()

    #     faqList.append({'question': question_text, 'answer': answer})

    # return
    
# for x in range (1283, 1284):
#     getFAQs(x)

# print(len(faqList))