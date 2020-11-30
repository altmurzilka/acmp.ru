a, b, c = map(int, input().split())

string = ''

if a == 0 and b == 0 and c == 0:
    string += '0'

if a != 0:
    string += str(a)
if b != 0:
    if b>0:
        if not string:
            if b == 1:
                string += 'x'
            else:
                string += str(b)
                string += 'x'
        else:
            string += '+'
            if b == 1:
                string += 'x'
            else:
                string += str(b)
                string += 'x'
    else: 
        if b == -1:
            string += '-x'
        else: 
            string += str(b)
            string += 'x'
if c != 0:
    if c>0:
        if not string:
            if c == 1:
                string += 'y'
            else: 
                string += str(c)
                string += 'y'
        else: 
            string += '+'
            if c == 1:
                string += 'y'
            else: 
                string += str(c)
                string += 'y'
    else: 
        if c == -1:
            string += '-y'
        else: 
            string += str(c)
            string += 'y'

print(string)
