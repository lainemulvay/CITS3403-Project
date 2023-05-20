import requests
from bs4 import BeautifulSoup

faqList = []

# def getFAQs(page):
url = f'https://ipoint.uwa.edu.au/app/answers/list/st/5/page/2'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
questionContainer = soup.find_all('div', {'id': 'rn_Multiline_12_Content'})

for question in questionContainer:
    questions = question.find_all('h3')
    for q in questions:
        question_text = q.text.strip()
        link = 'https://ipoint.uwa.edu.au/' + q.find('a')['href']
        print(link)

        # answer = ''

        # r2 = requests.get(link, headers=headers)
        # soup2 = BeautifulSoup(r2.text, 'html.parser')
        # answerContainer = soup2.find_all('div', {'id': 'rn_AnswerText'})
        # print(answerContainer)

        # answer = []
        # answer.extend(answerContainer.find_all(lambda tag: tag.name in ['p', 'ul', 'ol']))
        # print(answer)

#         for paragraph in questionAnswer:
#             paragraphs = paragraph.find_all('p')
#             for p in paragraphs:
#                 answer += p.text.strip()

#         faqList.append({'question': question_text, 'answer': answer})

# # Print the FAQs
# for faq in faqList:
#     print('Question:', faq['question'])
#     print('Answer:', faq['answer'])
#     print('------------------')

        # faqs = {
        #     'question': question,
        #     'answer': answer
        # }
        # faqList.append(faqs)

    # return
    
# for x in range (1, 2):
#     getFAQs(x)

# print(len(faqList))
