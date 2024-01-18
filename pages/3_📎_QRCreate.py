import streamlit as st
import qrcode
from PIL import Image

# Title
st.title('QRコード生成ツール')

# Input
URL = st.text_input('変換URL入力', 
                    help="URLじゃなくてもOK！", 
                    placeholder="ここに QRコード化したい文字列を入力！ 例: https://various-tools-ja.streamlit.app/"
                    )
fill_color = "whitesmoke"

# Default
if URL == "":
    URL = "https://various-tools-ja.streamlit.app/"
    fill_color = "dimgray"

# Slidebar of Resizing
size = st.slider('Resize', 3, 20, 10)

# Create QR
qr = qrcode.QRCode(box_size = size)
qr.add_data(URL)
_img = qr.make_image(fill_color=fill_color, back_color="TransParent")  # TransParent: 背景透過
_img.save('qrcode.png')
img = Image.open('qrcode.png')
st.image(img)
