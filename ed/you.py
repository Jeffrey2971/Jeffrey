import random
import socket


def begin(day, num, flag):
    while not flag:
        time = str(random.randrange(24))+':'+str(random.randrange(60))+':'+str(random.randrange(60))
        print('mable, i miss you at:', time, 'but you leave me...')
        if random.randrange(685) + 1 == day:
            flag = True
        num += 1
    print("""
          Mable,
          This is the last program I wrote for you,         
          it was our second day apart, this moment i miss u again,
          i love u so much but you didn't love me from the begtime to the endtime,
          we were wrong from the beginning, maybe u and i are not from the same world,
          thank u for spending 685 days with me, this period of time i vert happy and
          there are so many things i want to tell u but u don't care, so forget it,
          that's all in the past,right?
                            so please give me this chance to leave u,and place dot't get me any hope
                            Remember my birthday? Enter it and delete anything about you.
                            (photo/video/msg/music)
          """)

    print('format：year/month/day')
    return input('(:'), input('Any something else to talk me?')


def send(a, b):
    pass


def get():
    pass


if __name__ == '__main__':
    day, num, flag, port, ip = 685, 0, False, 8000, '11.230.64.210'
    ask = begin(685, 0, False)
    send(ask[0], ask[1])
    
    

