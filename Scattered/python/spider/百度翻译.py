import requests
import execjs

# 浏览器代{过}{滤}理
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "referer": "https://fanyi.baidu.com/?aldtype=16047",
# cookie的值为你自己的 我在此没进行赋值
    "cookie": ""
}

# 全局变量 用来存放data 和 parament
data = {}
parament = {}

# 用来判断输入的字符串 是否包含中文
def Judgement_language(Unknown):
    x = 1
    for i in Unknown:
        # 中文在正则里的范围是\u4e00-\u9fff
        if u'\u4e00' <= i <= u'\u9fff':
            x = 0
            break
    # 包含中文就是中译英
    if x!=0:
        form = "en"
        to = "zh"
    # 不包含中文则是英译中
    else:
        form = "zh"
        to = "en"
    return form,to

# 用来获取sign
def judge_sign(Unknown):
    # 加载js里的算法 计算出sign
    JsData = execjs.compile("""
      function e(r) {
        var i = "320305.131321201"
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u = null !== i ? i : (i = window[l] || "") || "";
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S,
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
   }
  function n(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
   }
    """).call("e", Unknown)# 给e传递参数
    return JsData

# 传入form，to 和 待翻译的字符串 和 sign
def data_paraments(language,Unknown,sign):
    # 声明使用全局变量
    global data,parament
    # post请求url需要的data数据
    data = {
        "from": language[0],
        "to": language[1],
        "query": Unknown,
        "simple_means_flag": "3",
        "sign": sign,
# 把token修改为自己的 在此没进行赋值
        "token": ""
    }
    # 地址后面的后缀
    parament = {
        "from": language[0],
        "to": language[1]
    }


if __name__ == '__main__':
    # 待翻译的内容
    Unknown = input("请输入你要翻译的内容：")
    # 获取form 和 to
    language = Judgement_language(Unknown)
    # 获取 sign
    sign = judge_sign(Unknown)
    # 传入参数构造data 和 paraments
    data_paraments(language,Unknown,sign)
    # 请求url
    translates = requests.post(url="https://fanyi.baidu.com/v2transapi", data=data, params=parament,headers=header).json()
    # 提取需要的内容
    translate = translates["trans_result"]["data"][0]["dst"]
    print(translate)