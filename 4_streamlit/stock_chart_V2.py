import streamlit as st
import requests as req
import pandas as pd

st.title("주식 차트")

col1, col2, col3 = st.columns(3)
stock = col1.text_input("종목코드", "005930") # 005930 : 삼성전자
ds = col2.date_input("조회 시작일", pd.to_datetime("2023-01-01"))
de = col3.date_input("조회 종료일", pd.to_datetime("2024-01-01"))

def get_stock(stock, ds, de) :
    url = f"https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={stock}&requestType=1&startTime={ds}&endTime={de}&timeframe=day"
    res = req.get(url)
    li = eval(res.text.replace("\n", "").replace("\t", ""))
    return pd.DataFrame(columns = li[0], data = li[1:])

if stock and ds and de :
    df = get_stock(stock, ds.strftime("%Y%m%d"), de.strftime("%Y%m%d"))
    df = df.set_index("날짜")
    st.line_chart(df["종가"])
    st.bar_chart(df["거래량"])
    st.download_button(label = "Download", data = df.to_csv(index = False), file_name = f"{stock}.csv")
    st.dataframe(df)