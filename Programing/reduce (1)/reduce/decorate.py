
def pretty_print(fn):

    def wrapper(*args,**kwargs):



        print(f"The function: {fn.__name__}")

        print(f"The description: {fn.__doc__.strip() if fn.__doc__ is not None else None}")

        for name,val in zip(fn.__code__.co_varnames[:len(args)],args):
            print(f"{name}:{val}")

        for name in (kwargs):
            print(f"{name}:{kwargs[name]}")


        try:
            val = fn(*args,**kwargs)
            print(f"The output: {val}")
            print()
            return val
        except Exception as e:
            print(f"Error: {e}")
        print()
            
        

    return wrapper


@pretty_print
def square(n,lim=1e16):

    """

        To find the square of a given number

        n = input
        lim = the limit of the input. if greater error is raised
    
    """

    if n>lim:
        raise Exception(f"input greater than the limit: {lim}")
    return n*n

@pretty_print
def fib(n,s = 0,t=1):

    """

        Used to find the Nth fibonacci number using iteration

        n = the end  position
        s = where we start
        t = the number after start in the series
    
    """



    for i in range(n):

        temp = s

        s = t
        t+=temp

    return temp

@pretty_print
def cube(n):
    return n*n*n






    



def main():

    """
                     To work with decorators to understand them more

    """

    square(1000000,1000)
    fib(11,s = 3,t=5)
    cube(3)


if __name__ == "__main__":
    print(main.__doc__)
    print()
    main()