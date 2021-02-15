w = input()
matched = 0

while True:
    text = input().split()
    if text[0] == "END_OF_TEXT":
        break
    for t in text:
        if w.lower() == t.lower():
            matched += 1

print(matched)