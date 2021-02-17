#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh


s = 'azcbobobegghakl'
longest = ''

for i in range(0, len(s)):
    string = s[i]
    key = i
    while key + 1 < len(s) and ord(s[key]) <= ord(s[key+1]):
        string += s[key+1]
        key += 1
    if len(string) > len(longest):
        longest = string

print("Longest substring in alphabetical order is: ", longest)
