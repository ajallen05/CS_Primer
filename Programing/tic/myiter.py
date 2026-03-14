# An implementation of the range object with reversed to learn Iterators


class Myrange:

    def __init__(self,*args):
        self.start = 0
        self.end=None
        self.step = 1
        self.n = self.start

        if(len(args)<1 or len(args)>3):
            raise TypeError
        
        elif len(args)==1:
            self.end = args[0]

        elif len(args)>=2:
            self.start = args[0]
            self.end = args[1]

            if(len(args)==3):
                self.step =  args[2]
    def __iter__(self):

        return self
    def __next__(self):

        if self.n == self.end:
            raise StopIteration
        ret = self.n
        self.n+=self.step
        return ret
    def __reversed__(self):

        return Myrange(self.end,self.start,-1)
def main():

    test = list(range(10))


    for i,num in enumerate(Myrange(10)):

        try:
            assert test[i]==num

        except:
            print(test[i],num)

    test2 = test[::-1]

    for i,num in enumerate(reversed(Myrange(10))):

        try:
            assert test2[i] == num

        except:
            print(test2[i],num)

    print("Passed All")


if __name__ == "__main__":

    main()

    




    


        

            
        
        

        




  


            






    