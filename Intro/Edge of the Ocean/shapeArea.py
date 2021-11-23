def solution(n):
    if not 1 <= n < 10 ** 4:
        return False
    area = n ** 2 + (n - 1) ** 2
    return area
