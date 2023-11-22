import streamlit as st
import habachen
import unicodedata

def main():
    # ページ設定
    st.set_page_config(
        page_title="全角・半角変換ツール - Streamlit",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items={
            "About": "### 全角・半角変換ツール (beta)"
        }   
    )

    # 概要説明
    st.title("全角・半角変換ツール")
    st.write("半角と全角の相互変換とUnicode正規化に対応しています。")

    # テキスト入力
    input_text = st.text_area("テキストを入力してください：")

    # 変換種別
    option1 = st.radio(
        "変換種別",
        ["全角に変換", "半角に変換", "正規化"],
        horizontal=True,
        label_visibility="collapsed"
    )

    if option1 == "正規化":
        # 正規化形式
        option2 = st.selectbox(
            "正規化形式を選択してください：",
            ["NFD", "NFC", "NFKD", "NFKC"],
            index = 3
        )
        
        # 正規化
        result = unicodedata.normalize(option2, input_text)

    else:
        # 変換対象プルダウン
        options_target = st.multiselect(
            "変換対象を選択してください：",
            ['仮名', '記号', '数字'],
            ['仮名', '記号', '数字'])

        # オプションの選択状況をbool型で保持
        option_kana = "仮名" in options_target
        option_ascii = "記号" in options_target
        option_digit = "数字" in options_target

        match option1:
            case "全角に変換":
                # 全角に変換
                result = habachen.han_to_zen(input_text, kana=option_kana, digit=option_digit, ascii=option_ascii)

            case "半角に変換":
                # 半角に変換
                result = habachen.zen_to_han(habachen.to_katakana(input_text), kana=option_kana, digit=option_digit, ascii=option_ascii)

    if result:
         # 結果を表示
        st.markdown("***")
        st.markdown("#### 結果")
        st.code(result, language="csv")    # プレーンテキストに近い言語形式

if __name__ == "__main__":
    main()
