import time
from functools import lru_cache

# @lru_cache(maxsize=2)
# def some_work(n):
#     time.sleep(3)
#     return n

# if __name__ == '__main__':
#     print("hello")
#     some_work(3)
#     some_work(4)
#     some_work(5)
#     print("good ")
#     some_work(3)
#     print("what going on")


@lru_cache(maxsize=int(input()))
def multiply(num):
    time.sleep(3)
    sum = 0
    for i in range(10):
        sum = num+i
    return sum


if __name__ == '__main__':
    print(multiply(30))
    print(multiply(20))
    print("hello")
    print(multiply(30))
    print(multiply(303))
    print("bye")
