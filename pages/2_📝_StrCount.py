import streamlit as st
import re

# Title
col1, col2 = st.columns([5, 1])
col1.title("文字数カウントツール")
col2.page_link("Home.py", label="Home", icon="🔙")

with st.container(height=500):
    
    # Input
    prompt = st.chat_input("ここに入力！", max_chars=100000) # 指定可能最大値：4294967295 高負荷すぎるため上限設定
    if prompt is None:
        prompt = ""
    
    # 素の文字数
    len_normal = len(prompt)
    # 空白・ラブ・改行を除外した文字数
    len_nonspace = len(re.sub(r"\s+", "", prompt))
    # 空白・タブ数
    cnt_space = len(re.findall(r"[ \t]", prompt))
    # 改行数
    cnt_newline = len(re.findall(r"[\n]", prompt))

    if prompt:
        st.info(f"""
        ##### 現在
        - すべての文字数：**{len_normal}**
        - 空白・改行以外：**{len_nonspace}** （空白数：**{cnt_space}**　改行数：**{cnt_newline}**）
        """)
        st.write("入力テキスト:")
        st.code(f" {prompt}", language=None)