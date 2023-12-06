import streamlit as st
import budoux

# budoux読み込み
parser = budoux.load_default_japanese_parser()

def main():
    # ページ設定
    st.set_page_config(
        page_title="便利ツール集 - Streamlit",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items={
            "About": "### 便利ツール集 (beta)"
        }
    )

    st.title("ようこそ！")
    st.write("鋭意製作中です…")
    st.write(f'{parser.translate_html_string("現時点で作成したツールは、左のサイドメニューから移動できます。")}', unsafe_allow_html=True)

    st.markdown("""
        ***
        #### StrConv
            全角・半角文字の相互変換や、Unicode正規化が行えるツールです。
        ***
        #### StrCount
            文章の文字数をチェックできるツールです。
    """)

if __name__ == "__main__":
    main()
