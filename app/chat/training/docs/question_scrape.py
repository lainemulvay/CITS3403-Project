import requests
from bs4 import BeautifulSoup

faqList = []

def getFAQs(identifier):
    url = f'https://ipoint.uwa.edu.au/app/answers/detail/a_id/{identifier}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # questionBox = soup.select('#rn_PageContent #ans_desc')
    # for element in questionBox:
    question = soup.select('#rn_PageContent #ans_desc')[0].text.strip()
    print(question)
    answer = soup.select('#rn_PageContent #ans_desc')


getFAQs(1283)  # Replace 1234 with the actual identifier






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