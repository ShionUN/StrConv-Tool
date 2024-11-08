import streamlit as st
import qrcode
from PIL import Image

# Title
col1, col2 = st.columns([5, 1])
col1.title('QRコード生成ツール')
col2.page_link("Home.py", label="Home", icon="🔙")

# Input
URL = st.text_area('Input', 
                    help="URLじゃなくてもOK！", 
                    placeholder="ここにURL等を入力！\n例: https://various-tools-ja.streamlit.app/",
                    label_visibility="collapsed")
fill_color = "whitesmoke"

# Default
if URL == "":
    URL = "https://various-tools-ja.streamlit.app/"
    fill_color = "dimgray"

# Style
st.html(
    """
    <style>
        div[data-testid=stSlider] > * {
            display: block;
            margin: 0 auto;
            width: 50%;
        }

        div[data-testid=stFullScreenFrame] > * {
            display: block;
            margin: 0 auto;
        }
        
        div[data-testid=stDownloadButton] button {
            display: block;
            margin: 0 auto;
        }
    </style>
    """
)

# Slidebar of Resizing
size = st.slider('サイズ調整', 3, 20, 6)

# Create QR
qr = qrcode.QRCode(box_size = size)
qr.add_data(URL)
_img = qr.make_image(fill_color=fill_color, back_color="TransParent")  # TransParent: 背景透過
_img.save('qrcode.png')
img = Image.open('qrcode.png')
st.image(img)

# Download button of QR image
with open("qrcode.png", "rb") as file:
    btn = st.download_button(
            label="画像として保存",
            data=file,
            file_name="qrcode.png",
            mime="image/png"
          )