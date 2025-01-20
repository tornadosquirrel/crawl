import requests
from bs4 import BeautifulSoup
import random
import re

# 크롤링할 URL
url = 'https://ko.wikipedia.org/wiki/파이썬'

# 웹 페이지 요청
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 텍스트 추출
paragraphs = soup.find_all('p')
text = ' '.join([para.get_text() for para in paragraphs])

# 텍스트 전처리: 문장 단위로 분리 및 불필요한 공백 제거
sentences = re.split('。|！|？', text)  # 문장 단위로 분리
sentences = [s.strip() for s in sentences if s]

# 단어 리스트 생성
nouns = []
for sentence in sentences:
    nouns += re.findall(r'\b\w+\b', sentence)  # 각 문장에서 단어 추출

# 한국어 문장 생성 함수
def generate_korean_sentence():
    if len(nouns) < 5:  # 최소 5개 단어가 있어야 문장 생성
        return "문장을 생성할 수 없습니다."
    
    # 무작위로 단어 선택
    modifier1 = random.choice(nouns)  # 관형어
    subject = random.choice(nouns)     # 주어
    modifier2 = random.choice(nouns)   # 관형어
    object_ = random.choice(nouns)     # 목적어
    adverbial = random.choice(nouns)    # 부사어
    predicate = random.choice(nouns)    # 서술어

    return f"{modifier1} {subject} {modifier2} {object_} {adverbial} {predicate}."

# 메인 함수
if __name__ == "__main__":
    sentence = generate_korean_sentence()
    print(sentence)