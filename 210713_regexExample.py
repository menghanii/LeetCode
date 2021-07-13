import re

# 핸드폰 번호 010/011/017/016-0000-0000, 단 2번째/3번째는 0으로 시작하면 안 됨.
phone_pattern = re.compile('[(010)(011)(017)(016)]-?[1-9][0-9]{3}-?[1-9][0-9]{3}')
# phone_pattern =  re.compile('[(0]')
test_string = '01048098701'
print(re.findall(phone_pattern, test_string))