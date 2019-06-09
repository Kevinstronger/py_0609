import random
#多个字符中选取特定数量的字符：
def fun1():
    for i in range(5):
        name = ''.join(random.sample('123456789abcdefg', 8))
        print(name)

def fun2():
    for i in range(10):
        print(random.randint(1,5))
#0-100之间的偶数
def fun3():
    for i in range(20):
        print(random.randrange(0,101,2))

def fun4():
    for i in range(5):
        print(random.choice( ['apple', 'pear', 'peach', 'orange', 'lemon'] ))

def sum(a):
    i = 1
    sum = 0
    while i<=a:
        sum = sum + i
        i += 1
    return sum



if __name__ == '__main__':
    num = int(input('请输入一个正整数：'))
    if isinstance(num, int):
        result = sum(num)
        print(result)

