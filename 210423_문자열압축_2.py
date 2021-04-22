string = input()
length_list = [] # 문자열 단위로 압축했을 때의 length를 담는 리스트
for window_size in range(1, len(string)//2 + 1): # 문자열 단위 (1개단위, 2개단위, ...)
    temp = [string[i:i+window_size] for i in range(0, len(string), window_size)] + ['END']
    compressed_str = ''
    cnt = 1
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            cnt += 1
        else:
            if cnt == 1:
                compressed_str += temp[i] 
            else:
                 compressed_str += str(cnt) + temp[i]
            cnt = 1
    length_list.append(len(compressed_str))
print(min(length_list))