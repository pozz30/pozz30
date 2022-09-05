#print(type("hello"))  
#print(isinstance("83",str)) #True
#print(isinstance(83,str))  #False

#문자 자료형은 변경 불가능한 객체이다

#sentence = "The cat is in the hat."
#print(sentence[0])  #sentence라는 변수명을 가진 문자열의 첫번째 인덱스 (파이썬에선 0번째 인덱스) 값을 호출함

#문자자료형은 시퀀스 자료형입니다.
#시퀀스 자료형은 문자 자료형 외에 리스트, 튜플 자료형 등이 있습니다.

#enter
#\n
#tab
#\t

print("hello,,,,\n,,,,\t bye")


#파이썬 문자열 형식 지정, 형식화 구문
# https://pyformat.info

#format를 사용해 자리 표시자를 값으로 대체
# print("{name} is {age} years old".format(name="Bruce", age="80"))

# #8자 이상이 되도록 선행 공백으로 문자열을 채우기
# print("{item:>8}".format(item="banna"))

#f-문자열
# batman = 12
# catwoman = 10
# print(f"Batman has {batman} apples. Catwoman has {catwoman} apples. Together, they have {batman+catwoman} apples")

# x = 7.0
# print(f"x is a {type(x)} - number. Its value is {x}. The statement 'x is greater than 5' is {x>5}")


#Quiz) 변수를 왜 이용할까?

# print("저희 회사의 구성원을 소개합니다~")
# print('저희 개발회사의 이름은 파이썬이에요')
# print('저희 회사 파이썬의 CEO 이름은 홍길동이며, 개발자 출신입니다')
# print('저희 회사의 구성원은 30명입니다.')


# company_name= '파이썬'
# ceo_name = '홍길동'
# ceo_area = '개발자'
# emp_number = 31

# print("저희 회사의 구성원을 소개합니다~")
# print("저희 개발회사의 이름은 "+company_name+'이에요')
# print('저희 회사 '+company_name+'의 CEO 이름은 '+ceo_name+'이며, '+ceo_area+'출신입니다')
# print('저희 회사의 구성원은 '+str(emp_number)+'명입니다.')

#LIST (목록 자료형)
#대ㅔ괄호를 사용하여 리스트를 생성할 수 있습니다.

# list_ex = [3, 3.5, None, True, 'Hello']
# print(isinstance(list_ex, list))



# list_empty = []
# print(list_empty)

# list_one = ["hello"]
# print(list_one)

# x= "hello"
# list_ex2 = [2<3, x.capitalize(), 5**2, [1,2]]

# print(list_ex2)

# print(list("apple"))

# a = [1, "example", True]
# b = [1, True, "example"]

# print(a == b)


#인덱싱, 슬라이싱

# x = [2, 4, 6, 8, 10]
# print(len(x))   #리스트의 크기를 반환

# print(x[0])
# print(x[1])  #인덱싱


# print(x[1:4])  #슬라이싱


#리스트는 변경 가능한 객체의 예시

# x = [2,4,6,8,10]
# y = [2,4,6,8,10]

# x[1] = "apple"
# print(x)

# #append, extend

# x = [2,4,6,8,10]
# x.append("string")
# print(x)
# x = [2,4,6,8,10]
# x.extend(["True"])
# print(x)



#pop
# x = [2,4,6,8,10]
# # print(x)
# # print(x.pop(1))
# # print(x)
# #remove

# x = ['a', 'b', 'c', 'd']
# print(x.remove('d'))
# print(x)

#시퀀스의 예시
# #list
# x = ['a', 'b', 'c', 'd']
# #문자열
# "hello my name is peter"
# #tuple
# ('a', False, 0 ,1)
# #Numpy Array
# x = numpy.ndarray([0.2, 0.4])


#시퀀스 유형끼리는 공통된 인터페이스, 내부 기능을 공유한다!

#튜플 / tuple


# x = (1, "a", 2)
# print(x)
# print(type(x))

# y = (3,)
# print(y)
# print(isinstance(y, tuple))

# list vs tuple
# list -> 변경 가능한 자료형
# tuple -> 변경 불가능한 자료형

# x = [1, "developer", None]
# y = (1, "developer", None)
# print(x)
# print(y)

# print(x[0:1])
# print(y[0:1])

# x[0] = True
# print(x)

# y[0] = True


#튜플 자료형 변환
# x = [2,4,8]
# y = "apple"
# print(tuple(x))
# print(tuple(y))


#객체가 시퀀스 내에 포함되어있는 값인지 확인하는 방법 : obj in seq

# x= (1,3,5,'a')
# y= [1,3,5,'a']
# z= 'apple'

# print('a' in x)
# print('a' in y)
# print('a' in z)

#시퀀스를 합치는 방법 : seq1+seq2
# x= (1,3,5,'a')
# y= (2,4,6)
# z = x+y
# print(z)


#시퀀스 인덱싱
# x = "abcdefg"
# print(x[0])

#시퀀스 슬라이싱
# print(x[0:3])  #x[0, 1, 2]

#시작 인덱스
#끝 인덱스
#단계적 크기

# seq = "abcdefg"
# print(seq[0:4:1])  #start: 0 , stop: 4, step:1
# print(seq[1:4:1])
# print(seq[0:5:1]) 
# print(seq[0:5:2])
# print(seq[0:0:1])
# print(seq[:])
# print(seq[::2]) 
# print(seq[::-1])
# print(seq[-2:])
# print(seq[:-2])

#슬라이싱 령어
#seq[start:stop:step]  #파이썬이 기본적으로 제공하는 슬라이싱 
# print(seq[slice(0,3,1)])
# print(seq[0:3:1])
