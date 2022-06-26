def check_arm(num,len):
    value=num
    result=0
    while num>0:
        new_num=num%10
        num=num//10
        result+=new_num**len
    if result==value:
        return "Number is Armstrong"
    else:
        return "Number is not Armstrong"

num=int(input())
result=check_arm( num, len(str(num)) )
print(result)