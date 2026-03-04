
print('input ____________________________________________')

input()
input("enter:")
inx= input("enter: ")
iny= float(input("enter number: "))


# ---------------------- مشروع تحويل الوزن kg => g --------------------------
print(' ____________________________________________ مشروع تحويل الوزن ')



# ----------------------------------------------------------------------------

print('\n index ____________________________________________\n')

nam = "Sulaiman"
#      01234567
# بحث عن موقع اندكس للحرف
# "⋈" اذا الحرف مو موجود "1-" لان يبدي العد من "0" الى 
print(f"find('l'): \n{nam.find("l")} \n")
# تغيير رمز
print(f"replace: \n{nam.replace('l',"55")} \n")

sentence = "البرمجة ممتعة ومفيدة ومسلية"
# maxsplit (اختياري): أقصى عدد مرات تقسيم.
# يقسم عند المسافات  "separator" بدون تحديد الشيء الذي تريد أن تقسم النص عنده
# يحذف مكان التقسيم ثم يقسم
parts = sentence.split(sep='م',maxsplit= 2)
print(parts)


# عدد العناصر
print(f"len(nam): {len(nam)} \n")
# طباعة الموجود بالموقع المحدد و يبدأ العد من 0
print(f"nam[5]: {nam[5]} \n")

print('try ____________________________________________')

# يطبع رساله اذا حدث خطأ
# except ValueError مثل except ممكن ان تعمل خطا لتظهر لك نوع الخطا و تنسخه و تضيفه بعد
# ممكن ما تحدد نوع الخطا بس اي خطا يصير يطبع فما تظيف نوع الخطا
# طبعا ممكن تستخدم اكثر من except مع نوع الخطا لاكن بدون نوع بس واحد
try:
    number= int(input("enter number: "))
except ValueError: print("no no no")


# ---------------------- Try مشروع --------------------------
print(' ____________________________________________ Try مشروع ')

# Try مشروع 
try:
    x= int(input("enter num: "))
    print(x+5)
    y = int(input("enter num: "))
    print (5/y)

except TypeError:
    print("noo")
except ZeroDivisionError:
    print("Can't divide with 0")
except ValueError as err:
    print(err)


# ---------------------- مشروع القصة --------------------------
print(' ____________________________________________ مشروع القصة')

# مشروع القصة
# Short Story with Hidden Name
# Little Mia walked to the park.
# ميا الصغيرة مشيت إلى الحديقة
# Under the big oak tree, she found a shiny coin.
# تحت شجرة البلوط الكبيرة، وجدت عملة لامعة
# Curious, she picked it up and looked around.
# بدافع الفضول، التقطتها ونظرت حولها
# A bird chirped loudly as if it was talking to her.
# زقزق طائر بصوت عالٍ وكأنه يتحدث معها
# Smiling, Mia put the coin in her pocket and continued walking.
# مبتسمة، وضعت ميا العملة في جيبها وواصلت المشي
# 🔍 الحروف الأولى من كل جملة تشكل اسم "LUCAS".

a= ['Little Mia walked to the park',
'Under big tree, she found a shiny coin',
'Curious, she picked it up and looked around',
'A bird sits on the tree and looks at her',
'Smiling, Mia put the coin in her pocket and went home']
for i in a:
    print(i)

print("-------------------------")
x= 0
print(a[0][x]+a[1][x]+a[2][x]+a[3][x]+a[4][x])
print(a[0][4]+a[1][3]+a[2][2]+a[3][1]+a[4][0])
print("-------------------------")



# ---------------------- input مشروع --------------------------
print(' ____________________________________________ input مشاريع')

'''التحدي: مطلوب منك كتابة برنامج بسيط يعرض تحية مخصصة لشخصين ويطلب منهما الإجابة على سؤال.
يجب أن يطلب البرنامج من المستخدمين إدخال أسمائهم.
بعد إدخال الأسماء، يجب أن يطبع البرنامج رسالة تقول: "مرحبًا {x} و {y}، كيف حالكما؟".
بعد ذلك، يطلب من كل من "x" و "y" الإجابة على سؤال: "هل أنتم بخير؟".
في النهاية، يجب أن يطبع البرنامج ردود الأشخاص مع الأسماء.
المخرجات المتوقعة:
أدخل اسمك الأول: sara
أدخل اسمك الثاني: mona
مرحبًا sara و mona، كيف حالكما؟
هل أنتم بخير، sara؟ (نعم/لا): نعم
هل أنتم بخير، mona؟ (نعم/لا): لا
ردود sara و mona: نعم، ل'''''
x = input("enter your name: ")
y = input("enter your name: ")
print(f"hello {x} and {y} ")
a = input(f"how are you {x}")
b = input(f"how are you {y}")
print(f"{x} say {a} \n{y} say {b}")


# ---------------------- input with math مشروع --------------------------
print(' ____________________________________________ input with if shorter مشاريع')

weight = int(input("enter your weight in Kg: "))
print(f"your weight in g is: {weight*1000}g")


# ---------------------- input with if shorter مشروع --------------------------
print(' ____________________________________________ input with if shorter مشاريع')

# برنامج امكانية تصويت شخص في الانتخابات اذا اردني و اكبر من 18
country = input("are your country jordan yse or no: ")
age = int(input("enter your age: "))
if country.lower()=="yse" and age>18:
    cand = input("Mention your candidate's name: ")
    print(f"your candidate is {cand}")
else:
    print("sorry, you cannot nominate..")


