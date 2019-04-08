class MyStack:
    """implement stack with max in O(1)"""
    def __init__(self):
        self.mystack = []
        self.max_nums = []

    def push(self, item):
        # have to push it in anyway
        self.mystack.append(item)

        # if it's the first item
        # push it to max_nums too
        if (len(self.mystack) == 1):
            self.max_nums.append(item)

        # otherwise, compare with
        # the top of max_nums
        if (item > self.max_nums[-1]):
            self.max_nums.append(item)
        else:
            self.max_nums.append(self.max_nums[-1])

    def mymax(self):
        return self.max_nums[-1]

    def peek(self):
        return self.mystack[-1]

    def pop(self):
        self.mystack.pop()
        self.max_nums.pop()

def testme():
    s = MyStack()
    s.push(80)
    s.push(-2)
    s.push(9)

    print('==1')
    print(s.peek())
    print(s.mymax())

    s.push(10)
    print('==2')
    print(s.peek())
    print(s.mymax())

    s.push(15)
    print('==3')
    print(s.peek())
    print(s.mymax())

    s.pop()
    print('==4')
    print(s.peek())
    print(s.mymax())

if __name__ == '__main__':
    testme()

