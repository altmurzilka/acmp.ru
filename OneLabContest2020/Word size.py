'''
You are given a text.
Print the length of each word in given text.
Example
standard input
Alik Ayana Dias Elvira
standard output
4 5 4 6
'''

arr = []
a = list(map(str, input().split()))

for i in a:
    arr.append(str(len(i)))
print(' '.join(arr))
