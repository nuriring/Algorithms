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