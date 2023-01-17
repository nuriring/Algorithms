a = [1,2,3,4]
b = [3,4,1,2]
if a==b:
    print("같다")


def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

print(func_c(a,b))


def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n % multi_day) * multi_day_price + (n // multi_day) * one_day_price


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
one_day_price1 = 3
multi_day1 = 5
multi_day_price1 = 14
n1 = 6
ret1 = solution(one_day_price1, multi_day1, multi_day_price1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

one_day_price2 = 2
multi_day2 = 3
multi_day_price2 = 5
n2 = 11
ret2 = solution(one_day_price2, multi_day2, multi_day_price2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")