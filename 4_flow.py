# num_health = 90

# if num_health > 80:
#     status = "good"
# if num_health > 50 & num_health <= 80:    # 50 < num_health <= 80
#     status = "okay"
# elif num_health > 0:     #  0 < num_health <= 50
#     status = "danger"

# x = -1
# my_list = [1 if x >=0 else 0]
# print(my_list)

#for문 / while 문 / 반복문

# for <var> in <iterable>:
#     block of code  #for문의 body

# total = 0
# for item in [1,3,5]:
#     total = total + item
#     print(total)
#     #total += 

# print(total)

# while <condition>:
#     block of code  #while문의 body

# total = 0
# while total < 2:
#     print("step")
#     total += 1

# print(total)

#break,continue

#break
# for item in [1,2,3,4,5]:
#     if item ==3:
#         print(item, "...break!")
#         break
#     print(item, ",,,next iteration!")

# x = 1
# while x < 4:
#     print("x = ", x, ">> enter loop-body <<")
#     if x == 2:
#         print("x = ", x, "continue...back to the top of the loop!")
#         x += 1
#         continue
#     x += 1
    
# print("...reached end of loop-body--")

#iterable 의 예시 : list, tuple, string

[0, None, -2, 1]  #list as iterable
"hello out there" #string as iterable
("a", False, 0, 1) #tuple as iterable

# for <var> in <iterable>:

#iterable built-in 함수

#list: iterable의 member들로 이뤄진 list를 생성하여 반환함
# a = "I am a member"
# print(list(a))

# #tuple: iterable의 member들로 이뤄진 tuple를 생성하여 반환함
# print(tuple(a))

# #sum : iterable의 member들을 더해줌
# a = [1,2,3]
# print(sum(a))

# #sorted: iterable의 member들을 정렬한 list를 반환함
# a = "I am a member"
# print(sorted(a))

# #any: iterable의 member들 중 하나라도 bool의 결과값이 True이면 바로 True를 반환함
# print(any((0, None, [], 0)))
# print(any((1, None, [], 0)))

# #all: iterablem의 모든 member들에 대해 bool의 결과값이 True일때 True를 반환함
# print(all((0, None, [], 0)))
# print(all((1, True, [0,1], "hi")))

# #min: iterable의 최소값 member 값을 반화함
# print(min("hello"))

# #max: iterable의 최대값 member 값을 반화함
# print(max("hello"))
# print(max([0,1,2,1000]))

# #unpacking iterables

# my_list=[7, 9 , 11]
# # x = my_list[0]
# # y = my_list[1]
# # z = my_list[2]

# #--> unpacking
# x,y,z = my_list
# print(x,y,z)

# enumerating
# for entry in  enumerate("abcdef"):
#     print(entry)