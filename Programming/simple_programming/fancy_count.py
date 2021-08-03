from time import time


def count_stuff():
    flag = ""
    f    = open("data.dat", "r"); data = f.read().split("\n")

    check_zeros  = lambda x: x.count('0') % 3 == 0
    check_ones   = lambda x: x.count('1') % 2 == 0

    checked_data = [ line for line in data if (check_ones(line) or check_zeros(line)) and line ]
    f.close()

    return len(checked_data)


if __name__ == '__main__':
    start = time()
    print(f"Flag: {count_stuff()}")
    print(f"Time Taken: { time() - start }")
