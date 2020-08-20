
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("https://wenku.baidu.com/view/2d2f8384a0116c175f0e48fb.html")
    print(response)
    html = response.read()
    charset = chardet.detect(html)#对该html进行编码的获取
    print(charset) #打印编码格式

