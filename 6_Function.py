
print('def ____________________________________________')

def students():
    print("Ahmad")
    print(5+6)

students()

# ممكن نسأل شات اشان نعرف "البراميتر" المطلوبة لان في البعض ما تظر او من الموقع "python"
def studentss(x,y):        # القيم المطلوبة تسمى "برامتر"
    print("Ahmad")
    print(x+y)

studentss(2,10)      # القيم التي ندخلها تسما "ارجمنت"

def full_name(first_name,last_name,tribe):
    first_name= first_name.title()
    last_name= last_name.title()
    tribe= tribe.title()

    print(first_name,last_name,tribe)

full_name('sulaiman','khalid','alriyami')
full_name(tribe= 'al husayn',first_name= 'mohamed',last_name= 'hasan')

# نستخدم هذه الطريقة عندما نريد انشاء فنكشن
# نعلم انها ستحتوي على ثلاث قيم ولاكننا لم نقرر بعد كيف تعمل
def A(x,y,z):
    pass
    ...
A(1,2,3)  # اذا كانت الفنكشن تطلب قيم فيجب ادخالها

print('____________________________________________ مشروع ')

# مشروع def
# اكتب كودًا يعرض قائمة طعام المطعم
# ثم يسأل المستخدم إذا كان يريد طلب طعام
# وبعد ذلك يختار المستخدم فئة من الفئات المتاحة
# وتكرر نفس العملية للمشروبات والحلويات
# وأخيرًا يحسب إجمالي الفاتورة
def menu_show(customer_enter):
    food_num = 0
    for i,z in customer_enter.items():
        food_num+=1
        print(f"{food_num}-{i} {z}$")
    customer= int(input("Enter your choice number: "))

    food_num = 0
    for i in customer_enter.values():
        food_num += 1
        if customer == food_num :
            cost=i
            print(cost,"cost")
            global customer_cost
            customer_cost+= cost
            return customer

food_menu={"burger":5,"pizaa":10,"fries":15}
drink_menu= {"juice":5, "coffee":10, "water":1}
sweet_menu= {"cake":10, "chocolate":20, "fruit":15}
menu_list= {1:'food_menu' , 2:'drink_menu' , 3:'sweet_menu' }

customer_cost= 0
while True:
    print(f"1-food_menu\n2-drink_menu\n3-sweet_menu\n4-cost")
    customer= int(input("Enter your choice number: "))
    if customer == 1:
        menu_show(food_menu)
    elif customer == 2:
        menu_show(drink_menu)
    elif customer == 3:
        menu_show(sweet_menu)
    elif customer == 4:
        print(f"Total cost {customer_cost}$")
        finish_or= input("Do you want anything another yes or no: ")
        if finish_or.lower() == "no":
            break
    else:
        print("pleas enter number from menu!")


print("'*' '**' ____________________________________________")

def my_hobbise(name, *hobbise):     # عندما تضيف "*" ممكن تدخل عدة قيم و يعتبرهن "tuple" و ممكن تستدم على هذا الاساس
    print(name)
    print(hobbise)                  # نتأكيد انه يعتبرها "tuple"
    for i in range(len(hobbise)):
        print('best hobbies mine',hobbise[i])

print('*'*20)
my_hobbise('ali',"play game",'sport')

def my_business(name, age, **money): # عندما تضيف "**" ممكن تدخل عدة قيم و يعتبرهن "dict" و ممكن تستدم على هذا الاساس
    print(f'name: {name} is {age} year-old')
    print(money)                     # "dict" نتأكيد انه يعتبرها 
    print("Have money from: ")

    for key,value in money.items():
        print(f"{key}= {value}$")

print('\n',"**money")
my_business('ali',25, "yotube", '100', business= '200')

print('return ____________________________________________')

def num(x):           # مع "return"
    return x+x+x
num(3)          # استدعينا الفنكشن لاكن ما شي امر طباعة
print(num(5))   # مثد "return" تخزن الذي امامها في "()num"
checking1= num(5)+100
print(f"checking1: \n{checking1} \n")

def number(x):   # "None" ما ممكن تستفيد منها ترجع "return" بدون 
    x+x+x
num(10)          # استدعينا الفنكشن لاكن ما شي امر طباعة
print(num(2))    # مثد "return" تخزن الذي امامها في "()num"
checking2= num(5)+100
print("checking2:",checking2)

print('------------')

def y():                 # بدون "return" يفرق اذا ما مطلوب تدخل قيم ما يتخزن شي في ()y
    x= 5+5
y()
print('y',y())

def yy():               # مع "return" يفرق اذا ما مطلوب تدخل قيم "return" تخزن في ()y
    x= 5+5
    return x
yy()
print('yy',yy())


def jakar(x):                   # "break" و "return" نتأكد الفرق بين 
    while x > 0:                # لـ"break" و "return" داخل "if"  داخل "for" داخل "while" داخل "فنكشن"
        x-= 1
        print(x)
        for i in range(5):
            print(x*i)
            if x==4:
                print(x * '*')
                break          # نلاحظ "break" تخرج من "for" فقط و ترجع تدخل فيها بعدين
            print("انتقل")     # للتأكد ان بوجود "break" لن يتنفذ الذي تحته بنفس "if" لاكن ينفذ الي بعد
            if x==2:
                print(x*'$')   # اشان نتأكد ان "return" مو معناته راح ينطبع "x"
                return x       # نلاحظ "return" تخرج من كامل "الفنكشن" مو بس "for" او "if"
        print('//////////')

print()
jakar(5)

print('lambda ____________________________________________')
def _x_(a):          # تشتغل كذا "lambda"
    return a+10

x_ = lambda a: a+10
print(x_(2))

print('____________________________________________ lambda مشروع ')

people = [(("أحمد", 60),("سارة", 50)), (("سالم", 40),("خميس", 30)), (("لميا", 20),("محمد", 10))]
print(len(people))
sorted_people = sorted(people, key= lambda person: person[1])
print(people[1])
# sorted=> [0] وبما انا ما حدنا بعدها فراح يدخل على  person[1]تدخل على 0 بعدين تشوف وين
# sorted طبعا بترتيب person[1] وظيفتها ترجع person فاسمها lambda اما 
# اما key فنستخدمها لنحدد الترتيب يعتمد على ايش
# lambda و ففكشن و اصلن هي المهمة المطلوبة وحدة فقط return نستخدمها اشان بدل ما نستخدم
print(sorted_people)

students

print('global ____________________________________________')

my_age = 25

# الفرق بين انك تستخدم علامة"#" او العلامات """
# انك تقدر تستدعي الكلام الي بين العلامات اما الشباك ما تقدر
def age():
    """
# نستخدم global لنطلع على قيمه من خارج "الفنكشن" و حتى نقدر نعدل على الي بالخارج
# طبعا اذا تريد تستخدم المتغير في فنكشن ثاني لازم نفس الشي تكتب "global"
    """
    global my_age
    my_age -= 5

age()
print(age.__doc__)  # كذا تستدعي الكلام الي بين العلامات
print(my_age)

# "print "اظغط كنترول و كلك يمين على المثد الي تريد تعرف كيف مكتوبة مثلا 
# اذا ما تظهر الخيارات بعد النقطة اضغط "كنترول و مسافة"










