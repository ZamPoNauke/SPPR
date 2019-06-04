# -*- coding: utf-8 -*-
from tkinter import *


class Block:
    def __init__(self, hypothesis, symptomps):
        self.button_yes = Button(command=self.yes, text="Yes")
        self.button_no = Button(command=self.no, text="No")
        self.button_mb = Button(command=self.mb, text="May Be")
        self.label_input = Label(bg='black', fg='white', width=60)
        self.label_output = Label(bg='black', fg='white', width=60)

        self.svid_pred_num = 0
        self.hypothesis = hypothesis
        self.symptomps = symptomps
        self.Ph_list_film = []
        self.Ph_list = []
        self.max_Ph = 0.0

        self.n = 0

        self.label_input.pack()
        self.button_yes.pack()
        self.button_no.pack()
        self.button_mb.pack()
        self.label_output.pack()

        self.get_question_and_price(' ')

    def yes(self):
        self.get_question_and_price('Yes')

    def no(self):
        self.get_question_and_price('No')

    def mb(self):
        self.get_question_and_price('Mb')  # ничего не изменит

    def unswer_hyp(self, data):
        for i in self.hypothesis:
            if i[3] == self.svid_pred_num:
                i[1] = i[data]
        for i in self.symptomps:
            if self.svid_pred_num == i[0]:
                i[3] = '1'

    def get_question_and_price(self, answer):
        def print_masiv(masiv):
            for i in masiv:
                print(i)
            print()

        if self.n < len(self.symptomps):
            for i in self.hypothesis:
                # цена (подсчет цен). Нужны для того, что бы определить какой вопрос задать первым.
                Price = abs(((i[4] * i[1]) / (i[4] * i[1] + i[5] * (1 - i[1]))) - (
                            ((1 - i[4]) * i[1]) / (1 - i[4] * i[1] - i[5] * (1 - i[1]))))
                N = i[3]
                
                PHE = (i[4] * i[1]) / (i[4] * i[1] + i[5] * (1 - i[1]))
                i[6] = PHE
                PH_E = ((1 - i[4]) * i[1]) / (1 - i[4] * i[1] - i[5] * (1 - i[1]))
                i[7] = PH_E
                
                for j in self.symptomps:
                    if j[0] == N:
                        j[2] = Price  # записываю цену в список свидетельств
            print_masiv(self.symptomps)
            print_masiv(self.hypothesis)
                
            # выбор вопроса по цене
            max_list = []
            max_ce = 0
            for i in self.symptomps:
                if i[3] == '0':
                    max_list.append(i[2])
                    max_ce = max(max_list)
                    if i[2] == max_ce:
                        svid_pred = i[4]
                        self.svid_pred_num = i[0]
                        
            if answer == 'Yes':
                self.unswer_hyp(6)
            elif answer == 'No':
                self.unswer_hyp(7)
            for i in self.symptomps:
                if self.svid_pred_num == i[0]:
                    i[3] = '1'

            self.label_input['text'] = ' '.join(svid_pred)
            
            for i in self.symptomps:
                if self.svid_pred_num == i[0]:
                    i[3] = '1'

            self.n += 1
            Ph_1, Ph_2, Ph_3, Ph_4 = 0.0, 0.0, 0.0, 0.0
            self.Ph_list = []
            for i in self.hypothesis:
                if i[2] == '1':
                    Ph_1 += i[1]
                if i[2] == '2':
                    Ph_2 += i[1]
                if i[2] == '3':
                    Ph_3 += i[1]
                if i[2] == '4':
                    Ph_4 += i[1]
            self.Ph_list.extend([Ph_1, Ph_2, Ph_3, Ph_4])

            self.Ph_list_film = []
            for i in self.hypothesis:
                if i[0] not in (self.Ph_list_film):
                    self.Ph_list_film.append(i[0])

            self.max_Ph = int(self.Ph_list.index(max(self.Ph_list)))
            print(self.Ph_list_film)
            print(self.Ph_list)
            print(self.max_Ph)
            print(self.n)
            self.label_output['text'] = str("Ответ: " + self.Ph_list_film[self.max_Ph] + " ") + str(self.Ph_list[self.max_Ph])
        else:
            self.label_input['text'] = 'Опрос окончен'
            self.label_output['text'] = str("Финальный ответ: " + self.Ph_list_film[self.max_Ph] + " ")


if __name__ == '__main__':
    def open_file(massiv, file):
        with open(file) as handle:  # открываем файл с гипотезами
            for line in handle:
                massiv.append([str(x) for x in line.split('; ')])
        for i in massiv:
            i[-1] = i[-1][:-1]
        return massiv

    hypothesis = []  # гипотезы
    symptomps = []  # свидетельства
    open_file(hypothesis, "hypothesis.txt")
    for i in hypothesis:
        i[1], i[4], i[5] = float(i[1]), float(i[4]), float(i[5])

    open_file(symptomps, "symptomps.txt")

    root = Tk()
    root.title('Нейлоровская система')
    first_block = Block(hypothesis, symptomps)

    root.mainloop()
