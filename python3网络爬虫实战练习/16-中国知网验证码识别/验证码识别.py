import tesserocr
from PIL import Image


#当识别得到验证码结果和实际图片内容有差异时，可以试着将图片处理一下，比如转灰度值，二值化，此外，还可以指定二值化的阈值

# image=Image.open('code.jpg')
# result=tesserort.image_to_text(image)
# print(result)

#直接将图片转化为文字
# print(tesserocr.file_to_text('code.png'))

#若图片内容转化有差异，可做如下处理
# image=Image.open('code.jpg')
# image=image.convert('L')      #将图片转化为灰度图像
# image.show()
# image=image.convert('1')
# image.show()     #将图片进行二值化处理

image=Image.convert('L')
threshold=80    #设置二值化阈值
table=[]
for i in range(256):
    if i<threshold:
        table.append(o)
    else:
        table.append(1)

image=image.point(table,'1')
image.show()      #将原来验证码中杂乱的线条去掉，使整个验证码变得黑白分明，再尝试重新识别验证码