# 071203-456789

while True:
    number = input("주민등록번호를 입력해주세요:")

    if number[6] == "-":
        break
    else:
        print("다시 입력해주세요!")

temp = ""
if number[0] == '0' or number[0] == '1' or number[0] == '2':
    temp = '20' + number[0] + number[1] + "년생"

    if number[7] == '3':
        temp += " 남자"
    elif number[7] == '4':
        temp += " 여자"

else:
    temp = '19' + number[0] + number[1] + "년생"

    if number[7] == '1':
        temp += " 남자"
    elif number[7] == '2':
        temp += " 여자"

print(temp)
