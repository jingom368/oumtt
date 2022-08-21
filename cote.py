# o 1. 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
answer=('*'*a+'\n')*b
print(answer)

# o 2. x만큼 간격이 있는 n개의 숫자
x, n = -4,2

def solution(x, n):
    answer = range(x, x*(n+1), x)
    return list(answer)

def solution(x, n):
    return [x*(i+1) for i in range(n)]
    
solution(-4,2)

# o 3. 행렬의 덧셈
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer

# o 4. 핸드폰 번호 가리기
phone_number = "01033334444"
len(phone_number[0:-4])*'*'+phone_number[-4:]
def solution(phone_number):
    answer = len(phone_number[0:-4])*'*'+phone_number[-4:]
    return answer

# o 5. 하샤드 수
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0 

# o 6. 평균 구하기
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

# o 7. 콜라츠 추측
def solution(num):
    index = 0
    while(num != 1):
        if num % 2 == 0:
            num = num/2
            index += 1
        else:
            num = num*3+1
            index += 1
        if index > 500:
            index = -1
            break
    return index

# o 8. 최대공약수와 최소공배수
def solution(n, m):
    s, l = n, m
    while(l%s != 0):
        if s>l: 
            s, l = l, s
        if l%s != 0:
            l, s = l-s, s
    return [s, int(n*m/s)]

def gcdlcm(a,b):
    c, d = max(a,b), min(a,b)
    t = 1
    while(t>0):
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer 

# o 9. 짝수와 홀수
def solution(num):
    return "Even" if num%2==0 else "Odd"

# o 10. 제일 작은 수 제거하기
def solution(arr):
    if len(arr) != 1:
        arr.remove(min(arr)) 
    else:
        arr = [-1]
    return arr
  
# o 11. 정수 제곱근 판별
from cmath import nan
import math
from queue import Empty
def solution(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return math.pow((math.sqrt(n)+1),2)
    else:
        return -1

# o 12. 정수 내림차순으로 배치하기
def solution(n):
    answer = ''
    for number in sorted(str(n), reverse=True):
        answer += number 
    return int(answer)

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

# o 13. 자연수 뒤집어 배열로 만들기
def solution(n):
    return [int(i) for i in list(reversed(str(n)))]

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# o 14. 자릿수 더하기
def solution(n):
    return sum([int(i) for i in str(n)])

# o 15. 이상한 문자 만들기
def solution(s):
    return " ".join(["".join([i[j].lower() if j%2 == 1 else i[j].upper() for j in range(len(i))]) for i in (s).split(' ')])

def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), "try hello world".split(" ")))

# o 16. 약수의 합
def solution(n):
    return sum([i+1+int(n/(i+1)) if n%(i+1) == 0 and n/(i+1) != int(n**(1/2)) else (i+1+int(n/(i+1)))/2 if n%(i+1) == 0 and n/(i+1) == int(n**(1/2)) else 0 for i in range(int(n**(1/2)))])

def solution(n):
    return n + sum([i for i in range(1, n//2+1) if n%i == 0])

# x 17. 시저 암호
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def solution(s, n):
s = "a B z"

def toWeirdCase(s):
    return 
"".join(map(lambda x: [k if x==v else ' ' if x==' ' else '' for k,v in alpha_enumerate], list(s.lower())))
alpha_enumerate = [[key, value] for key, value in enumerate(alpha)]
[(k+4)%26 for i in s.lower() for k,v in alpha_enumerate if i==v]


# o 18. 문자열을 정수로 바꾸기
def solution(s):
    return int(s[0]+s[1:] if s[0] == '+' or s[0] == '-' else s)

def strToInt(str):
    a = int(str)
    return a

# 19. 수박수박수박수박수박수?
def solution(n):
    return "".join([['수', '박'][i%2] for i in range(n)])

def water_melon(n):
    s = "수박" * n
    return s[:n]

# 20. 소수 찾기
def is_prime(n):
    sieve = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * 2, n+1, i):
                sieve[j] = False
    return primes
is_prime(100)

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 21. 서울에서 김서방 찾기
def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"

# 22. 문자열 다루기 기본
def solution(s):
    if len(s) == 4 or len(s) == 6:
            if s.isdigit() == True:
                return True
            else:
                return False
    else: 
        return False

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 23. 문자열 내림차순으로 배치하기
def solution(s):
    return "".join(sorted(s, reverse=True))

# 24. 문자열 내 p와 y의 개수
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

# 25. 문자열 내 마음대로 정렬하기
def solution(strings, n):
    return sorted(strings, key=lambda x:x[n])

# 26. 두 정수 사이의 합
def solution(a, b):
    return sum([i for i in range(min(a,b),max(a,b)+1)])
    
# 27. 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = sorted([i for i in arr if i%divisor==0]) 
    if len(answer) == 0:
        return [-1]
    return answer

def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

# 28. [1차] 다트 게임
import re

def solution(dartResult):
    dart_num = re.findall("1?[0-9]", dartResult)
    dart_bonus = re.findall("[A-Z]\W?", dartResult)
    alpha = {"S":1,"D":2,"T":3}
    point = [int(dart_num[i])**(alpha[dart_bonus[i][0]]) for i in range(3)]
    for i in range(3):
        if re.findall("\W", dart_bonus[i]) == ['*']:
            point[i] = point[i] * 2
            if i == 1 or i == 2:
                point[i-1] = point[i-1] *2
        elif re.findall("\W", dart_bonus[i]) == ['#']:
            point[i] = point[i] * (-1) 
    return sum(point)
    
# 29. 가운데 글자 가져오기
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]

# 30. [1차] 비밀지도
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
import re
def solution(n, arr1, arr2):
    a = [format(i, 'b').zfill(n) for i in arr1] 
    b = [format(j, 'b').zfill(n) for j in arr2]
    answer = ["".join(['#' if a[i][j] == '1' or b[i][j] == '1' else ' ' for j in range(n)]) for i in range(n)]
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

# 31. 부족한 금액 계산하기

def solution(price, money, count):
    return price*count*(count+1)/2 - money if money <= price*count*(count+1)/2 else 0

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 32. 나머지가 1이 되는 수 찾기
def solution(n):
    return min([i for i in range(2,n) if (n-1)%i == 0])
    
# 33. 2016년
week = {1:"SUN", 2:"MON", 3:"TUE", 4:"WED", 5:"THU", 6:"FRI", 0:"SAT"}
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def solution(a, b):
    return week[(sum(month[:(a-1)])+5+b)%7]

# 34. 두 개 뽑아서 더하기
def solution(numbers):
    return sorted(list(set([numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i<j])))

# 35. 예산
d, budget = [1,3,2,5,4], 9
while(budget>0):
    budget = budget-min(d)
    d.remove(min(d))
    print(budget)
    print(d)
def solution(d, budget):
    answer = len(d)
    while (budget>0) and (d != []):
        budget = budget-min(d)
        if budget <= 0:
            break
        d.remove(min(d))
    return answer-len(d)+1
solution([2,2,3,3], 10)

## 올바른 괄호

def solution(s):
    answer = [s[i] for i in range(len(s))]
    return answer

## 배달
N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3

road_n = sorted([[road[i][0],road[i][1],road[i][2]] for i in range(len(road))], key=lambda x:(x[0], x[1]))
road_w = [[road_n[i][0],road_n[i][1]] if road_n[i][0] <= road_n[i][1] else [road_n[i][1], road_n[i][0]]  for i in range(len(road_n))]
Road = [[road_n[i][0],road_n[i][1],road_n[i][2]] if road_n[i][0] <= road_n[i][1] else [road_n[i][1], road_n[i][0],road_n[i][2]]  for i in range(len(road_n))]



[road_n[i][j] for i in range(len(road_n)) for j in range(len(road_n[0]))]
[[road[i][2] for i in range(len(road))]]



#### 행렬과 연산
import copy
rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
def ShiftRow(rc):
    return list(map(lambda x:x[1],sorted([[(k+1)%len(rc),v] for k,v in enumerate(rc)], key=lambda x:x[0])))

def Rotate(rc):
    rc_new = copy.deepcopy(rc)
    rc_new[0][1:] = [i for i in rc[0]][:-1]
    rc_new[-1][:-1] = [i for i in rc[-1]][1:]
    for j in range(0,len(rc)-1): 
        rc_new[j+1][-1] = [rc[i][-1] for i in range(len(rc))][:-1][j]
        rc_new[j][0] = [rc[i][0] for i in range(len(rc))][1:][j]
    return rc_new

def solution(rc, operations):
    for i in operations:
        rc = ShiftRow(rc) if i =="ShiftRow" else Rotate(rc) 
    return rc
solution(rc, ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])