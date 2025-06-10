import streamlit as st
st.title("나의 첫 app")
st.write("hello")
name=st.text_inout("이름 입력")
if name:
   if name=="박서준"
     st.success("반갑습니다. 박서준님!")
else:
     st.warning("누구세요?")
