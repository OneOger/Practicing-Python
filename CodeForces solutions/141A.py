# CodeForces
# 141A - Amusing Joke

name1 = input() # First string;
name2 = input() # Second string;
bla = input()   # Third string.

both = name1+name2
countboth = 0
countbla = 0
c = 0

for i in both:
    number = ord(i)
    countboth += number  # By using ord() function sum ASCII code of each character of string 1 and 2 (together);

for i in bla:
    number1 = ord(i)
    countbla += number1  # Same for third string;

for i in both:
    if i in bla:
        if countboth == countbla:
            c+=1
        else:
            c-=10**3
    else:
        c-=10**3

if c > 0:
    print('YES')
else:
    print('NO')