import os
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from dotenv import load_dotenv
load_dotenv()

fontlist = [
    ["NotoSansJP-Regular.otf", "", 8, -23, 1]
]

if fontlist[0][4] == 0:
    ttfontname = "C:\\Windows\\Fonts\\" + fontlist[0][0]
else:
    ttfontname = "C:\\Users\\" + os.getenv("USER_NAME") + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\" + fontlist[0][0]

fontsize = 110
canvasSize = (128, 128)
backgroundRGB = (255, 255, 255)
textRGB = (0, 0, 0)

text = "あ"
img = PIL.Image.new("RGB", canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)
font = PIL.ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(text, font = font)
textTopLeft = (fontlist[0][2], fontlist[0][3])
draw.text(textTopLeft, text, fill = textRGB, font = font)
filename = "image.png"
img.save(filename)
