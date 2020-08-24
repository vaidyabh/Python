'''# 1) If natural number is divisble by 3 and 5, provide the sum of those number'''

def solution(number):
    sum = 0
    print('add num', number + 1)
    for num in range(1, number):
       # print('num outside', num)
        if (num % 3 == 0) or (num % 5 == 0):
            print('num inside ', num)
            sum = sum + num
            
    return sum

print(solution(10)) # output is 23


'''# 2) print float values for below code'''

print(float(''))            # ValueError: could not convert string to float:
print(float(5))             # 5.0
print(float('5', '1234'))   # ValueError: could not convert string to float:
