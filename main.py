import urllib.request
import json

kd_dict = {1: 'shentong', 2: 'ems', 3: 'yuantong', 4: 'shunfeng', 5: 'yunda', 6: 'zhongtong', 7: "tiantian",
           8: "debang"}


def Check():
    while True:
        print("仅支持以下快递公司查询:")
        print("1.申通    ")
        print("2.EMS邮政    ")
        print("3.圆通    ")
        print("4.顺风    ")
        print("5.韵达    ")
        print("6.中通    ")
        print("7.天天    ")
        print("8.德邦    ")
        print("0.退出\n")
        choose = int(input("请选择您的快递公司:"))
        while choose not in range(0, 9):
            choose = int(input("抱歉暂不支持此公司请重新选择:"))
        if choose == 0:
            print("感谢使用!\n")
            break
        kd_num = input("请输入快递单号:")
        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[choose], kd_num)
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        status = target['status']
        if status == '200':
            data = target['data']
            for i in range(len(data)):
                print(i)
                print("\n时间: " + data[i]['time'])
                print("状态: " + data[i]['context'] + "")
            print("\n感谢使用!\n")
            break
        else:
            print("输入有误请重新输入!\n")
    # print("按任意键结束......")


if __name__ == '__main__':
    while True:
        Check()
        out = input("按任意数字退出(其他键继续).........")
        if '0' <= out <= '9':
            break
        else:
            print("\n")
            continue
