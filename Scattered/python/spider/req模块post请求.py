import requests
import re
import os

# Request URL: http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule


def _get(_to, header, url):
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

    return requests.post(url, headers=header, data=fromdata).text


def _re(request):

    pat = r'"tgt":"(.*?)"}'

    return re.findall(pat, request)


if __name__ == '__main__':
    _to = input('请输入需要翻译的信息返回json格式：')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) A'
                            'ppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    request = _get(_to, header, url)

    result = _re(request)

    print('需翻译内容：' + _to + '\n翻译结果为：' + result[0])

print('运行结束，请按任意键退出！')
os.system('pause>nul')
quit()
