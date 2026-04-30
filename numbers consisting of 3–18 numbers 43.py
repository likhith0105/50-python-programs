numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
numbers2 = [21,22,23,24,25]
combine = numbers + numbers2

for number in combine:
    if number % 4 == 0:
        print(number)