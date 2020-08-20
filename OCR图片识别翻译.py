import os
import time
import pyperclip
from aip import AipOcr
import hashlib
import json
import random
import requests


def init():

    """OCR Servlet"""
    global url, appid, secretKey, salt
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    appid = '20200709000515966'
    secretKey = 'zkBZZvSCzzIILP96StRh'
    salt = random.randint(32768, 65536)

    """Translate Servlet"""
    APP_ID = "21197258"
    API_KEY = "2nh0SuB0Z1zbZFtR6mfATYVb"
    SECRET_KEY = "rwXvvdP1iufWGhWGWFfwp0oSPE2gDTfN"

    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return aipOcr


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def result_(filePath, options):
    result = ""
    try:
        data = aipOcr.basicGeneral(get_file_content(filePath), options)
    except:
        raise ConnectionError("网络连接异常！")
    words_result = data['words_result']
    for i in range(len(words_result)):
        result += words_result[i]['words']
    return result


def translate_(q):
    """auto自动识别语种"""
    # 生成签名
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    # post请求参数
    data = {
        "appid": appid,
        "q": q,
        "from": fromLang,
        "to": toLang,
        "salt": str(salt),
        "sign": sign,
    }
    # 返回时一个json
    trans_result = json.loads(requests.post(url, data=data).content).get('trans_result')[0].get("dst")
    return trans_result


if __name__ == '__main__':

    """Default"""
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    """存放要识别照片的目录"""
    fileDir = r"/Users/jeffrey/screen"

    """检查的文件类型"""
    fileType = ["png", "jpg", "bmp"]

    """是否翻译"""
    translate = True

    """翻译或运行失败后是否声音提示，一声为成功，两声为失败"""
    sound_success = True
    sound_failed = True

    """翻译语种，auto 为自动识别"""
    fromLang = 'auto'
    toLang = 'auto'

    """刷新间隔秒数"""
    waitTime = 2

    """获取指定目录下的文件，第一次运行不会处理这些文件"""
    oldPhotoList = os.listdir(fileDir)
    print("脚本已启动")
    while True:
        time.sleep(waitTime)
        try:
            newPhotoList = os.listdir(fileDir)
            """利用set集合不可重复性获取不一致的信息"""
            diffList = list((set(oldPhotoList) ^ set(newPhotoList)))
            if len(diffList) >= 1:
                for i in diffList:
                    oldPhotoList.append(i)
                    diffList.remove(i)
                    target = fileDir + os.sep + i
                    if not os.path.exists(target):
                        print("文件不存在" + str(len(diffList)))
                        print("\a\a")
                        continue
                    if os.path.splitext(target)[-1].replace(".", "") not in fileType:
                        print("这不是一张图片")
                        print("\a\a")
                        continue
                    aipOcr = init()
                    result = result_(target, options)
                    if len(result) == 0:
                        print("本次截图中没有找到内容")
                        print("\a\a")
                        continue
                    if translate:
                        result = translate_(result)
                    pyperclip.copy(result)
                    if sound_success:
                        print("\a")
                    print("已将本次结果复制到粘贴板")
        except Exception as e:
            if sound_failed:
                print("\a\a")
            print(e)
