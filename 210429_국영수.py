import sys
sys.stdin = open('input.txt','r')
num = int(input())

name_and_score= []

for i in range(num):
    info = input().split()
    name_and_score.append([info[0], int(info[1]), int(info[2]), int(info[3])])

name_and_score.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in name_and_score:
    print(i[0])
