#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


class StaticChain:
    def __new__(cls, *args, **kwargs):
        cls.pin = []
        cls.data = []
        return object.__new__(cls)

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.count = 0
        if not self.pin:
            for i in range(maxsize):
                self.pin.append(i)
                self.data.append(None)
            self.pin[0] = 1
            self.pin[maxsize - 1] = 0

    # 添加方法
    '''
        插入位置0，则self.pin[self.maxsize - 1]改变；
        其它为插入的前一个元素变，本身变，self.pin[0]也变
    '''
    def add_item(self, element=None, position=0):
        if not element:
            print('没有数据无法添加')
            return
        if position > self.count or self.count == self.maxsize - 2:
            print('列表长度不够，无法添加')
            return
        # 先添加元素，再修改其对应的pin
        self.data[self.pin[0]] = element
        if position == 0:
            self.pin[self.pin[0]], self.pin[self.maxsize - 1] = \
                self.pin[self.maxsize - 1], self.pin[0]
        else:
            temp = self.pin[self.maxsize - 1]
            for i in range(position - 1):
                temp = self.pin[temp]
            self.pin[self.pin[0]], self.pin[temp] = self.pin[temp], self.pin[self.pin[0]]
        self.pin[0] = self.data[1:].index(None) + 1
        if self.count == 0:
            self.pin[self.pin[0]] = 0
        self.count += 1
        print('添加完成')

    # 删除方法
    '''
        删除0位时，只需要修改self.pin[self.maxsize - 1]；
        删除末位时，只需要指末位的前一位pin改为0；
        其它只需要把pin值替换成被删除位的pin值即可
    '''
    def del_item(self, position):
        if position > self.count - 1:
            print('位置超过列表元素，无法进行删除操作')
        if self.count == 0:
            print('当前列表已空，无法进行删除操作')
        temp = self.pin[self.maxsize - 1]
        if position == 0:
            self.pin[self.maxsize - 1] = self.pin[temp]
            self.count -= 1
            print('删除完成')
            return
        for i in range(position - 1):
            temp = self.pin[temp]
        # 把对应的数据清空
        self.data[self.pin[temp]] = None
        if position == self.count - 1:
            self.pin[temp] = 0
        else:
            print(temp)
            self.pin[temp] = self.pin[self.pin[temp]]
        self.count -= 1
        self.pin[0] = self.data[1:].index(None) + 1
        print('删除完成')

    # 显示方法
    def show_items(self, position=1):
        temp = self.pin[self.maxsize - 1]
        for i in range(self.count):
            print(self.data[temp], end=' ')
            temp = self.pin[temp]
        print('\n', self.pin, '\n', self.data)


if __name__ == '__main__':
    test = StaticChain(6)
    test.add_item('A', 0)
    test.show_items()
    print('\n' + '~' * 20)
    test.add_item('B', 0)
    test.show_items()
    print('\n' + '~' * 20)
    test.add_item('C', 1)
    test.show_items()
    print('\n' + '~' * 20)
    test.add_item('D', 3)
    test.show_items()
    print('\n' + '~' * 20)
    test.del_item(2)
    test.show_items()
    print('\n' + '~' * 20)
    test.del_item(0)
    test.show_items()
    print('\n' + '~' * 20)
    test.del_item(1)
    test.show_items()

