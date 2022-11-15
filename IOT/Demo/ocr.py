import tesserocr
from PIL import Image
# 读取图片
im = Image.open('123.png')
# 识别文字
string = tesserocr.image_to_text(im)
print(string)
print(tesserocr.file_to_text('123.png'))
