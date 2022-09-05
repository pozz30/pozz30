###자료형/연산자/변수

##숫자형, 문자형, 참/거짓형

# print(1)    #자료형?  - 정수형 자료형 (숫자형)
# print(-1)   #자료형?

# print(type(1))

# from re import X
# from tkinter import Y


# print(3.14)
# print(1000000)
# print(10+1)
# print(3-10)
# print(11*11)
# print((4+1)*5)


# 변수, 혹은 어떤 두 수를 x,y라할때

# x*y => 곱하기
# x/y => 나누기
# x//y => 나눈 후 정수 부분의 값
# x%y => 나눈 나머지의 값
# x **y => x의 y 거듭제곱
# -x => 음수 x
# abs(x) => 절대값 X
# x == y => x와 y의 값이 같으면 참, 다르면 거짓
# x != y => x와 y의 값이 다를때 참, 같으면 거짓
# x > y => x가 y보다 클때 참, 아니면 거짓
# x >= y => x가 y보다 같거나 클 때 참, 아니면 거짓
# x < y  
# x<=y
##연산자 예시

# print(2+3)      #5
# print((2+3)+5)  #10

# print(8//3)     #2
# print(8%3)
# print(8/3)
# print(5-8)
# print(abs(-5-8))
# print(3==4)
# print((3==(4-1)) & (4>3))
# print(str((3==(4-1)) & (4>3)))


# print(type((3==(4-1)) & (4>3)))
# print(type(str((3==(4-1)) & (4>3))))

# print(3)
# print(2)
# print(3/2)  #???  1.5 ? 2?

# print(type(2.0))
# print(type(2))

# import math
# print(math.sqrt(4.))  #2
# print(math.log10(10))  #1)
# print(math.factorial(4))  #4! = 24

# print(2+3j)   
# print(complex(2,3))
# print(complex(0,1)**2)
# print(type(2+3j))  #complex?
# print(isinstance(2-4j,float)) #True )

#문자형

# print("I am developer")
# print('using quotation')
# print('happy' * 9)

# x = 'I am developer'
# print(x)
# print(type(x))

#참/거짓형

#and -> a & b
#or -> a | b
# 
# print(True or False)    #True
# print(True and False)   #False
# print(not False)        #True
# print(False | True)     #True
# print(False & True )    #False


# print(isinstance(True, int))
# print(int(True))
# print(isinstance(False, int))
# print(int(False))

#Bool 예시
# print(5<10)
# #참
# print(5>10)
# #거짓
# print(True)
# #참
# print(not True)
# #거짓
# print(False)
# #거짓
# print(not (5>10))
#참


#부정자료형 - none형
# print(type(None))

# x = 2
# print(x is None)
# print(x is not None)

# y = None
# print(y is None)

# large_num = None

# for number in [1,2,3,4]:
#     if number>10:
#         large_num = number
#         break

# if large_num is None:
#     print("The list did not contain any number larger than 10")



###변수###


from tkinter import N


name = "Brian"  #name이 변수 이름이고, brian이 해당 변수가 가르키는 값
grade = 92  # grade이 변수 이름이고, 92점이 해당 변수가 가르키는 숫자 값
failing = False


var = 92
_var = 92
homework = 92
var21 = 92

#for, while, break, pass, continue, elif, import, from, as, try, except



#Mutable: 리스트, 딕셔너리(사전), 집합(세트), 배열(array, numpy)
#Immutable: 숫자, 문자열, 튜플


# x = [1,2,3]
# print(x)
# x[0] = -4
# print(x)

# x = (1,2,3)
# x[0] = -4

#증분 대입문 
x = 5
#x = x+1
x+=1
print(x)

x+=n ---> x=x+n  
x//=n   ---> x=x*n  