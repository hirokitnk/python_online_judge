s = input()
p = input()

i = 0

result = False

while i < len(s):
    if s.startswith(p):
        result = True
        break
    i += 1
    s = s[-1] + s[0:len(s)-1]

if result:
    print("Yes")
else:
    print("No")