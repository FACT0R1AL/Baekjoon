flag = False

while True:
    nums = [1] * 11
    nums[0] = 0

    while True:    
        num = int(input())

        if (num == 0):
            flag = True
            break

        answer = input()

        if (answer == "too low"):
            for i in range(1, num+1):
                nums[i] = 0
        
        elif (answer == "too high"):
            for i in range(num, len(nums)):
                nums[i] = 0

        elif (answer == "right on"):
            if (nums[num] == 0):
                print('Stan is dishonest')
                break
            else:
                print('Stan may be honest')
                break
            
    if (flag): break