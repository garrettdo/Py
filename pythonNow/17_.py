# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

# 引入Pillow
from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-30, 0), '1', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('avatar.png')
    img = img.convert('RGB')
    img = img.resize((90, 90), Image.ANTIALIAS)
    img.save('xyz.jpg')
    add_num(image)


# # 从PIL库导入所需模块
# from PIL import Image,ImageFont,ImageDraw
# import sys
# # 必须要reload
# reload(sys)
# # 字符编码改为utf8
# sys.setdefaultencoding('utf-8')
#
# # 头像图片路径 D:\文档\Garrett\03my\Py\Resource Library\images
# headPath=r"D:\\文档\\Garrett\\03my\\Py\\Resource Library\\images\\"
# # 处理后输出路径 D:\文档\Garrett\03my\Py\Resource Library\images
# outputPath=r"D:\\文档\\Garrett\\03my\\Py\\Resource Library\\images\\"
# # 字体路径
# fontPath=r"C:\\Windows\\Fonts\\"
# # 头像文件
# headFile="head.jpg"
# # 输出文件
# outFile="output.jpg"
# # 打开图片，建立画布
# image=Image.open(headPath+headFile,'r')
# draw=ImageDraw.Draw(image)
#
# # 由图片大小确定字体大小
# fontsize=min(image.size)/4
#
# # 增加文字
# # 实例字体对象
# fontobj=ImageFont.truetype(font=fontPath+"AdobeHeitiStd-Regular.otf",size=fontsize,index=0,encoding='',filename=None)
# # 用draw对象的text()方法添加文字
# draw.text((image.size[0]-fontsize,0),text="5",fill=(255,0,0),font=fontobj,anchor=None)
# # 保存图片
# image.save(outputPath+outFile)

