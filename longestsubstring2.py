#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh


s = 'azcbobobegghakl'
longest = ''

for i in range(0, len(s)):
    temp = s[i]
    key = i
    while key + 1 < len(s) and ord(s[key]) <= ord(s[key+1]):
        temp += s[key+1]
        key += 1
    if len(temp) > len(longest):
        longest = temp

print("Longest substring in alphabetical order is: ", longest)
