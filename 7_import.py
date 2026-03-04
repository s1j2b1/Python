from Python.ss import students

print('import from python ____________________________________________')

students()

# عبارة عن تمبلت يحتوي على اتربيوت و مثد يعني متغيرات و دوال
# اشان تطلع او تستخدم شي من "class" لازم تنشأ متغير يسمى اوبجكت تستدعي الشي الي تريده من خلاله
class my_class:
    my_name= "Ali"
    def students(silf):      # اي فنكشن داخل "class" لازم تحطلها "silf"
        print(silf.my_name)  # ما تحتاج جلوبل بـ "silf" تقدر توصل اذا كنت داخل الـ "class"
        print(5+6)

o= my_class()          # "اوبجكت" للـ"class" و تقدر تعمل اكثر من واحد لنفس الـ"class"
o.students()           # كذا تستدعي "فنكشن" من "class" لازم "()"
print('\n',o.my_name,'\n')  # نطبع قيمة متغير من الـ"class"

o.my_name= "Mohamed"   # كذا نقدر نغير قيمة داخل "class"
o.students()

print('____________________________________________ مشروع')


# مشروع class
# كلاس باسم الطلاب يحتوي على الاسم رقم هوية و تخصص طريقة لطباعة بطاقة اهوية ثم
# دالة فرعية لطلاب تكنولوجيا المعلومات
# طريقة انشاء حساب جيميل الاسم الاسم الاخير سنة الميلاد @جيميل.كوم
# دالة فرعية لطلاب القانون الكل مع طريقة لاختيار الشركة بشكل عشوائي من بين 5 شركات

class studunts:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.print_id = print(f'{self.name} ID: {self.id}')
        # print("ali")


class x(studunts):
    def stud(self):
        print(self.major)
        self.print_id
        pass


obj1 = studunts("omar", 12, 'doctor')
obj1.print_id

obj2 = x("salim", 12, 'doctor')
obj2.stud()


print('__init__ ____________________________________________')

class name:
    j=9
    def __init__(self,num,nam):
        self.__nam = nam
        self.__num = num

    def new_print(self):
        print(self.__nam,self.__num)

    @staticmethod
    def r(data):
        return data.replace("-","/")

    def newR(self,data):
        return data.replace("-",'/')

    def d(self,pp):
        print(999)
        return pp.replace("j", "55")



o= name(60,"sami")

print(o.j)
# o.new_print()
# o.__nam="omar"
# o.__num=8
# o.new_print()
# o= name(99,"omar")
# o.new_print()

# print(o.r("7-8-09-66"))
# print(o.newR("7-8-09-66"))
# print(o.d("hfhj"))


# print(bin(ord(print(3+5))))




print('import from out ____________________________________________')


print('import library ____________________________________________')












