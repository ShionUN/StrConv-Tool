import streamlit as st
import jaconv

def main():
    st.title("全角・半角変換ツール")
    st.write("半角文字を全角文字に、または全角文字を半角文字に変換します。")

    # テキスト入力
    input_text = st.text_area("テキストを入力してください:")

    # 変換方向
    option1 = st.radio(
        "変換方向",
        ('全角に変換', '半角に変換'),
        horizontal=True,
        label_visibility="collapsed"
    )

    # 変換対象
    option2= st.radio(
        "変換対象👇",
        ('ぜんぶ', '仮名・記号', '仮名だけ'),
        horizontal=True
    )


    # 全角に変換
    if option1 == '全角に変換': 
        match option2:
            case 'ぜんぶ':
                result = jaconv.h2z(input_text, kana=True, digit=True, ascii=True)
            case '仮名・記号':
                result = jaconv.h2z(input_text, kana=True, digit=False, ascii=True)
            case '仮名だけ':
                result = jaconv.h2z(input_text, kana=True, digit=False, ascii=False)

    # 半角に変換
    if option1 == '半角に変換':
        match option2:
            case 'ぜんぶ':
                result = jaconv.z2h(jaconv.hira2kata(input_text), kana=True, digit=True, ascii=True)
            case '仮名・記号':
                result = jaconv.z2h(jaconv.hira2kata(input_text), kana=True, digit=False, ascii=True)
            case '仮名だけ':
                result = jaconv.z2h(jaconv.hira2kata(input_text), kana=True, digit=False, ascii=False)

    # 結果を表示
    st.write("変換結果:")
    st.code(result, language="csv")    # プレーンテキストに近い言語形式

if __name__ == "__main__":
    main()
