import random
from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# در این برنامه، یکی از سه کلمه "سنگ"، "کاغذ" یا "قیچی" در عنوان
# پنجره برنامه بصورت تصادفی نمایش داده میشود - آیا میتوانید
# آن را به شکلی تغییر دهید که نام سه اتومبیل را بصورت تصادفی
# نمایش دهد؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.title(random.choice(["سنگ", "کاغذ", "قیچی"]))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()