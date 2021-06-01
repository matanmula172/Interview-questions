# yearly transaction calculator
def solution(A, D):
    fee = calculate_fee(A, D)
    return sum(A) - fee


def is_month(int_month, date):
    try:
        month = date.split('-')[1]
        if str(int_month) == month or ('0' + str(int_month)) == month:
            return True
    except:
        print("erroneous month")
        return False


def count_month(month, A, D):
    pos_count = 0
    sum_exp = 0
    for i in range(len(D)):
        if is_month(month, D[i]) and A[i] < -0:
            pos_count += 1
            sum_exp += A[i]
    if sum_exp <= -100 and pos_count >= 3:
        return pos_count
    return 0


def calculate_fee(A, D):
    fee = 0
    for i in range(1, 13):
        count = count_month(i, A, D)
        if count < 3:
            fee += 5
    return fee


A = [100, 100, 100]
D = ["2020-12−31", "2020-12-22", "2020-12-03"]

print(solution(A,D))