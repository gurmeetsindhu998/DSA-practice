class Stack():
    def __init__(self) -> None:
        self.st=[]

    def push(self, data:int):
        self.st.append(data)

    def pop(self):
        return self.st.pop()
    @property
    def empty(self):
        return self.st == []


def stinv( sta: Stack) -> Stack:
    temp= Stack()
    revst = Stack()
    while not sta.empty:
        item = sta.pop()
        temp.push(item)
        revst.push(item)

    while not temp.empty:
        sta.push(temp.pop())

    return sta

if __name__=="__main__":
    s= Stack()
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    rev = stinv(s)
    
    while len(rev.st) >0 :
        print(rev.pop())
