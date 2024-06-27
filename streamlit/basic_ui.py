import pandas as pd
import streamlit as st

# button
button = st.button("버튼을 눌러보세요👆")
if button :
    st.write(":blue[버튼]이 눌렸습니다:) :sparkles:")

# download button
# 샘플 데이터 생성
df = pd.DataFrame({
    "first column" : [1, 2, 3, 4],
    "second column" : [10, 20, 30, 40]
})
st.download_button("Download", data = df.to_csv(), file_name = "sample.csv")

# checkbox
agree = st.checkbox("동의하십니까?")
if agree :
    st.write("동의하셨습니다.")

# radio button
color = st.radio("좋아하는 색상은?", ("orange", "blue", "black", "white"))
if color :
    st.write(f"좋아하는 색상은 {color}이군요:-)")
    
# select box
num = st.selectbox("좋아하는 숫자는?", [1, 2, 3, 4, 5])
if num :
    st.write(f"좋아하는 숫자는 {num}이군요:-)")
# multi select
fruits = st.multiselect(f"좋아하는 과일은?", ["🍉", "🍒", "🍋", "🍇"], default = ["🍉", "🍋"])
if fruits :
    st.write(f"좋아하는 과일은 {fruits}이군요:-)")

# slider
range = st.slider("나이를 선택하세요.", 10, 100, (20, 30))
if range :
    st.write(f"나이는 {range}세 입니다.")
    
range = st.slider("나이를 선택하세요.", min_value = 10, max_value = 100)
if range :
    st.write(f"나이는 {range}세 입니다.")
    
# inputbox
# 텍스트
name = st.text_input("이름을 입력하세요.", "조승연")
if name :
    st.write(f"이름은 {name}입니다.")
# 숫자
num = st.number_input("숫자를 입력하세요.", 0, 100, 50)
if num :
    st.write(f"숫자는 {num}입니다.")
# 날짜
date = st.date_input("날짜를 선택하세요.", pd.to_datetime("2024-01-01"))
if date :
    st.write(f"날짜는 {date}입니다.")