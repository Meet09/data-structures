import sys
import copy


class LinkedList:
    class Node:
        def __init__(self, data, nextNode):
            self.data = data
            self.nextNode = nextNode

    __head = None
    __length = 0

    def __int__(self):
        self.__head = None

    def push(self, data):
        if self.__head is None:
            self.__head = self.Node(data, None)
            self.__length += 1
        else:
            lastnode = self.__head
            while lastnode.nextNode is not None:
                lastnode = lastnode.nextNode
            lastnode.nextNode = self.Node(data, None)
            self.__length += 1

    def pushAfter(self, element, data):
        tmp = self.__head
        while tmp is not None:
            if element == tmp.data:
                nn = tmp.nextNode
                tmp.nextNode = self.Node(data, nn)

                break
            tmp = tmp.nextNode
        self.__length += 1

    def pop(self):
        self.ele = self.__head
        while self.ele.nextNode is not None:
            self.prevEle = self.ele
            self.ele = self.ele.nextNode

        self.prevEle.nextNode = None
        del self.ele
        self.__length -= 1
        # popelement=None

    def removeFirst(self):
        self.temp = self.__head.nextNode
        self.__head = self.temp
        del self.temp
        self.__length -= 1

    def removeAfter(self, element):
        # 1 2 3 4 5
        tmp = self.__head
        while tmp is not None:
            if tmp.data == element:
                delnode = tmp.nextNode
                tmp.nextNode = delnode.nextNode
                del delnode
                break
            tmp = tmp.nextNode
        self.__length -= 1

    def searchElement(self, element):
        tmp = self.__head
        while tmp is not None:
            if (tmp.data == element):
                return True
            tmp = tmp.nextNode
        return False

    def printnodes(self):
        printnode = self.__head
        nodeView = ""
        while printnode:
            nodeView = nodeView + str(printnode.data) + " "
            printnode = printnode.nextNode
        print(nodeView[:-1])

    def length(self):
        print(self.__length)


"""
last node has nextnode value null i.e tail
first node has nextnode value of second and second has third like link
"""

# if __name__ == '__main__':
#     # first = Node(1, Node(2, Node(3, Node(4, None))))
#     # n = first
#     # while n:
#     #   print(n.data)
#     #   n = n.nextNode
#     #   print(n)

#     ll = LinkedList()
#     # print(ll.head)
#     # ll.append(1)
#     # ll.append(2)
#     # ll.append(3)
#     # ll.append(4)
#     for i in range(1, 5):
#         ll.push(i)
#     print("Before")
#     """
#     1 -> 2 -> 3 -> 4 -> None
#     """

#     ll.printnodes()
#     ll.pop()
#     print("After")
#     ll.printnodes()
#     # ll.length()

#     print(ll.length)
