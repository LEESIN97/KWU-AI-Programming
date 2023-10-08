from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import wordcloud
import matplotlib.pyplot as plt
import time


#크롬드라이버로 원하는 url 접속
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
url = input('URL 주소를 입력하시오 : ')
driver.get(url)
time.sleep(2)

#원하는 키워드 입력
search_box = driver.find_element(By.CSS_SELECTOR, '#query')
query = input('검색할 키워드를 입력하시오 : ')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

#뉴스 더보기 page에서 text 추출
more_news = driver.find_element(By.CSS_SELECTOR, '#main_pack > section.sc_new.sp_nnews._fe_news_collection._press_option_check_visible._prs_nws_all > div > div.api_more_wrap > a')
more_news.click()
news = [a.text for a in driver.find_elements(By.CSS_SELECTOR, '#main_pack > section > div > div.group_news > ul li a')]
hangul_filtered_news = [''.join(c for c in s if '\uAC00' <= c <= '\uD7A3' or c.isspace() or c in ".,?!") for s in news]
hangul_filtered_news_str = ' '.join(hangul_filtered_news)

#wordcloud 생성
s_words = wordcloud.STOPWORDS.union({'문서', '저장하기', '언론사', '선정', '언론사', '네이버뉴스', '궁금하다면', '바로가기'})
image = wordcloud.WordCloud(font_path= 'C:/WINDOWS/FONTS/MALGUNSL.TTF',width=1000, height = 700, stopwords= s_words).generate(hangul_filtered_news_str)

plt.figure(figsize= (40, 30))
plt.imshow(image)
plt.show()


