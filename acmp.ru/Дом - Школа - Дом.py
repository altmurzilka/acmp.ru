location = input()
n = int(input())

if location == 'School' and n%2 != 0 or location == 'Home':
    print("Yes")
else:
    print("No")
