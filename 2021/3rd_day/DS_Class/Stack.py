from DS_Class.LinkedList import LinkedList

class Stack:
    def __init__(self, d):
        self.top = -1
        self.dim = d
        self.data = [0]*d

    def push(self, o):
        if(self.top==len(self.data)-1): # stack이 가득차면..
            self.data = self.data+[0]*self.dim
        self.top=self.top+1
        self.data[self.top]=o

    def pop(self):
        if self.top < 0:
            print("Stack Empty")
            return None
        else:
            self.top = self.top-1
            return self.data[self.top+1]

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def size(self):
        return self.top+1

    def topv(self):
        if self.top < 0:
            print("Stack Empty")
            return None
        else:
            return self.data[self.top]

    def printStack(self):
        print("There are ", self.size(), " elements: ", end='')
        print('[', end='')
        for i in range(0, self.size()):
            if i==self.size()-1:
                print(self.data[i],']')
            else:
                print(self.data[i],',', end='')

class LStack:
    def __init__(self):
        self.size=0
        self.top=None
        self.data=LinkedList()

    def push(self,o):
        self.top = self.data.insertLast(o)
        self.size = self.size+1

    def pop(self):
        self.size=self.size-1
        self.top=self.top.getPrev()
        return self.data.remove(self.top.getNext())

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def size(self):
        return self.size

    def printStack(self):
        print("There are ", self.size, " elements in the Stack: ", end='')
        self.data.printList()
    def topv(self):
        return self.data.Last().getElement()

if __name__ == '__main__':
    #s=Stack(2)
    s=LStack()
    s.push("Hyerim Bae")
    s.push("Wonkyunmg Kim")
    s.pop()
    s.push("Taewoong Bae")
    s.push("Taeyoung Bae")
    s.printStack()


