# โปรแกรมคำนวนการแลกคูปอง

product01 = float(input("ราคาสินค้า >>> "))
money01 = float(input("จำนวนเงินที่ใช้แลกคูปอง >>>"))

kupong02 = 10 / 100 * product01

if money01 >= 500 :
    print("คูปองที่คุณสามารถแลกได้ คือ >>> ", kupong02, "คูปอง")
elif money01 >= 100 :
    print("คูปองที่คุณสามารถแลกได้ คือ >>> ", kupong02, "คูปอง")
elif money01 >= 50 :
    print("คูปองที่คุณสามารถแลกได้ คือ >>> ", kupong02, "คูปอง")
else :
    print("ไม่สามารถแลกคูปองได้")