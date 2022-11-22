from PIL import Image, ImageFont, ImageDraw,ImageFilter
# 从PIL库引入创建验证码用到的各模块。
# Image用于创建图片对象，相当于创建一个画板，是第1步；
# ImageDraw用于针对Image对象进行绘画，可用text将文字画上去，用line将线条画上去；
# ImageFont用于在将文字画上去时使用的字体。
# ImageFilter用于为图片加滤镜。
import random
# random模块用于随机取数，如取随机取字符，随机取颜色
def getColor():
    """
    利用random.randint返回三组0至255之间的整数，形成RGB颜色代码。
    """
    return random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)

def creatVerificationCode(length):
    """
    验证码主函数，length为所创建验证码的长度
    """
    # 设置验证码图片的宽和高
    width = 120
    height = 30
    # 创建image,下面的(255, 255, 255)为背景颜色，可用getColor()函数替代，以实现背景颜色随机
    verificationImage = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Draw对象:
    drawImage = ImageDraw.Draw(verificationImage)
    # 采用Arial字体，将字体复制到static文件夹中可以直接使用。20号
    textFont = ImageFont.truetype("static/font/Verdana-1.ttf", 20)
    # 验证码的基本字符串，即只从这些字符中产生验证码
    verBaseChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    # 从上面基本字符串中随机选length指定长度个字符
    verChar = "".join(random.sample(verBaseChar,length))
    # 为每个验证码字符串生成不同位置，黑色
    for i in range(len(verChar)):
        # 字符位置为左：17*1+6，即隔6显示一个字符，上为2-8之间随机，字体为Arial,黑色（可用getColor())替换为随机颜色
        drawImage.text((17 * i + 6, random.randrange(2,8)), verChar[i], font=textFont, fill=(0,0,0))
    # 画2条干扰线，每条线X点从左到右（0-120），Y点在0-30之间随机产生，颜色随机。如需多条线可循环产生
    drawImage.line((0,random.randrange(0,30),120,random.randrange(0,30)),fill=getColor())
    drawImage.line((0,random.randrange(0,30),120,random.randrange(0,30)),fill=getColor())
    # 为验证码图片增加滤镜，本例中未使用，注释掉
    # verificationImage = verificationImage.filter(ImageFilter.DETAIL)
    # 将上面的各种方法生成的验证码对象保存为指定的文件名。测试用，成功后注释
    # verificationImage.save('code.png', 'png')
    # 返回生成的图片和使用的验证码字符
    return verificationImage,verChar