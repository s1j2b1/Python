
print('____________________________________________ -+  */  **  ( ) الترتيب ')

print(f"3*4+5: \n{3*4+5} \n")
print(f"3*(4+5): \n{3*(4+5)} \n")

print(f"a: \n{5/2} \n")    # flout
print(f"b: \n{5//2} \n")   # int
print(f"c: \n{5*3} \n")

print(f"d: \n{5**4} \n")
print(f"e: \n{((5*5)*5)*5} \n")

print(f"f: \n{5%3} \n")    # 5/3=> 1,1,1 و باقي 2

print('____________________________________________ مشروع')

# مشروع math
y =  (((2*2)*2)*2)*2
yy=  2**5
print(y)
print(yy)
print("-------------------------")

r = 5//2
rr= 5/2.5
print(r)
print(rr)
print("-------------------------")

q = 5.8%2
print(q)


print('if ____________________________________________')

# tools >  <  >=  <=  !=  ==
# we can use "str" with "str"
if 7:               # 7 tro
    print("Ok")

if 7>5:
    print("I'm big")

if "ali" != "Ali":   # 'a'\'A'
    print('yes')

x="01"
y="10"
if x[0] == y[0]:
    print(f"x:{x}= y:{y}")
else:
    print(f"x:{x[0]}!= y:{y[0]}")

if '1'> x <'11':    # "01" bigger than "1"   تأكد هل يقارن كأرقام ام بالاسكي كود يعي مثلا بدل 1 حط حرف
    print("x=",x)

# if elif  or  if  if
if x==1:
    print('A')
elif x=='1':
    print('B')
elif x=='0':
    print('C')
else:
    print('No one')

# not  or  and
if x and y == '01' or y[1]=='0' :
    print("welcome")


print('____________________________________________ مشروع')

# مشروع اذا الاشتراك اكثر من 24 شهر او العمر اقل من 16 تخفيض 30%

# project input in if
# مشروع input with if shorter
# برنامج امكانية تصويت شخص في الانتخابات اذا اردني و اكبر من 18
country = input("are your country jordan yse or no: ")
age = int(input("enter your age: "))
if country.lower()=="yse" and age>18:
    cand = input("Mention your candidate's name: ")
    print(f"your candidate is {cand}")
else:
    print("sorry, you cannot nominate..")


print('____________________________________________ projects with more than "if" مشروع')

# تحديد درجة الطالب هل أ90 100 / ب 80 90 / ج 70 80 / د 60 70 / درجة غير صالحة
mark = int(input("enter your mark: "))
if 90<=mark<101:
    print("A")
elif 80<=mark<90:
    print("B")
elif 70<=mark<80:
    print("C")
elif 60<=mark<70:
    print("D")
elif 0<=mark<60:
    print("F")
else:
    print("invalid grade")


print('____________________________________________ project user input enter any "if" مشروع')

# input with math longer مشروع 
#  اللعبة   #
# حساب نقاط الاعب  #
# عدد النقاط عدد صحيح  #
#  مستوى الصعوبة *1 *2 * 3 #
# عدد المحاولات غير الصحيحة  #
#  اختيار المستوى عند التسجيل #
#  اذا النتيجة اقل من 0 اجعلها 0 #
#  تكرار اللعبة #
#  اذا تجاوزة 100 اجعلها 100 #
#  المستوى الصعب النقاط-(الاخطاء*3)+10 #
#  اذا المستوى غير صالح اطبع #

mark, bless, error = 0,0,0
import random
level = int(input("select level 1 or 2 or 3: "))

for game in range(5):
    nom1 = random.randrange(1,10)
    nom2 = random.randrange(1,10)
    multiply = nom1*nom2
    #print(multiply)                                   #احذفها بعدين

    #game1
    if level==1:
        answer = int(input(f"\n{nom1}*{nom2}= "))
        if answer==multiply:
            print(answer)
            mark +=1
            bless +=1
        else:
            print(f"{answer} is error try agin")
            mark -=1
            error +=1
        print(f"mark: {mark}")

    # game2
    elif level==2:
        answer = int(input(f"\n{nom1}*{nom2}= "))
        if answer==multiply:
            print(answer)
            mark +=1
            bless +=1
        else:
            print(f"{answer} is error try agin")
            mark -=2
            error +=1
        print(f"mark: {mark}")

    #game3
    elif level==3:
        answer = int(input(f"\n{nom1}*{nom2}= "))
        if answer==multiply:
            print(answer)
            mark +=1
            bless +=1
        else:
            print(f"{answer} is error try agin")
            mark -=3
            error +=1
        print(f"mark: {mark} +10")

    else:
        print("error")
        level = int(input("please select level 2 or 2 or 3: "))

if mark<0:
    mark=0
if mark>100:
    mark=100

if level==3:
    print(f"your error answer: {error}\nyour correct answer: {bless}\nyour mark: {bless+10}")
else:
    print(f"your error answer: {error}\nyour correct answer: {bless}\nyour mark: {mark}")



# projects with more than "and"  "or"  "not"







