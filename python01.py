import pickle
import os


# 创建一个专门用来存储信息的类，这个类有自己固定的内存空间，不像对象一样会被回收，导致数据消失
class Save:
    # 总的信息池
    messagePool = []
    # 保存信息的格式形如 uid : 留言内容，因为load只能加载一个对象，所以用一个字典对象进行所有信息的存储
    message_board = {}
    # 保存信息的文件
    load_url = './text.txt'
    # 保存全部信息的文件
    message_pool_url = './message.txt'


class Student():
    text = 'message board'
    is_lock = False

    def __init__(self, uid=None):
        self.uid = uid
        self.msg = []

    def leave_a_message(self):
        if self.is_lock is False:
            self.is_lock = True
            try:
                with open(Save.load_url, 'rb+') as fp:
                    msg = pickle.load(fp)
                Save.message_board = msg
                with open(Save.message_pool_url, 'rb') as fp:
                    Save.messagePool = pickle.load(fp)
            except FileNotFoundError as e:
                pass
            res = input('请输入你的留言')
            with open(Save.message_pool_url, 'wb') as fp:
                Save.messagePool.append(res)
                pickle.dump(Save.messagePool, fp)

            # 如果用户第一次发言，字典没有对应的索引会报错，在content里调用了索引，哪里有错找哪里，所以要在此处做异常处理
            # 不能覆盖用户的发言
            try:
                content = Save.message_board[self.uid] + ',' + res
            except KeyError as e:
                content = res
            Save.message_board[self.uid] = content
            with open(Save.load_url, 'wb+') as fp:
                pickle.dump(Save.message_board, fp)

        else:
            print('请不要多次留言！')


def get_message(uid=None):
    with open(Save.load_url, 'rb+') as fp:
        # 只能读取一个对象
        msg = pickle.load(fp)
        if uid is not None:
            try:
                lists = msg[int(uid)].split(',')
                cnt = len(lists)
                if cnt >= 20:
                    print(list[-21:-1:-1])
                else:
                    print(lists)
            except KeyError as e:
                print('此id未被注册')
        else:
            with open('./message.txt', 'rb') as fp:
                msgs = pickle.load(fp)
                if len(msgs) >= 10:
                    print(msgs[-1:-11:-1])
                else:
                    print(msgs)



zs =  Student()
zs.leave_a_message()
get_message()