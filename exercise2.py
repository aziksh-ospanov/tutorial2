num = input("original number ")
reverse = True

for i in range(len(num)):
    if num[i] != num[len(num)-i-1]:
        reverse = False

if reverse == True:
    print("The original and reverse number is the same")
else:
    print("The original and reverse number is not the same")
    
