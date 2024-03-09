import streamlit as st
import budoux

# budoux読み込み
parser = budoux.load_default_japanese_parser()

def main():
    # ページ設定
    st.set_page_config(
        page_title="ツール集",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items={
            "About": "### ツール集 (beta)"
        }
    )
    
    st.title("ようこそ！")
    st.write(f'{parser.translate_html_string("以下が、現時点で作成したツールです。（鋭意製作中…）")}', unsafe_allow_html=True)
    st.markdown("***")
    
    # introduction of each page
    if st.button("StrConv Tool", type="primary"):
        st.switch_page("pages/1_↔️_StrConv.py")
    st.write(f'{parser.translate_html_string("全角・半角文字の相互変換や、Unicode正規化を行うことができます。")}', unsafe_allow_html=True)
    
    st.markdown("***")
    if st.button("StrCount Tool",type="primary"):
        st.switch_page("pages/2_📝_StrCount.py")
    st.write(f'{parser.translate_html_string("文章の文字数をチェックできます。")}', unsafe_allow_html=True)
    
    st.markdown("***")
    if st.button("QRCreate Tool",type="primary"):
        st.switch_page("pages/3_📎_QRCreate.py")
    st.write(f'{parser.translate_html_string("URL等の文字列をQRコードに変換できます。")}', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
