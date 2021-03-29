import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--decimal", dest="decimal", action="store") # store : 추가 옵션을 받는 경우
parser.add_argument("-f", "--fast", dest="fast", action="store_true") #store true : 옵션의 유무만 필요한 경우
args = parser.parse_args()

print(args.decimal)
print(args.fast)