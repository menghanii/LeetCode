string = input()
digit = 0
alpha = []
for st in string:
    if st.isdigit():
        digit += int(st)
    else:
        alpha.append(st)
alpha.sort()
print(''.join(alpha)+str(digit))
