# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
product = a[0] * a[1]
print(product)