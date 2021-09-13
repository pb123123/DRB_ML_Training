class MyVector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
            self.size=0
        else:
            try:  # we test if param is iterable
                self.coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def getSize(self):
        return self.size
        
    def getItems(self):
        return self.coords

    def elementAt(self, i):
        if self.size!=0 and i<self.size:
            return self.coords[i]
        else:
            print("요청한 범위가 올바르지 않습니다.")

    def insertAt(self, i, val):
        if self.size == len(self.coords)-1:
            #print("꽉 찼어요.")
            newList = [0] * (len(self.coords)*2)
                #(range(len(self.coords)*2))
            for j in range(0, self.size):
                newList[j]=self.coords[j]
            self.coords = newList
        if i >= 0 and i<= self.size:
            for k in range(self.size, i, -1):
                self.coords[k]=self.coords[k-1]
            self.coords[i]=val
            self.size = self.size+1

    def removeAt(self, i):
        if self.size == 0:
            print("빈 벡터입니다.")
        else:
            if i < 0 or i >= self.size:
                print("잘못된 범위의 숫자입니다.")
            else:
                for k in range(i, self.size):
                    self.coords[k]=self.coords[k+1]
                self.size = self.size-1

    def replaceAt(self, i, val):
        if i < 0 or i >= self.size:
            print("잘못된 범위의 숫자입니다.")
        else:
            self.coords[i] = val

    def insertLast(self, val):
        if self.size == len(self.coords)-1:
            print("꽉 찼어요. 벡터를 조금 더 늘립니다. ", val)
            newList = [0] * (len(self.coords)*2)
                #(range(len(self.coords)*2))
            for j in range(0, self.size):
                newList[j]=self.coords[j]
            self.coords = newList
        self.coords[self.size]=val
        self.size=self.size+1

    def printVector(self):
        print('[', end='')
        for i in range(0, self.size):
            if i==self.size-1:
                print(self.coords[i],']')
            else:
                print(self.coords[i],',', end='')

    def toString(self):
        str=""
        for i in range(0, self.size):
            str=str+self.coords[i]
        return str