import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import streamlit as st

# 1. 네이버 뉴스 페이지 크롤링
def get_news_item(url) :
    res = req.get(url)
    soup = bs(res.text, "html.parser")

    date = soup.select_one("span.media_end_head_info_datestamp_time")["data-date-time"]
    title = soup.select_one("h2#title_area").text
    media = soup.select_one("a.media_end_head_top_logo > img")["title"]
    content = soup.select_one("div.newsct_article").text.replace("\n", "")

    return (date, title, media, content)

# 2. 뉴스 검색, 뉴스 리스트 수집
def get_news(search, ds, de) :
    page = 1
    result = []

    while True :
        start = (page - 1) * 10 + 1
        url = f"https://s.search.naver.com/p/newssearch/search.naver?de={de}&ds={ds}&eid=&field=0&force_original=&is_dts=0&is_sug_officeid=0&mynews=0&news_office_checked=&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22finance%22%7D%7D%7D&nso=%26nso%3Dso%3Add%2Cp%3Afrom{ds.replace('.', '')}to{de.replace('.', '')}%2Ca%3Aall&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&office_category=0&office_section_code=0&office_type=0&pd=3&photo=0&query={search}&query_original=&service_area=0&sort=1&spq=0&start={start}&where=news_tab_api&nso=so:dd,p:from{ds.replace('.', '')}to{de.replace('.', '')},a:all"
        res = req.get(url) # 결과가 json 형태로 출력
        doc = eval(res.text.replace("\n", ""))

        if len(doc["contents"]) == 0 :
            break

        for lst in doc["contents"] :
            soup = bs(lst, "html.parser")
            a_tags = soup.select("div.info_group > a")
            if len(a_tags) == 2 : # 네이버 뉴스가 있음
                try :
                    result.append(get_news_item(a_tags[-1]["href"])) # 마지막 a 태그의 "href"가 네이버 뉴스의 url
                except Exception as e :
                    print("오류 : ", e)
        page += 1
    return pd.DataFrame(columns = ["date", "title", "media", "content"], data = result)

# 3. streamlit 출력
st.title("네이버 뉴스 크롤러")
with st.sidebar :
    search = st.text_input("키워드", value = "", placeholder = "검색어 입력")
    ds = st.date_input("조회 시작일", pd.to_datetime("2024-06-29"))
    de = st.date_input("조회 종료일", pd.to_datetime("2024-06-30"))

if search and ds and de :
    df = get_news(search, ds.strftime("%Y.%m.%d"), de.strftime("%Y.%m.%d"))
    st.dataframe(df)