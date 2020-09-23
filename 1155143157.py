#just sharing as tutor allowed owo

#Tutor2ex1
height = 1.75
weight = 80.5

bmi = weight / height / height
# bmi = weight / (height ** 2)
print("bmi = {:.2f}".format(bmi))
if (bmi >= 18.5) and (bmi <= 25):
    print("Healthy")
else:
    print("Unhealthy")
    
#Tutor2ex2
def checkreverse(num):
    print("original number {:d}".format(num))
    strnum = list(str(num))
    rev = list(reversed(strnum))
    if strnum == rev:
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not the same")
checkreverse(121)
checkreverse(125)

#Tutor2ex3
intset = [1,3,4,8,9]

print(intset)
print(sum(intset))

#Tutor2ex4
numset = [2,7,11,15]
target = 9
def findsolution(numset, target):
    Found = False
    for i in range(len(numset)):
        if Found == True:
            break
        for j in range(len(numset)):
            if (numset[i] != numset[j]) and (numset[i] + numset[j] == target):
                Found = True
                a = i
                b = j
                print("[{:d}, {:d}]".format(a, b))
                break
    if Found == False:
        print("Not found")
findsolution(numset, target)
