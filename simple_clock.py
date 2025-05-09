def timeInWords(h, m):
    # Write your code here
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if (m==0):
        return numbers[h-1]+ " o' clock"
    elif (m==15):
        return "quarter past " + numbers[h-1]
    elif (m==30):
        return "half past " + numbers[h-1]
    elif (m==45):
        return "quarter to " + numbers[h]
    else:
        if (m==1):
            return "one minute past " + numbers[h-1]
        elif (m<=20):
            return numbers[m-1] + "minutes past " + numbers[h-1]
        elif (20 < m and m <30):
            ones = m % 10
            return "twenty " + numbers[ones-1] + " minutes past " + numbers[h-1]
        else:
            new_m = 60-m
            if (new_m==1):
                return "one minute to " + numbers[h]
            elif (new_m<=20):
                return numbers[new_m-1] + " minutes to " + numbers[h]
            else:
                ones = new_m % 10
                return "twenty " + numbers[ones-1] + " minutes to " + numbers[h]
            
h,m = map(int, input().split())
print(timeInWords(h,m))