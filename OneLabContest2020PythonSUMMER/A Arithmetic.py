'''
You are given an array of elements of size N.
You need to find the arithmetic mean of all even numbers at all odd indexes in array.
Output
Print the average value with 6 digits after decimal part
Examples
standard input
7
1 2 3 4 5 6 7
standard output
0
standard input
8
62 94 92 96 10 43 63 80
standard output
54.666667
Note
Array indexing starts with 1.
[62, 92, 10] All even numbers placed at odd indexes in array.
Average value = (62+92+10)/3 = 54.666667
To print double with given precision write following code : cout ¾ fixed ¾ set precision(6) ¾ d; where d is your answer
'''

n = int(input())
a = list(map(int, input().split()))
count = 0
avg = 0
for i in range(0, len(a), 2):
    if a[i]%2 == 0:
        avg += 1
        count += a[i]
if avg == 0:
    print(0)
else: print("{:.6f}".format(count/avg))
