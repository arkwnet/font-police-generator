import os
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from dotenv import load_dotenv
load_dotenv()

font_list = [
    ["meiryob.ttc", "MeiryoBold", 10, -11, 0],
    ["meiryo.ttc", "Meiryo", 9, -11, 0],
    ["msgothic.ttc", "MSGothic", 6, 9, 0],
    ["msmincho.ttc", "MSMincho", 7, 9, 0],
    ["BIZ-UDGothicR.ttc", "BIZUDGothic", 9, 10, 0],
    ["BIZ-UDGothicB.ttc", "BIZUDGothicBold", 9, 10, 0],
    ["BIZ-UDMinchoM.ttc", "BIZUDMinchoMedium", 9, 8, 0],
    ["YuGothL.ttc", "YuGothicLight", 9, 8, 0],
    ["YuGothR.ttc", "YuGothic", 9, 8, 0],
    ["YuGothM.ttc", "YuGothicMedium", 9, 8, 0],
    ["YuGothB.ttc", "YuGothicBold", 9, 8, 0],
    ["yuminl.ttf", "YuMinchoLight", 9, 9, 0],
    ["yumin.ttf", "YuMincho", 9, 9, 0],
    ["yumindb.ttf", "YuMinchoDemiBold", 9, 9, 0],
    ["UDDigiKyokashoN-R.ttc", "UDDigiKyokashoRegular", 7, 8, 0],
    ["UDDigiKyokashoN-B.ttc", "UDDigiKyokashoBold", 7, 8, 0],
    ["WIX-UDKakugo_LargePr6N-M.otf", "UDKakugoLargeM", 8, 8, 1],
    ["WIX-UDKakugo_LargePr6N-DB.otf", "UDKakugoLargeDB", 8, 8, 1],
    ["WIX-RodinProN-DB.otf", "RodinDB", 8, 8, 1],
    ["NotoSansJP-Thin.otf", "NotoSansJPThin", 8, -23, 1],
    ["NotoSansJP-Light.otf", "NotoSansJPLight", 8, -23, 1],
    ["NotoSansJP-Regular.otf", "NotoSansJPRegular", 8, -23, 1],
    ["NotoSansJP-Medium.otf", "NotoSansJPRegular", 8, -23, 1],
    ["NotoSansJP-Bold.otf", "NotoSansJPRegular", 8, -23, 1],
    ["NotoSansJP-Black.otf", "NotoSansJPBlack", 8, -23, 1],
]

print("Loading data_kanji")
f = open("data_kanji.txt", "r", encoding = "UTF-8")
data_kanji = f.read()
f.close()

print("Loading data_other")
f = open("data_other.txt", "r", encoding = "UTF-8")
data_other = f.read()
f.close()

data_all = data_kanji + data_other
data_len = len(data_all)
print(data_len)

fontsize = 110
canvasSize = (128, 128)
backgroundRGB = (255, 255, 255)
textRGB = (0, 0, 0)

for i in range(len(font_list)):
    if font_list[i][4] == 0:
        ttfontname = "C:\\Windows\\Fonts\\" + font_list[i][0]
    else:
        ttfontname = "C:\\Users\\" + os.getenv("USER_NAME") + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\" + font_list[i][0]
    if (os.path.exists("images\\" + font_list[i][1]) == False):
        os.mkdir("images\\" + font_list[i][1])
    for j in range(int(data_len)):
        text = data_all[j : j + 1]
        img = PIL.Image.new("RGB", canvasSize, backgroundRGB)
        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font = font)
        textTopLeft = (font_list[i][2], font_list[i][3])
        draw.text(textTopLeft, text, fill = textRGB, font = font)
        filename = "images\\" + font_list[i][1] + "\\" + str(j).zfill(4) + ".png"
        img.save(filename)
        print(filename)
