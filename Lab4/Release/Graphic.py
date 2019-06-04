from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))

root = Tk()
# Основной экран
root.title("Графическая программа на Python")
root.geometry("400x500+300+250")

# Кнопка
btn_Yes = Button(text="Yes",          # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             command=click_button
             )
btn_No = Button(text="No",          # текст кнопки
                 background="#555",     # фоновый цвет кнопки
                 foreground="#ccc",     # цвет текста
                 padx="20",             # отступ от границ до содержимого по горизонтали
                 pady="8",              # отступ от границ до содержимого по вертикали
                 font="16",              # высота шрифта
                 command=click_button
                 )
btn_DN = Button(text="Dont know",          # текст кнопки
                 background="#555",     # фоновый цвет кнопки
                 foreground="#ccc",     # цвет текста
                 padx="20",             # отступ от границ до содержимого по горизонтали
                 pady="8",              # отступ от границ до содержимого по вертикали
                 font="16",              # высота шрифта
                 command=click_button
                 )

question = "Вопрос: "
label1 = Label(text=question, justify=LEFT)
label1.place(relx=.4, rely=.4)

poetry = 'Текст вопроса. Несколько подлиннее'
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.5)

question = "Промежуточный вывод: "
label3 = Label(text=question, justify=LEFT)
label3.place(relx=.3, rely=.7)

question = "Итоговый ответ: <тест еще не завешен>"
label4 = Label(text=question, justify=LEFT)
label4.place(relx=.0, rely=.95)

btn_Yes.pack()
btn_No.pack()
btn_DN.pack()

root.mainloop()
