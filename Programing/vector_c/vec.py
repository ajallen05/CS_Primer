from functools import reduce

class Vector:
    def __init__(self,*args):

        for val in args:

            if not type(val) in (int,float):
                raise Exception(f"Vectors values should be of type Int or Float not {type(val)}")
        
        self.values = args

    @property
    def norm(self):
        return round(self/self.magnitude,2)
    
    @property
    def magnitude(self):
        return round(reduce(lambda x,y: x**2 + y**2,self.values)**(0.5),2)

    def __round__(self, ndigits=0):
        return Vector(*map(lambda x: round(x,ndigits),self.values))
    
    def __str__(self):
        return f"{(self.values)}"
    
    def __iter__(self):
        for val in self.values:
            yield val

    def __getitem__(self, key):
        return self.values[key]
    
    def __repr__(self):
        return f"Vector{self.values}"
        
    def __len__(self):
        return len(self.values)
    
    def len_check(self,other):
        return len(self) == len(other)
    
    def __ne__(self,other):

        return not self==other

    def __eq__(self, other):
        if not self.len_check(other):
            raise Exception(f"comparission yielded unequal sizes of {len(self)} and {len(other)}")
        for i,j in zip(self.values,other.values):
            if i!=j:
                return False
        return True
    
    def __add__(self, other):
        if self.len_check(other):
            vals = (i+j for i,j in zip(self.values,other.values))
            return Vector(*vals)
        else:
            raise Exception(f"Sizes of {len(self)} and {len(other)} are not compatible for addition")
        
    def __sub__(self,other):
        return self + -1*other
        
    def __mul__(self,other):
        if  type(other) in (int,float):        
            return Vector(*(i*other for i in self.values))

        elif type(other) is Vector:
            return Vector(*(i*j for i,j in zip(self,other)))
        else:
            raise Exception(f"Multiplication with value '{other}' of type {type(other)} is not possible")
    
    def __truediv__(self,other):

        if other == 0:
            raise Exception("Vector Division with 0 not possible")
        
        return self * (1/other)
    
    def __rtruediv__(self,other):

        return self/other
        
    def __neg__(self):
        return -1 * self
    
    def __rmul__(self,other):
        return self * other 
    

    @classmethod
    def dot(cls,vec1,vec2):
        return vec1.dot(vec2)
    

    def dot(self,vec2):
        return reduce(lambda y,x: y + x[0]*x[1],zip(self,vec2),0)

if __name__ == "__main__":
    
    v1 = Vector(1,1,1)
    v2 = Vector(4,4,4)
    assert v2 - v1 == Vector(3,3,3)

    v1 = Vector(3, 2)
    v2 = Vector(1, 1)
    assert v1 + v2 == Vector(4, 3)
    assert v1 * 2 == Vector(6, 4)
    assert 2 * v1 == Vector(6, 4)


    for i,val in enumerate(Vector(1,2,3)):
        assert i+1 == val
    
    assert Vector(2,4,6)[2] == 6

    try:

        Vector(False,1,2)
    except:
        pass
    else:
        assert False,"Non number exception was not raised"

    
    assert eval(repr(Vector(1,1))) == Vector(1,1)
    print("ok")




            
    
