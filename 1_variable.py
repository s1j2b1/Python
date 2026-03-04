
# يطبع الرموز "str" بصيغة 011001
print(bin(ord('5')))
# يطبع الارقام بصيغة 011001
print(bin(5))

print()
print("s\tulaima\nn",'\n')

print("Sulaiman".lower())
print("Sulaiman".upper())
print("Sulaiman".lower().islower())
print("Sulaiman".istitle()) # upper هل اول حرف 
# \ .isnumeric() المحتوى رياضيات \ .isprintable() كل المحتوى حرف رقم رمز \ 
# .isspace() لا تحتوي حرف رقم رمز \ .isdecimal() E فقط ارقام صحيحة\ 
# .isdigit() فقط ارقام صحيحة اي لغة\.isidentifier() المحتوى ينفع كمتغير
# .istitle() تبدأ بحرف كبير \ .isalnum() حروف ارقام فقط \ 
# .isalpha() حروف فقط \ .isascii() E فقط حرف رمز
print('\n')

print(2*"*"*2,'\n')

print("      /\\ /\  " *2)
print("    ( \" \' ) "*2)
print("    /| 💖|\\ " *2)
print("   / |   | \\" *2)
print("      | |   "  *2)

print("A"+'B')
print("C","D",'\n')
# print("comment")

'''
comment ...
How python steps
working all and stop at first error
'''

print('variable ____________________________________________')

# variable
# نختار اسماء معبرة لان من نكتب برنامج 1000 سطر راح نضيع بالاسماء
# "print" مثل "python" انتبه ان الاسم ليس مستخدم من لغة   
# لا يصح استخدام $ % @ & الخ.. في اي مكان
# انتبه من المساف بأول اسطر
# لا تضع رقم اول الاسم

_ = 5
_x= bool(1)
myNam = "sulaiman"
MyAge = 25
Iam_coder = 'Ai'
I_am_coder2 = "python"
one,tow,three = 1,2,float(3)

print('change ____________________________________________')

print(type(_),_,str(_),type(_)) # not change "_" to "str"
# _ = str(_)                      # now change "_" to "str"
print(_,type(_),'\n')

sum_test1 = 5
sum_test2 = 4
sum_test1+sum_test2           # not change
print("sum_test1",sum_test1)
sum_test1 += sum_test2        # now change
print("sum_test1:",sum_test1)
print("sum_test2:",sum_test2)
print(f"{sum_test1}/{sum_test2}") # another way print


