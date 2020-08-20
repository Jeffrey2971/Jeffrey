import os


def video_download():
    """
    基于python和you-git第三方下载包下载相关视频
    安装方法：pip3 install you-get 详情见：https://github.com/soimort/you-get
    适应python3.3以上版本
    """
    download_category = input("请选择下载视频类型：单个视频请输入1，系列视频请输入2\
(系列视频下载目前适用于哔哩哔哩)；或者输入“q”/“ctrl+c”退出程序: ")

    if download_category == 'q':
        quit()

    elif download_category == '1':
        # 单个视频下载
        video_path = input("请输入视频链接：")
        down_path = "you-get" + " " + video_path
        download(down_path)

    elif download_category == '2':
        list_download()

    else:
        print("请按照提示说明输入数值！")


def list_download():
    """下载bilibili的系列视频"""
    download_method = int(input("请选择下载方式：全部下载请输入1，单集下载请输入2，连续下载请输入3:"))

    if download_method == 1:
        video_path = input("请输入视频系列总链接：")
        video_count = int(input("请输入该视频总集数："))
        for i in range(1, int(video_count) + 1):
            if video_count == 1:
                down_path = "you-get" + " " + video_path
            else:
                down_path = "you-get" + " " + video_path + "?p=" + str(i)
            download(down_path)

    elif download_method == 2:
        video_path = input("请输入视频系列总链接：")
        video_index = input("请输入需要下载的集数：")
        down_path = "you-get" + " " + video_path + "?p=" + str(video_index)
        download(down_path)

    elif download_method == 3:
        video_path = input("请输入视频系列总链接：")
        video_start = input("请输入起始下载视频集数：")
        video_end = input("请输入截至下载视频集数：")

        # 加入链接和集数合法性验证

        for i in range(int(video_start), int(video_end) + 1):
            down_path = "you-get" + " " + video_path + "?p=" + str(i)
            download(down_path)

    else:
        print("请按提示要求输入数值！")


def download(down_path):
    """视频下载"""
    print("视频下载链接：", down_path)
    # message = os.popen(down_path)  # 返回cmd输入后返回信息
    message = os.system(down_path)
    print("message", message)


def quit():
    """退出"""

    print('退出程序...')


if __name__ == '__main__':
    video_download()
