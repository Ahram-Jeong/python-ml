import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.title("주식 차트")

col1, col2, col3 = st.columns(3)
stock = col1.text_input("종목코드", "005930") # 005930 : 삼성전자
ds = col2.date_input("조회 시작일", pd.to_datetime("2023-01-01"))
de = col3.date_input("조회 종료일", pd.to_datetime("2024-01-01"))

def get_stock(stock, ds, de) :
    return yf.download(stock, ds, de)

result = get_stock(stock + ".KS", ds, de)

chart = plt.figure(figsize = (20, 10))
plt.rc("font", family = "NanumGothic", size = 13)
plt.rcParams["axes.unicode_minus"] = False
plt.plot(result.index, result["Adj Close"], label = "종가")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.title("일별 시세 변동 그래프")
st.pyplot(chart)

st.dataframe(result)