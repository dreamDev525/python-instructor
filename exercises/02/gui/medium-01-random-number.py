import random
from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# برنامه زیر یک عدد تصادفی بین 1 تا 6 را بر روی یک دکمه نمایش
# میدهد
# آیا میتوانید برنامه را به شکلی تغییر دهید که عددی که در
# خروجی نمایش داده میشود در واحد 10 ضرب شود؟
# برنامه را به شکلی تغییر دهید که یک عدد زوج بین 2 تا 20 بصورت
# تصادفی نمایش داده شود

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.geometry("250x60")
window.title("یک عدد تصادفی")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers = [1, 2, 3, 4, 5, 6]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def choose_a_random_number():
    number = random.choice(numbers)
    button.config(text=str(number))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
button = Button()
button.config(text="کلیک کنید")
button.config(command=choose_a_random_number)
button.place(x=10, y=15, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
