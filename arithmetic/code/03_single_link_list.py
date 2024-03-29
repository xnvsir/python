# -*- coding:utf-8 -*-


class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem    # 保存的元素区
        self.next = None    # 下个元素默认为空


class SingleLinklist(object):
    """单链表的数据结构"""

    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表的长度，不需要的参数"""
        # cur 游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur!=None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur = cur.next
        print("")

    def add(self,item):
        """链表的头部添加，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """链表的尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """
        指定位置添加元素
        :param pos 从零开始
        """
        pre = self.__head
        if pos <=0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            count = 0
            while count <(pos-1):
                count += 1
                pre = pre.next
            # 当循环退后时，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur!= None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinklist()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(7)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.insert(-1, 100)
    ll.travel()
    ll.insert(4, 9)
    ll.travel()
    ll.insert(20, 50)
    ll.travel()