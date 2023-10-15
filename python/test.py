data = [1, 5, 4, 9]


def add_sum(nums, target):
    for i in nums:
        diff = target - i
        if diff in nums:
            return True


print(add_sum(data, 10))


# def longestCommonPrefix(strs):
#     result = ''
#     for value in strs:
#         pass


# while data:
#     print(data)

temp = 6565165
Temp = 641983860673

print(temp)
print(Temp)

print(109 & 5)

squares = []

for i in range(11):
    squares.append(i * i)

print(squares)
for i in range(8, -9, -2):
    print(i)

print([i * (i + 1) for i in range(0, 10)])

nums = [1, 2, 3, 4, 5, 6, 5, 1]

for i in nums:
    for j in nums[i:]:
        if i == j:
            print(i, j)


def fibbonacci(n):
    if n < 0:
        return "incorrect value"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)


print(fibbonacci(10))


def check_prime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return 0
    else:
        return 1


def primes_in_list(nums):
    prime_nums = []
    for i in nums:
        if check_prime(i):
            prime_nums.append(i)
    return prime_nums


print(primes_in_list([i for i in range(50)]))

for i in range(6):
    for j in range(i):
        print(i, end=" ")
    print(" ")

for i in range(6):
    for j in range(i):
        print(j, end=" ")
    print(" ")

for i in range(6, 1, -1):
    for j in range(i):
        print(i, end=" ")
    print(" ")


for i in range(10):
    for j in range(i):
        if not i % 2 == 0:
            print(i, end=" ")
    print(" ")

for i in range(6):
    for j in range(6):
        if i > j:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print(" ")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print(" ")

for i in range(1, 10):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print(" ")

for i in range(0, 6):
    for j in range(i, 6):
        print(j, end=" ")

    print(" ")

size = 7
m = (2 * size) - 2
for i in range(7):
    for j in range(0, m):
        print(end=" ")
    m -= 1
    for j in range(i + 1):
        print("*", end=" ")
    print(" ")

line = "hello world"
letters = []
word = ""
for i in line:
    letters.append(i)

for i in range(len(letters)):
    word += letters.pop()

print(word)

string = ""
for i in line:
    string = i + string

print(string)

m = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

l_d = 0
r_d = 0
for i in range(0, len(m)):
    l_d += m[i][i]
    r_d += m[i][-1 - i]

print(l_d)
print(r_d)
print(abs(l_d - r_d))

for i in range(6):
    for j in range(6 - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("#", end=" ")
    print("")


def mul_w(a, b):
    result = 0
    for i in range(b):
        result += a
    return a


print(mul_w(3, 5))


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for i in fib(5):
    print(i)


t = (
    56,
    65,
    165,
    [654, 64, 64, 65],
    165,
    165,
    5,
)
t_i = t.index()

print(type(t))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print("dzfhgjh", x)
