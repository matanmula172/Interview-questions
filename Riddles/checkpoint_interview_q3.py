# 1386. Cinema Seat Allocation
def get_reserved_seats(S):
    if S == "":
        return [[]]
    arr = str(S).split(' ')
    res_seats = []
    for i in range(len(arr)):
        col = ord(arr[i][-1]) - 64
        row = int(arr[i][:len(arr[i]) - 1])
        res_seats.append([row, col])
    return res_seats


def solution(N, S):
    reserved_seats = get_reserved_seats(S)
    reserved_seats.sort()
    if reserved_seats == [[]]:
        return 2*N
    result, i = 2 * N, 0
    while i < len(reserved_seats):
        reserved = [False] * 3
        curr = reserved_seats[i][0]
        while i < len(reserved_seats) and reserved_seats[i][0] == curr:
            col = reserved_seats[i][1]
            if 2 <= col <= 5:
                reserved[0] = True
            if 4 <= col <= 7:
                reserved[1] = True
            if 6 <= col <= 9:
                reserved[2] = True
            i += 1
        if not reserved[0] and not reserved[2]:
            continue
        if not all(reserved):
            result -= 1
            continue
        result -= 2
    return result

N = 3
S = "1A 1F 3K 2B"
print(solution(N, S))
