#Exercise1
def bmi(weight,height):
    bmi=weight/(height**2)
    print(f"{bmi:.2f}")
    if 18.5 <= bmi and bmi<= 25:
        print("healthy")
    else:
        print("unhealthy")
bmi(80.5,1.75)

#Exercise2
def reverse_n(n):
    re=0
    temp=n
    while temp!=0:
        remain=temp%10
        re=re*10+remain
        temp=temp//10
    print(n,re)
    if re==n:
        print("The original and reverse number is the same.")
    else:
        print("The original and reverse number is not the same.")
reverse_n(121)

#Exercise3
l=[1,3,4,8,9]
print(sum(l))

#Exercise4
def twoSum(nums, target):
    table={};
    for i,item in enumerate(nums):
        table[item]=i;
    for i,item in enumerate(nums):
        j=table.get(target-item)
        if j is not None and i!=j:
            return [i,j]
print(twoSum([2,7,11,15],9))

#Exercise5
def my_range(start,end,step):
    my_list=[]
    while start<=end:
        my_list.append(start)
        start+=step
    return my_list
print(my_range(1,100,2))
        
        
