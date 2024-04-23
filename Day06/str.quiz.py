#1. 뉴스 기사를 스크랩 해오고,
#유저가 입력한 단어를 기사에서 그 해당 단어를 대문자화 시켜서
# 다시 보여주기.

news = """students protest furries · octapharma plasma ransomware attack · lyrids meteor · erivan haub death · kentucky"""
word =input("단어 입력")
newnews= news.replace(word,word.upper())
print(newnews)

#2. 영어 기사를 스크랩해오고,
#단어 사이에 토 넣고 출력하기

words = news.split """students protest furries · octapharma plasma ransomware attack · lyrids meteor · erivan haub death · kentucky"""
news1 ="😒".join(words)
print(news1)