'''
test = [91,82,73,61,59]
 90 : 참 잘했어요
 80 : 잘했어요
 70 :

# test : 변수
# for, if
'''
'''
test = [91,82,73,61,59]
#print(list(enumerate(test)))
for i, score in enumerate(test):
    if score >= 90:
        print("%d 번째 학생은 참 잘했어요" % i)
    elif score >= 80:
        print("%d 번째 학생은 잘했어요" % i)
    elif score >= 70:
        print("%d 번째 학생은 노력어요" % i)
'''
'''
lst = [1]
print(lst + list(range(2,11,1)))
lst = lst + list(range(2,11,1))
print(lst)
for i in range(2,11,1):

    lst.append(i)
    #print('i =',i, 'list =',lst)
#list()
print(lst)
print(lst)
'''
score = [i for i in range(50,91,10)]  # 주

for i in range(4):
    for x in range(len(score)):
        print("%d 번째" %i, "// 값 : %d" %x)
