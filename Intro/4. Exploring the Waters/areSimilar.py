def solution(a, b):
    l = len(b) // 2
    m = len(b) // 2
    if a == b:
        return True
    for i in range(len(a)//2):
        print(f"i = {i}")
        print(f"l = {l}")
        for j in range(len(a)//2 + 1):
            print(f"j = {j}")
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            print(f"1.{a}, \n  {b}")
            if a == b:
                return True
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            print(f"2.{a}, \n  {b}")               
            tmp = b[l]
            b[l] = b[m]
            b[m] = tmp

            print(f"3.{a}, \n  {b}")

            if a == b:
                return True

            tmp = b[l]
            b[l] = b[m]
            b[m] = tmp
            print(f"4.{a}, \n  {b}")
            print(f"m = {m}")
            
            m += 1
        l += 1

    return False

a = [2, 3, 1]
b = [1, 3, 2]

print(solution(a, b))
