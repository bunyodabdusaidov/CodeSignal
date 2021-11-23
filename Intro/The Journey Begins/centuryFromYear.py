def solution(year):
    century_span = 100
    century = 1
    while True:
        if year <= century_span:
            return century
        century_span += 100
        century += 1
