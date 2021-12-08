import time
import random


def solution(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            n = i
            while n != len(a):
                #print(f"n = {n}")
                #print(f"i+1 = {i+1}")
                #print(f"len(a) - 1 = {len(a) - 1}")
                for j in range(i, len(a) - 1):
                    tmp = a[n]
                    a[n] = a[j]
                    a[j] = tmp
                    #print(f"a[n] = {a[n]}")
                    #print(f"a[j] = {a[j]}")
                    #print(a)
                    if a == b:
                        return True
                    else:
                        tmp = a[n]
                        a[n] = a[j]
                        a[j] = tmp
                n += 1
            return False
    return True

a = []
b = []
for i in range(3, 10**5+1):
    a.append(random.randint(1,1000))
    b.append(random.randint(1,1000))

#print(a)
#print(b)
tic = time.perf_counter()
print(solution(a, b))
toc = time.perf_counter()
print(f"Function executed = {toc - tic:0.4f} seconds")


