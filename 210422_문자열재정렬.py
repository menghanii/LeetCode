string = input()
digit = []
alpha = []
for st in string:
    if st.isdigit():
        digit.append(int(st))
    else:
        alpha.append(st)
alpha.sort()
print(''.join(alpha) + str(sum(digit)))
