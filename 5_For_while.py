'''
print('for ____________________________________________')

# for (i=0 , i<4 , i++)
for i in range(4):
    print(i)

for i in range(2,5):
    print(i)

for i in range(-2,10,2):
    print(i)

for i in "sulaiman":
    print(i)

name= input("Enter your name: ")
for i in name:
    print(i)

for i in range(5):
    print(i*"*")


print('____________________________________________ مشروع الاعداد الفردية')

# المستخدم يحدد رقم و اخبره هل زوجي ام فردي
num = int(input("enter integar number at 0 to 100: "))
if 0 <= num < 101:
    for i in range(0,101,2):
        if num == i:
            print(f"{num} is even num")

if 1 <= num < 101:
    for x in range(1,101,2):
        if num == x:
            print(f"{num} is odd num")

'''

x= [[[[0,1,2],[3,4,5]],[[6,7],[8,9,10]]],[[[11,12,13],[14,15]],[[16,17,18],[19,20]]]]
# ملاحظ يستحسن ان لا تستخدم نفس الحرف
for i in x:
    for i in i:
        # print(i)
        for i in i:
            print(i)

print('____________________________________________ مشروع')

# project print from list with out any [] ,


name1= "Ali"
for i in range(len(name1)):  # len=> 3
    print(i*'*')             # i first one is 0*'*'

my_dict= {'a':1,
          'b':2}
for x,y in my_dict.items():
    print(x,y)
    print(y)
print('\n')


print('while ____________________________________________')

loop_num= -2

x=0
while x < 5:
    x+=1
    # print(x+1)
    print(x)

print('\n')

# هنا تغيرت قيمة x في while الي قبل
while x < 11:
    x+= 1
    print('a',x)

# عادي المتغير ما يكون مباشرة قبل while
while loop_num < 5:
    print(loop_num)
    loop_num += 1


while_x = 1
while while_x < 5:
    my_password= '321'
    password= input("Enter password: ")
    if password == my_password:
        print("welcome")
        break
    else:
        print("try again")

print('\n')

y= 0
while y < 5:
    y += 1
    print(y)
    if y == 2 or 4:
        continue

while True:
    ...    


print('____________________________________________ مشروع')


# مشروع while
# لعبة تخمين للمستخدم ان يخمن ثلاث مرات
x=1
answer= 3
cc= ''
while x < 4:
    guess = int(input(f"{cc}guess number between 0 to 10: "))
    if guess == answer:
        print("win")
        x=4
    else:
        x += 1
        cc= 'try again '
        guess = int(input("try again guess number in 0 to 10: "))



# مشروع while
# برنامج يطلب ادخال كلمة مرور بشكل دائم الى ان يدخل الكلمة الصحيحة ب while
p = "sulaiman"
passw = input("enter the password: ")
x = True
while x:
    if passw == p:
        print(f"passworld \"{passw}\" is true")
        x = False
    else:
        passw = input("try again enter the password: ")


print(' ____________________________________________ مشاريع')

# مشروع while math
# # التأكد ما اذا كان الرقم اوليا 
while True:
    c= int(input("num: "))
    if c>1:
        for i in range(2, int(c**0.5)+ 1):
            print(c)

x = {1:0,2:0,3:0,4:0,5:0}

print(x)




# مشروع for , if
# برنامج يطبع الارقام الزوجية بين 1 و 50 ب for , if
for i in range(1,51):
    if i%2==0:
        print(i)

# مشروع for , if
# برنامج يطلب 5 ارقام و يطبع اكبر رقم ب for , if بالطريقة الثانية
y3= []
t3=0
for i in range(0,5):
    x3= int(input("num: "))
    y3.append(x3)
    for z3 in y3:
        if t3<x3>z3:
            t3=x3
print(y3)
print(t3)


# مشروع for , if
# برنامج يطلب 5 ارقام و يطبع اكبر رقم ب for , if
num = input("enter 5 num between 0 to 9: ")
print(num)
xnum = [*num]
print(xnum)
if len(xnum)>5:
    del xnum[5:]
    print(xnum)
b='0'
for i in xnum:
    if i>b:
        b=i
print(b)


# مشروع for , if list
# لعبة تخمين للمستخدم ان يخمن ثلاث مرات ب list
x1= [4,2,5]
a1= 0
while a1<3:
    y1 = int(input("think mun: "))
    for i in x1:
        if y1==i:
            print("win")
            a1= 3
    a1+=1


# مشروع for
# حذف الارقام المتشابهة
x2 = [1,2,3,2,2,4,5,6,4,8,9,9]
for i in x2:
    if x2.count(i)>1:
        r=x2.count(i)
        for R in range(1,r):
            x2.remove(i)
    print(x2)
print(f"--------------------\n{x2}")



# مشروع [] , for
# **tuple** index() جد موقع كلمة دون استخدام
# list_name = ('mohamad' , 'saliam' , 'omar' ,'kahlid' ,'sami')
# ind=0
# check_nam= input('enter name: ')
# for i in list_name:
#     ind+=1
#     # print(ind)
#     if check_nam==i:
#         print(ind)

