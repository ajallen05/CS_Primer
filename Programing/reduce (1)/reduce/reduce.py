"""
Implement the following functions, at least enough to get the tests to pass.

Try implementing each from scratch, but also once you've implement reduce, try implementing
them in terms of reduce!

As stretch goals:

    - Add more tests, and have them pass
    - Increase the flexibility of each function, e.g. enable my_map to operate over any iterable type
    - Implement more functions in terms of what you already have, e.g. "flatten", "unique", "group_by" etc. See https://lodash.com/docs/ for a long list of interesting utility functions.
"""


"""

how reduce works:

if init is none it becomes the first element


then we apply init to the second element in the function and return the value

"""

from collections.abc import Iterable


def reduce(f, xs, init=None):
    """
    Apply the function f cummulatively to the items of xs, reducing to a single value.

    If initializer is provided, use it as the first value. Otherwise, use only the
    values in xs.

    >>> reduce(lambda acc, x: acc + x, [1, 2, 3, 4])
    10
    >>> def mirror(d, x):
    ...     d[x] = x
    ...     return d
    >>> reduce(mirror, ['foo', 'bar'], {})
    {'foo': 'foo', 'bar': 'bar'}

    >>> reduce(lambda acc, x: -1*abs(acc) - x, [1,2,3,4])
    -10


    """

    xs = iter(xs)
    init = next(xs) if init is None else init
    
    for elem in xs:
        init = f(init,elem)

    return init


    """  

        My implementation

         xs,init = (xs,init) if init is not None else (xs[1:],xs[0])

         for i in xs:
         
            init = f(init,i)

        return init




    
    """



def product(nums):
    """
    Return the product of the given numbers

    >>> product([2, 3])
    6
    >>> product([-1.0, -1.0, -1.0])
    -1.0
    >>> product([])
    1
    """

    return reduce(lambda x,y:x*y,nums,1)




def my_map(f, xs):
    """
    Return a new list, with the function f applied to each item in the given list

    >>> my_map(lambda x: x * x, [1, 2, 3, 4])
    [1, 4, 9, 16]
    >>> my_map(lambda x:x*x,{1:1,2:2,3:3})
    [1, 4, 9]
    """

    def g(lis,i):

        lis.append(f(i))
        return lis
    
    return reduce(g,xs,[])


    """

        my implementation:

            return [f(i) for i in xs]
    
    """







        




def my_filter(f, xs):
    """
    Given a predicate function f (a function which returns True or False) and a list
    xs, return a new list with only the items of xs where f(x) is True

    >>> my_filter(lambda x: x > 0, [-1, 3, -2, 5])
    [3, 5]
    >>> my_filter(lambda x: False, [1, 2])
    []
    """

    def g(xs,x):

        if f(x):
            xs.append(x)
        return xs
    
    return reduce(g,xs,[])


    """

        my implementation:

        return [i for i in xs if f(i)]
    
    """









def my_zip(*iters):
    """
    Given one or more iterables of the same length, return a list of lists of them
    "zipped" together, ie grouped by index

    >>> my_zip('abc', 'def', (1, 2, 3))
    [['a', 'd', 1], ['b', 'e', 2], ['c', 'f', 3]]
    """


    def g(ans,iters):
        for i,elem in enumerate(iters):
            ans[i].append(elem)

        return ans

    
    return reduce(g,iters,[[] for j in iters])


def my_unique(lis):
    """
    Returns sorted unique elements from the list.

    Basic case
    >>> my_unique([1,2,3,1,2,5,5,5,5,7,0,0,0,9])
    [0, 1, 2, 3, 5, 7, 9]

    Already unique
    >>> my_unique([1, 2, 3])
    [1, 2, 3]

    Unsorted input
    >>> my_unique([5, 3, 1, 4, 2])
    [1, 2, 3, 4, 5]

    Single element
    >>> my_unique([42])
    [42]

    Empty list
    >>> my_unique([])
    []

    Negative numbers
    >>> my_unique([-1, -2, -1, 0, 1])
    [-2, -1, 0, 1]

    Mixed integers and booleans (tricky)
    >>> my_unique([1, True, 0, False])
    [0, 1]

    Floats and ints
    >>> my_unique([1, 1.0, 2, 2.0, 3])
    [1, 2, 3]

    Strings
    >>> my_unique(["b", "a", "b", "c"])
    ['a', 'b', 'c']

    Mixed comparable types (should work if comparable)
    >>> my_unique(["apple", "banana", "apple"])
    ['apple', 'banana']

    Large duplicates
    >>> my_unique([1]*100 + [2]*50 + [3]*10)
    [1, 2, 3]

    Edge: None values
    >>> my_unique([None, None, 1])
    Bruh


    Edge: unorderable types (depends on your implementation)
    >>> my_unique([1, "a"])
    Bruh
    
 
    """
    try:


        def g(xs,x):


            if x not in xs:
                xs.append(x)
            return xs
        
        return sorted(reduce(g,flatten(lis),[]))
    
    except Exception as e:
        print("Bruh")



def flatten(lis):
    """
    Flattens a nested iterable into a single list.

    Basic case
    >>> flatten([[1], ["a", "b", 2], range(3, 6)])
    [1, 'a', 'b', 2, 3, 4, 5]

    Already flat
    >>> flatten([1, 2, 3])
    [1, 2, 3]

    Deep nesting
    >>> flatten([1, [2, [3, [4, [5]]]]])
    [1, 2, 3, 4, 5]

    Empty structures
    >>> flatten([])
    []
    >>> flatten([[], [[]], [[[]]]])
    []

    Mixed types
    >>> flatten([1, "abc", [2, "de"]])
    [1, 'abc', 2, 'de']

    Tuples and lists mixed
    >>> flatten([1, (2, 3), [4, (5, 6)]])
    [1, 2, 3, 4, 5, 6]

    Range objects
    >>> flatten([range(3), [3, 4]])
    [0, 1, 2, 3, 4]

    Single element nested many times
    >>> flatten([[[[[1]]]]])
    [1]

    Boolean and None
    >>> flatten([True, [False, [None]]])
    [True, False, None]

    Edge case: string handling (depends on your design)
    >>> flatten(["hello", ["world"]])
    ['hello', 'world']
    """

    def g(xs,x):
       
       
       

       if not isinstance(x, Iterable) or  isinstance(x, (str, bytes)):
           xs.append(x)
           return xs
       
       ans = []


       for i in x:
            
           if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
                ans.extend(g([],i))
           else:
               ans.append(i)

       xs.extend(ans)

       return xs
                
               
    
    return reduce(g,lis,[])











if __name__ == "__main__":
    import doctest
    doctest.testmod()
    flatten([[1],["a","b",2],range(3,10)])


    print('ok')
