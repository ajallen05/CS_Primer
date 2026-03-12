def f (i,d):

        num = d + d * (i % 2)
        return num // 10 + num % 10



lookup = {d:f(1,d) for d in range(10)}





def check_digit_imperative(nums) -> bool:

    total = 0


    for i in range(len(nums)):

        # num = int(nums[- i-1]) + int(nums[- i-1]) * (i % 2)
        # total += num // 10 + num % 10

        total += f(i,int(nums[-i-1]))

    return total % 10 == 0


def check_digit_functional(nums) ->bool:

    return sum(f(i,int(d)) for i,d in enumerate(reversed(nums)))%10==0


def check_digit_lookup(nums) -> bool:
     


     return sum(lookup[int(d)] if i%2 else int(d) for i,d in enumerate(nums))%10==0


checks = [check_digit_imperative,check_digit_functional,check_digit_lookup]








if __name__ == "__main__":


    for check_digit in checks:


        assert check_digit("17893729974")

        assert not check_digit("17893729973")

        print(check_digit,"works")

    print("Yes! It works!.")
