from tkinter import *


def main():
    def click_button_yes():
        root.title("Clicks {}".format('Yes'))

    def click_button_no():
        root.title("Clicks {}".format('No'))

    def click_button_dn():
        root.title("Clicks {}".format('Dn'))
        set_poetry(hypothesis)

    def set_poetry(text):
        #label2.text = text[0][0]
        label2 = Label(text=text[0][0], justify=LEFT)
        label2.place(relx=.2, rely=.5)
        root.mainloop()
        data_update()

    def data_update():
        def open_file(massiv, file):
            with open(file, encoding='windows-1251') as handle:  # открываем файл с гипотезами
                for line in handle:
                    massiv.append([str(x) for x in line.split('; ')])
            for i in massiv:
                i[-1] = i[-1][:-1]
            return massiv


        def print_masiv(masiv):
            for i in masiv:
                print(i)
            print()

        open_file(hypothesis, "hypothesis.txt")
        for i in hypothesis:
            i[1], i[4], i[5] = float(i[1]), float(i[4]), float(i[5])

        open_file(symptomps, "syptomps.txt")
        print_masiv(hypothesis)
        print_masiv(symptomps)
        n = 0
        while n < len(symptomps):
            for i in hypothesis:
                PHE = (i[4]*i[1])/(i[4]*i[1]+i[5]*(1-i[1]))
                i[6] = PHE
                PH_E = ((1-i[4])*i[1])/(1-i[4]*i[1]-i[5]*(1-i[1]))
                i[7] = PH_E
                # цена (подсчет цен). Нужны для того, что бы определить какой вопрос задать первым.
                Price = abs(PHE - i[1]) + abs(PH_E - i[1])
                N = i[3]
                for j in symptomps:
                    if j[0] == N:
                        j[2] = Price  # записываю цену в список свидетельств
            print_masiv(symptomps)

            #  выбор вопроса по цене
            max_list = []
            max_ce = 0
            for i in symptomps:
                if i[3] == '0':
                    max_list.append(i[2])
                    max_ce = max(max_list)
                    if i[2] == max_ce:
                        svid_pred = i[4]
                        svid_pred_num = i[0]

            print(svid_pred)
            yn = (input("Да, Нет или Не знаю: ")).lower()

            def unswer_hyp(svid_pred_num, hypothesis, data):
                for i in hypothesis:
                    if i[3] == svid_pred_num:
                        i[1] = i[data]

            if yn == 'да':
                unswer_hyp(svid_pred_num, hypothesis, 6)
            elif yn == 'нет':
                unswer_hyp(svid_pred_num, hypothesis, 7)
            for i in symptomps:
                if svid_pred_num == i[0]:
                    i[3] = '1'

            n += 1
            Ph_1, Ph_2, Ph_3, Ph_4 = 0.0, 0.0, 0.0, 0.0
            Ph_list = []
            for i in hypothesis:
                if i[2] == '1':
                    Ph_1 += i[1]
                if i[2] == '2':
                    Ph_2 += i[1]
                if i[2] == '3':
                    Ph_3 += i[1]
                if i[2] == '4':
                    Ph_4 += i[1]
            Ph_list.extend([Ph_1, Ph_2, Ph_3, Ph_4])
            Ph_list_film = []
            for i in hypothesis:
                if i[0] not in(Ph_list_film):
                    Ph_list_film.append(i[0])

            for i in hypothesis:
                max_Ph = int(Ph_list.index(max(Ph_list)))

        label4 ("Ответ:", Ph_list_film[max_Ph])

    root = Tk()
    # Основной экран
    root.title("Графическая программа на Python")
    root.geometry("400x500+300+250")

    btn_Yes = Button(text="Yes",          # текст кнопки
                     background="#555",     # фоновый цвет кнопки
                     foreground="#ccc",     # цвет текста
                     padx="20",             # отступ от границ до содержимого по горизонтали
                     pady="8",              # отступ от границ до содержимого по вертикали
                     font="16",              # высота шрифта
                     command=click_button_yes
                     )
    btn_No = Button(text="No",          # текст кнопки
                    background="#555",     # фоновый цвет кнопки
                    foreground="#ccc",     # цвет текста
                    padx="20",             # отступ от границ до содержимого по горизонтали
                    pady="8",              # отступ от границ до содержимого по вертикали
                    font="16",              # высота шрифта
                    command=click_button_no
                    )
    btn_DN = Button(text="Dont know",          # текст кнопки
                    background="#555",     # фоновый цвет кнопки
                    foreground="#ccc",     # цвет текста
                    padx="20",             # отступ от границ до содержимого по горизонтали
                    pady="8",              # отступ от границ до содержимого по вертикали
                    font="16",              # высота шрифта
                    command=click_button_dn
                    )

    question = "Вопрос: "
    label1 = Label(text=question, justify=LEFT)

    poetry = 'Текст вопроса. Несколько подлиннее'
    label2 = Label(text=poetry, justify=LEFT)

    question = "Промежуточный вывод: "
    label3 = Label(text=question, justify=LEFT)

    question = "Итоговый ответ: <тест еще не завешен>"
    label4 = Label(text=question, justify=LEFT)

    hypothesis = []  # гипотезы
    symptomps = []  # свидетельства


    btn_Yes.pack()
    btn_No.pack()
    btn_DN.pack()
    label1.place(relx=.4, rely=.4)
    label2.place(relx=.2, rely=.5)
    label3.place(relx=.3, rely=.7)
    label4.place(relx=.0, rely=.95)
    root.mainloop()

if __name__ == '__main__':
    main()
