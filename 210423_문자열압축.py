string = input()
length_list = [] # 문자열 단위로 압축했을 때의 length를 담는 리스트
min_str_num = len(string)
if len(string) == 1:# Edge Case : 'a'
    print(len(string))
else:
    for window_size in range(1, len(string)//2 + 1): # 문자열 단위 (1개단위, 2개단위, ...)
        temp = []
        for i in range(len(string)//window_size + 1): # ex) 길이 16 // 7개 단위 == 2번 잘림. +1은 자투리 문자열도 넣어주기 위해서.
            temp.append(string[i * window_size : (i+1) * window_size])
            if temp[-1] == '': # 나누어떨어지는 경우에는 ''
                temp.pop()
        temp.append('END') # END Flag

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