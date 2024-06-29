import streamlit as st
import pandas as pd
import time

# 파일 업로드 버튼 생성
file = st.file_uploader("파일 선택 (csv or excel)", type = ["csv", "xls", "xlsx"])

time.sleep(3)

# 파일 확장자 분기 처리
if file is not None :
    ext = file.name.split(".")[-1]
    if ext == "csv" : # csv 파일
        df = pd.read_csv(file)
        st.dataframe(df)
    elif "xls" in ext : # 엑셀 파일
        df = pd.read_excel(file, engine = "openpyxl")
        st.dataframe(df)