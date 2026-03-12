from numpy import array

lookup = array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]])


def check_digit(nums):
    total = 0

    for i, d in enumerate(reversed(nums)):


        total += lookup[i % 2][ord(d)-48]

    return total % 10 == 0


if __name__ == "__main__":

    assert  check_digit("17893729974")

    assert  not check_digit("17893729973")

    print("Yes! It works!.")
