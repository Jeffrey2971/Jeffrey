from urllib import request

url = 'http://i.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                  'AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56'
                  ' Safari/535.11',

    'Cookie': 'BIDUPSID=768BEE8CB74BDA3692D056815506C385; PSTM=1576036744; BAIDUID=768BEE8CB74BDA36CBCC1573383EBC6B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1452_21115_30210_18560_22160; PSINO=7; yjs_js_security_passport=fd8f9420e7a22cfd55a9d54ff97a2938ad60d47d_1576467533_js; ZD_ENTRY=baidu; PHPSESSID=t95udss0sfuq1varosfiui1h31; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1576476792; BDUSS=XBKamdhLXo4a0YwbTM1MlplcnU0TVdTT05sRG9zalNFUXZTdnNiS0dKMlFyUjVlRVFBQUFBJCQAAAAAAAAAAAEAAACZaU-3SmVmZnJleTI5NzEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJAg912QIPddM; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1576476820'
}

req = request.Request(url)

reponse = request.urlopen(req)

print(reponse.read().decode())
