
from urllib import request
import urllib.parse
import re
import os


# Request URL: http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule

'''
i: 你好
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15764179485786
sign: bbe247ed7b1fd652524877b91c20521a
ts: 1576417948578
bv: 1737e427f1a1a5eb9068cf6afc8730f4
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''


def _connect():
    try:
        request.urlopen('http://www.baidu.com/', timeout=2)
    except:
        return False
    return True


def _get(_to,header,url):
    fromdata = {  # post 请求所需参数fromdata
    'i': _to,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15764179485786',
    'sign': 'bbe247ed7b1fd652524877b91c20521a',
    'ts': '1576417948578',
    'bv': '1737e427',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
    }

    data = urllib.parse.urlencode(fromdata).encode(encoding='utf-8')

    req = request.Request(url, data=data, headers=header)

    return request.urlopen(req).read().decode()


def _re(request):

    pat = r'"tgt":"(.*?)"}'

    return re.findall(pat, request)


def _out():
    print('翻译结束，请按任意键退出！')
    os.system('pause>nul')
    quit()


if __name__ == '__main__':
    _connect_result = _connect()
    if _connect_result is False:
        print('当前网络不可用！')
        _out()
    _to = input('请输入需要翻译的信息返回json格式：')
    if _to == '':
        print('输入不能为空！')
        _out()
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) A'
                            'ppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    request = _get(_to, header, url)

    result = _re(request)

    print('需翻译内容：' + _to + '\n翻译结果为：' + result[0])

    _out()
