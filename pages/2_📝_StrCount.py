import streamlit as st
import re

st.title("文字数カウントツール")

prompt = st.chat_input("テキストはこちらに！改行は Shift + Enter で！", max_chars=100000) # 指定可能最大値：4294967295 高負荷すぎるため上限設定
if prompt is None:
    prompt = ""

# 素の文字数
len_normal = len(prompt)
# 空白を除外した文字数
len_nonspace = len(re.sub(r"\s+", "", prompt))

if prompt:

    st.write("入力テキスト:")
    st.code(f" {prompt}", language=None)
    st.info(f"""
    ##### 現在
    - すべての文字数：**{len_normal}**
    - 空白以外　　　：**{len_nonspace}**
    """)
    if st.button("Rerun"):
        st.rerun()