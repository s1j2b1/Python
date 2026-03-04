'''
print('list \ tuple \ set \ dict ____________________________________________')

# list ordered=> مرتب \ changeable=> تقبل تغيير \ duplicate => تقبل تكرار
a= ['s',5,True]
b= list(('s',5,True))
print(f"type(a): \n{type(a)} \n")
print(f"b: \n{b} \n")

# tuple ordered=> مرتب \ changeable=> لا تقبل تغيير \ duplicate => تقبل تكرار
c= ('s',5,True)
d= tuple(('s',5,True))
print(f"type(c): \n{type(c)} \n")
print(f"d: \n{d} \n")

# set unordered=> غير مرتب \ unchangeable=> لا تقبل تغيير \ No duplicate => لا تقبل تكرار
e= {'s',5,True}
f= set(('s',5,True))
print(f"type(e): \n{type(e)} \n")
print(f"f: \n{f} \n")

# dict unordered=> غير مرتب \ chingble=> تقبل تغيير \ No duplicate => لا تقبل تكرار
# تحتوي key:value
# فقط key كل الشروط تطبق على
# بس تأكد هل الفاليو مرتب يعني تقدر تستدعي بالاندكس مع الكي موقع معين
g= {'s':2,
    5:"man",
    'woman':True }

h= dict({'s': 2,
         5: "man",
         'woman': True})
print(f"type(g): \n{type(g)} \n")
print(f"h: \n{h} \n")

print('list ____________________________________________')

my_list= []                          # فاضية "list"  ممكن نعمل 
print(f"type(my_list): \n{type(my_list)} \n")
print(f"my_list: \n{my_list} \n")

my_list= [2,[55,"A"],'e',True,2.2]  # 2D list
print(f"my_list[1:10]: \n{my_list[1:10]} \n")
print(f"my_list[-2]: \n{my_list[-2]} \n")
print(f"my_list[1:]: \n{my_list[1:]} \n")
print(f"my_list[:10]: \n{my_list[:10]} \n")
print(f"my_list[:]: \n{my_list[:]} \n")
print(f"my_list[1][1]: \n{my_list[1][1]} \n")
print(f"type(my_list[1][1]): \n{type(my_list[1][1])} \n")
print(f"len(my_list): \n{len(my_list)} \n")

my_list[1]= 4
my_list[-2:]= 'a','b','c'
print(f"my_list[-2:]: \n{my_list} \n")

my_list.append(10)       # تضيف اخر شي
my_list.insert(2,'Ali')  # تضيف و تزحف الي بعده
print(f"insert: \n{my_list} \n")

my_list.remove('a')
print(f"remove: \n{my_list} \n")

my_list.pop()        # remove last value
my_list.pop(1)       # remove index
my_x= my_list.pop()  # remove last value and save it in "my_x"
print(f"pop: {my_list} ")
print(f"my_x: \n{my_x} \n")

del my_list[0]
# del my_list
print(f"del[0]: \n{my_list} \n")

my_list.clear()
print(f"clear(): \n{my_list} \n")

my_list= [2,[55,"A"],'e',True,2.2]
y_list= [5,6,7,'f']
my_list.extend(y_list)              # "my_list" بآخر "y_list" كذا تنضاف
# "w_list" اما كذا ما تنضاف ولا تنحفظ في 
# طبعا ما تتغير my_list نفس الشي راح تتغير لاكن "y_list" بس نلاحظ هنا
w_list= y_list.extend(my_list)

print(f"mmm_list: \n{my_list} \n")
print(f"yyy_list: \n{my_list} \n")
print(f"w_list: \n{w_list} \n")
print(f"my_list: \n{my_list} \n")
w_list= my_list + y_list           # كذا طريقة ثانية ممكن تضيف
print(f"w_list: \n{w_list} \n")

print(f"count(55): \n{w_list.count(55)} \n")       # يطلع كم مرة متكرر
y_list= ['5','6','7','2','1']
y_list.sort(reverse=True)          # يرتب من الاكبر اذا فاضي من الاصغر "reverse=True" مع
print(f"y_list: \n{y_list} \n")
print(f"sort: \n{y_list.sort(reverse=True)} \n")   # "None" ما يعطي خطا بس "print" ما ينفع نخليها داخل 
print(f"index: \n{y_list.index("5")} \n")          # وين موقع "5"

print(f"dir(list): \n{dir(list)} \n")                        # المثد الي ممكن نستخدمهن

print('____________________________________________ مشروع')

# مشروع list
# قائمة من الارقام من 1الى 10 اطبع العنصر الثالث اضف الرقم 11 قم بالفرز تنازليا**list**
# num=[]
# for i in range(1,11):
#     num.append(i)
# print(num)
# print(num[2])
# num.append(11)
# num.sort(reverse=True)
# print(num)


print('Tuple ____________________________________________')

my_tupl= ()                  # ممكن نعمل "Tuple" فاضية
print(f"type(): \n{type(my_tupl)} \n")
print(f"my_tupl: \n{my_tupl} \n")

my_tupl= (2,)                # بقيمة وحدة لازم مع فاصلة "Tuple" كذا نعمل 
print(f"my_tupl: \n{my_tupl} \n")
my_tupl= ((1,'Ali'),'h',5,False,3.2)
print(f"my_tupl: \n{my_tupl} \n")

my_tupl+= (5,)               # في "Tuple" ممكن نضيف قيم و نحذف بس ما ممكن نعدل
print(f"my_tupl+=: \n{my_tupl} \n")

# اشان نعدل قيمة في "Tuple" نحولها ل "list" ونعدل بعدين نرجعنا
my_tupl= list(my_tupl)
print(f"my_tupl:list \n{my_tupl} \n")
my_tupl.remove(False)
print(f"my_tupl:remove \n{my_tupl} \n")
my_tupl= tuple(my_tupl)
print(f"my_tupl:tuple \n{my_tupl} \n")

print(f"index: \n{my_tupl.index('h')} \n")
print(f"count: \n{my_tupl.count(5)} \n")

print(f"my_tupl[1:10]: \n{my_tupl[1:10]} \n")
print(f"my_tupl[-2]: \n{my_tupl[-2]} \n")
print(f"my_tupl[1:]: \n{my_tupl[1:]} \n")
print(f"my_tupl[:10]: \n{my_tupl[:10]} \n")
print(f"my_tupl[:]: \n{my_tupl[:]} \n")
print(f"my_tupl[0][1]: \n{my_tupl[0][1]} \n")
print(f"type[0][1]: \n{type(my_tupl[0][1])} \n")
print(f"len: \n{len(my_tupl)} \n")

# del my_tupl
print(f"my_tupl: \n{my_tupl} \n")

print(f"dir(): \n{dir(tuple)} \n")                        # المثد الي ممكن نستخدمهن

print('____________________________________________ مشروع')

# مشروع tuple
# # # مجموعة باسما اربع مدن اطبع امدينة الثانية**tuple**
# ctyName = ('nizwa' , 'sohar' , 'soor' , 'salala')
# print(ctyName[1])


print('set ____________________________________________')

my_set= set()
print(f"my_set: \n{my_set} \n")
my_set.add(5)
print(f"type: \n{type(my_set)} \n")
print(f"add(5): \n{my_set} \n")

# ما نقدر نعمل 2D set
# ما ممكن نحط داخل "set" [] {} فقط ()
# في كل مرة يتغير ترتيب مواقع القيم
my_set= {(1, 'Ali'),'h',5,False,3.2}
print(f"my_set: \n{my_set} \n")

my_set.add(55)           # يضيف لاكن في موقع عشوائي لان "set"
print(f"add(55): \n{my_set} \n")

# my_set.remove('s')       # يعطي "Error" اذا العنصر ما موجود
my_set.discard('s')      # "Error"يحذف العنصر و اذا ما موجود ما يعطي
print(f"discard: \n{my_set} \n")

my_set.pop()             # يحذف اخر عنصر لاكن طبعا "set" مو مرتبة
print(f"pop: \n{my_set} \n")

set_x=[1,1,5,3,7]
set_y= set(set_x)        # راح تنحذف العنار المكررة لان "set" لا تقبل التكرار
print(f"set_x: \n{set_x} \n")
print(f"set_y: \n{set_y} \n")

# set_y.update()
print(f"update: \n{set_y} \n")


A = {'mohamad', 'saliam', 'omar', 'kahlid', 'sami'}
B = {'bnana','carot','saliam','carot','omar','apple'}
print(A==Bf"update: \n{set_y} \n")
# يحذف المتشابه و يضيف الي مو موجود ولازم تحفظ في متغير لان هي ما تغير A او B
print(f"symmetric_difference(B): \n{A.symmetric_difference(B)} \n")
# يحذف المتشابه و يضيف الي مو موجود و تغير A او B
print(f"symmetric_difference_update(B): \n{A.symmetric_difference_update(B)} \n")
print(f"union(B): \n{A.union(B)} \n")                       #  يضيف الي مو موجود فقط و لازم تحفض في متغير
print(f"difference(B): \n{A.difference(B)} \n")                  # تحذف المتشابه و لازم تحفض في متغير
print(f"difference_update(B): \n{A.difference_update(B)} \n")           # تحذف المتشابه و تغير A او B
print(f"intersection(B): \n{A.intersection(B)} \n")                # تحذف غير المتشابه و لازم تحفض في متغير
print(f"intersection_update(B): \n{A.intersection_update(B)} \n")         # تحذف غير المتشابه و تغير A او B
print(f"isdisjoint(B): \n{A.isdisjoint(B)} \n")                  # اذا ماشي تشابه في العناصر True
print(f"issuperset(B): \n{A.issuperset(B)} \n")                  # اذا عناصر المجموعة الثانية كلها موجودة بالاولى True
print(f"issubset(B): \n{A.issubset(B)} \n")                    # اذا كل عناصر الاولى موجودة في الثانية True

print(f"dir(): \n{dir(set)} \n")                        # المثد الي ممكن نستخدمهن

print('____________________________________________ مشروع')

# مشروع set
# # الاتحاد و التقاطع بين مجموعتين **set**
# grop1 = {1,5,'A','S','F'}
# grop2 = {'S','U','L','I','M','A','N',1}
# join = grop1.intersection(grop2)
# unjoin = grop1.symmetric_difference(grop2)
# print(join)
# print(unjoin)

'''

print('dict ____________________________________________')

my_dict= {}
print(f"type(): \n{type(my_dict)} \n")
print(f"my_dict: \n{my_dict} \n")

# لا تقبل تكرار "key" لاكن عادي تكرار "value"
my_dict= {
    's':2,
    5:"man",
    's':5,
    'woman':True }

my_dict= dict({
         's': 2,
         5: "man",
         's':5,
         'woman': True})

print(f"my_dict: \n{my_dict} \n")
my_dict['s']= 12           # لتغيير "value" اما "key" ما ممكن يتغير
print(f"my_dict: \n{my_dict} \n")

print(f"my_dict[5]: \n{my_dict[5]} \n")          # لطباعة "value" معين لازم ننادي "key"

# print(my_dict['name'])     # يعطي "Error" اذا ما موجود
# ما يعطي "Error" اذا مو موجود و ممكن يطبع رسالة اذا مو موجود
print(my_dict.get('name','هذا المفتاح غير متوفر'))

for x,y in my_dict.items():
    print(x,y)
print()
for x in my_dict.values():
    print(x)
print()
for y in my_dict.keys():
    print(y)

print(f"len: \n{len(my_dict)} \n")
print(f"type: \n{type(my_dict)} \n")
print(f"items: \n{my_dict.items()} \n")
print(f"keys: \n{my_dict.keys()} \n")
print(f"values(): \n{my_dict.values()} \n")

my_dict.update({'key':11})       # يضيف في الاخير
print(f"update({'key':11}): \n{my_dict} \n")

my_dict.pop('key')      # يحذف و لازم تعطيه اسم
print(f"pop('key'): \n{my_dict} \n")

my_dict.popitem()      # يحذف اخر ايتم
print(f"popitem(): \n{my_dict} \n")

del my_dict['s']       # يحذف و لازم تعطيه اسم
print(f"del['s']: \n{my_dict} \n")

x_my_dict= my_dict.copy()
print(f"x_my_dict: \n{x_my_dict} \n")
my_dict.clear()
print(f"clear(): \n{my_dict} \n")
print(f"x_my_dict: \n{x_my_dict} \n")

print('____________________________________________ مشروع')

# مشروع dict
# # # قاموس لاسماء3 الاصدقاء و اعمارهم ضف صديق جديد و اطبعه**dic**
# frind = {    'name1' : 'mohamad',
#              'name2' : 'sultan',
#              'name3' : "rama"       }
# friendName= input('friend name: ')
# frind.update({f'nam{len(frind)+1}': friendName})
# print(frind)
# print("")


print(' ____________________________________________ مشاريع')


# مشروع list
# قائمة من الارقام من 1الى 10 اطبع العنصر الثالث اضف الرقم 11 قم بالفرز تنازليا**list**
# num=[]
# for i in range(1,11):
#     num.append(i)
# print(num)
# print(num[2])
# num.append(11)
# num.sort(reverse=True)
# print(num)



# مشروع list , for
# ازالة العناصر المكررة**list**
# my_name = [input("enter: ")]
# for i in my_name:
#     newName = [*i]
# for r in newName:
#     R= newName.count(r)
#     if R>1:
#         for t in range(1,R):
#             newName.remove(r)
# print(newName)


# مشروع tuple , for
# # حساب متوسط مجموع العناصر**tuple**
# avareg = (10,43,28,30,20,66)
# sum_num= 0
# for i in avareg:
#     sum_num += i
# print(avareg)
# print(f"{sum_num}/{len(avareg)}= {sum_num/len(avareg)}")



# مشروع list , for longer
# **list** برنامج يدور االقائمة لليمين [45123][12345]
# x = [1,2,3,4,5,6]
# y = len(x)
# a = x[y-1]
# for i in range(0,2):
#     x.append(a)
#     y = len(x)
#     x[y-1]=x[y-2]
#     x[y-2]=x[y-3]
#     x[y-3]=x[y-4]
#     x[y-4]=x[y-5]
#     x[y-5]=x[y-6]
#     x[y-6]=x[0]
#     x[0]=x[y-1]
#     x.pop()
# print(x)





# مشروع list , for longer
# برنامج حساب تكرار كل كلمة في جملة معينة خزن النتيجة في قاموس **str**
# x = 'hello world hello python'
# l = []
# m = {}
# for i in x:
#     l.append(i)
#     print(l)
#     if i==' ':
#         print(*l)
#         s=
#         # print(s)
#         # m.update({s,1})
#         l=[]
# print(l)
# print(*l)
# print(s)













