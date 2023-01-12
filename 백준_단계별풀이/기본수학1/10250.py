import sys
sys.stdin = open('10250.txt')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    H,W,N = map(int,input().split())
    now_floor = 1
    check_in = 0
    room_number = 1

    while check_in<N:
        # if H == 1:
        #     check_in += 1
        #     if check_in == N:
        #         floor = 1
        #         room = N


        while now_floor<=H:
            check_in += 1
            # now_floor += 1
            if check_in==N:
                # print(now_floor,room_number)
                floor = now_floor
                room = room_number
                break
            now_floor += 1
        room_number+= 1
        now_floor = 1

    # print(floor,room)
    if room<10:
        print(int(str(floor)+'0'+str(room)))
    # elif floor<10 and room>=10:
    #     print(int(str(floor) + '0' + str(room)))
    else:
        print(int(str(floor) + str(room)))