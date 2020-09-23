# Tutorial2
ex = int(input("Choose to run an exercise:"))
if ex == 1:
    # Ex1 Calculating BMI
    wei = 80.5
    hei = 1.75
    BMI = wei / (hei * hei)
    print("{:.2f}".format(BMI))
    if BMI >= 18.5 and BMI <= 25:
        print("Healthy")
    else:
        print("Unhealthy")
elif ex == 2:
    # Ex2 reverse number
    num = int(input(""))
    a = num
    print("original number", a)
    temp = 0
    while a != 0:
        temp = a % 10 + temp * 10
        a = a // 10

    if temp == num:
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not the same")
elif ex == 3:
    # Ex3 Summation
    list = [1, 3, 4, 8, 9]
    sum = 0

    for x in list:
        sum += x

    print(sum)
elif ex == 4:
    # Ex 4 Two-Sum Problem
    nums = list(map(int, input("Enter a list elements separated by space : ").split()))
    target = int(input("Target:"))
    for x in range(len(nums)):
        for y in range(x, len(nums)):
            if target - nums[x] == nums[y]:
                print("[{},{}]".format(x, y, ))
                break
        else:
            continue
        break
elif ex == 5:
    # Ex 5 Implement your range()
    start = int(input("Start:"))
    end = int(input("End:"))
    step = int(input("Step:"))
    ls= []
    while start<end:
        ls.append(start)
        start += step
    print(ls)

