import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prevLink = None
        self.nextLink = None

    def value(self):
        return self.data

class DoubleLinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.cursor = None
        self.LAST = Node('LAST')

        if (args == ()): return

        # head
        self.head = Node(args[0])

        # mid
        prev = None
        current = self.head

        for arg in args[1:]:
            current.prevLink = prev
            current.nextLink = Node(arg)

            prev = current
            current = current.nextLink

        # tail
        self.tail = current
        self.tail.prevLink = prev

        # cursor
        self.cursor = self.LAST
        self.cursor.prevLink = self.tail
        self.tail.nextLink = self.cursor

    def values(self, direction=0):
        if (direction == 0):
            current = self.head

            if (current == None):
                return
            
            result = ''

            while current != self.LAST:
                result += current.data
                current = current.nextLink

            print(result)

        else:
            current = self.tail
            result = ''

            while current != self.LAST:
                result += current.data
                current = current.prevLink

            print(result)
  
    def getLength(self):
        current = self.head
        length = 0

        while current != None:
            length += 1

        return length
    
    def moveCursor(self, dir):
        # left
        if (dir == 'L' and self.cursor != self.head):
            self.cursor = self.cursor.prevLink
        
        # right
        elif (dir == 'D' and self.cursor != self.LAST):
            self.cursor = self.cursor.nextLink

    def getCursorPos(self):
        return self.cursor.data

    def insert(self, target, data):
        new_node = Node(data)
        current = self.head

        if (current == None):
            self.head = new_node
            self.tail = new_node

            self.moveCursor('D')
            return

        while True:
            # no target in this list
            if (current == self.LAST):
                prev = self.tail.prevLink
                prev.nextLink = new_node
                new_node.prevLink = prev
                new_node.nextLink = self.LAST
                self.LAST.prevLink = new_node
                self.tail = new_node
                return

            elif (current.data == target and current == self.cursor):
                prev = current.prevLink
                next = current.nextLink

                # target == head
                if (prev == None):
                    new_node.prevLink = None
                    new_node.nextLink = current
                    current.prevLink = new_node
                    self.head = new_node
                    return
                
                else:
                    prev.nextLink = new_node
                    new_node.prevLink = prev
                    new_node.nextLink = current
                    current.prevLink = new_node
                    return

            current = current.nextLink

    def pop(self, target):
        current = self.head

        # empty list
        if (current == None):
            return
        
        while True:
            # no target in this list
            if (current == self.LAST):
                prev = self.tail.prevLink
                prev.nextLink = self.LAST
                self.LAST.prevLink = prev
                self.tail = prev

                # print("no target")
                del(current)
                return

            # target is here!
            elif (current.data == target and current == self.cursor.prevLink):
                prev = current.prevLink
                next = current.nextLink

                # target == head
                if (prev == None):
                    if (current.nextLink == self.LAST):
                        self.head = None
                    else:
                        self.head = current.nextLink
                        self.head.prevLink = None

                    del(current)
                    return

                # target == tail
                if (next == None):
                    self.tail = current.prevLink
                    self.tail.nextLink = self.LAST
                    self.LAST.prevLink = self.tail
                    del(current)
                    return
                
                else:
                    prev.nextLink = next
                    next.prevLink = prev
                    del(current)
                    return 
            
            current = current.nextLink

string = list(input().rstrip())
N = int(input().rstrip())

editor = DoubleLinkedList(*string)

for _ in range(N):
    cmd, *args = input().rstrip().split()
    
    if (cmd == 'L'):
        editor.moveCursor('L')

    if (cmd == 'D'):
        editor.moveCursor('D')

    if (cmd == 'B' and editor.cursor != editor.head):
        editor.pop(editor.cursor.prevLink.data)

    if (cmd == 'P'):
        arg = args[0]

        editor.insert(editor.cursor.data, arg)

    editor.values()
    print(editor.getCursorPos())
    print('-----------------------')

editor.values()