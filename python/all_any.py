"""
فانکشن های any و all در پایتون. هر دوی این فانکشن ها یک آبجکت iterable گرفته و نسبت به آیتم های داخل آنها True یا False برمیگردانند
"""
x = [1, 0, False]
print(any(x))

y = [0, False, 0]
print(any(y))

"""
فانکشن all فقط در صورتی که تمام مقادیر آبجکت iterable برابر True باشد نتیجه True برمیگرداند در غیر اینصورت اگر حتی فقط یکی از آیتم ها برابر False باشد نتیجه False برمیگرداند:
"""
x = [1, 0, True]
print(all(x))

y = [True, 1, 1]
print(all(y))
