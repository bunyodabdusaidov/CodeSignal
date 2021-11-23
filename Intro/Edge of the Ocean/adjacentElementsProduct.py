def solution(inputArray):
    largest_product = inputArray[0] * inputArray[1]
    n = 1
    while n < len(inputArray) - 1:
        current_product = inputArray[n] * inputArray[n+1]
        if current_product > largest_product:
            largest_product = current_product
        n += 1
    return largest_product
