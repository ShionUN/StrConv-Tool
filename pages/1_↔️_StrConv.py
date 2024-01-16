import streamlit as st
import budoux
import habachen
import unicodedata

# budoux読み込み
parser = budoux.load_default_japanese_parser()

# 概要説明
st.title("全角・半角変換ツール")
st.write(f'{parser.translate_html_string("半角と全角の相互変換とUnicode正規化に対応しています。")}', unsafe_allow_html=True)

# テキスト入力
input_text = st.text_area(
    "テキストを入力してください：",
    height=95,
    placeholder="ここにテキストを入力…",
    label_visibility="collapsed"
)

# 目的タブ
tab1, tab2, tab3 = st.tabs(["全角に変換", "半角に変換", "正規化"])

target_list = ['仮名', '記号', '数字']

# セッション情報初期化
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = target_list

# 変換対象プルダウン（全角に変換）
options_target1 = tab1.multiselect(
    "変換対象を選択してください：",
    target_list,
    default=st.session_state.selected_option if all(option in target_list for option in st.session_state.selected_option) else None,
    key="options_target1"
)
# 選択内容が変更されたらsession_stateの値を更新（同期）
if options_target1 != st.session_state.selected_option:
    st.session_state.selected_option = options_target1
    st.rerun()

# 変換対象プルダウン（半角に変換）
options_target2 = tab2.multiselect(
    "変換対象を選択してください：",
    target_list,
    default=st.session_state.selected_option if all(option in target_list for option in st.session_state.selected_option) else None,
    key="options_target2",
    help="「仮名」を選択した場合、ひらがなは半角カナに変換されます。"
)
# 選択内容が変更されたらsession_stateの値を更新（同期）
if options_target2 != st.session_state.selected_option:
    st.session_state.selected_option = options_target2
    st.rerun()

# オプションの選択状況をbool型で保持
option_kana1 = "仮名" in options_target1
option_ascii1 = "記号" in options_target1
option_digit1 = "数字" in options_target1

# オプションの選択状況をbool型で保持
option_kana2 = "仮名" in options_target2
option_ascii2 = "記号" in options_target2
option_digit2 = "数字" in options_target2

# 正規化形式選択プルダウン
option_norm = tab3.selectbox(
        "正規化形式を選択してください：",
        ["NFD", "NFC", "NFKD", "NFKC"],
        index = 3
)

# １．全角に変換
result1 = habachen.han_to_zen(input_text, kana=option_kana1, digit=option_digit1, ascii=option_ascii1)
if result1:
    # 結果を表示
    tab1.markdown("***")
    tab1.markdown("#### 結果")
    tab1.code(result1, language=None)

# ２．半角に変換
result2 = habachen.zen_to_han(habachen.to_katakana(input_text), kana=option_kana2, digit=option_digit2, ascii=option_ascii2)
if result2:
    # 結果を表示
    tab2.markdown("***")
    tab2.markdown("#### 結果")
    tab2.code(result2, language=None)

# ３．正規化
result3 = unicodedata.normalize(option_norm, input_text)
if result3:
    # 結果を表示
    tab3.markdown("***")
    tab3.markdown("#### 結果")
    tab3.code(result3, language=None)
