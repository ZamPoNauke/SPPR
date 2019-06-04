# -*- coding: utf-8 -*-
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


def main():
    hypothesis = []  # гипотезы
    certificate = []  # свидетельства
    open_file(hypothesis, "hypothesis.txt")
    for i in hypothesis:
        i[1], i[4], i[5] = float(i[1]), float(i[4]), float(i[5])

    open_file(certificate, "syptomps.txt")
    print_masiv(hypothesis)
    print_masiv(certificate)

    n = 0
    while n < len(certificate):
        for i in hypothesis:
            PHE = (i[4]*i[1])/(i[4]*i[1]+i[5]*(1-i[1]))
            i[6] = PHE
            PH_E = ((1-i[4])*i[1])/(1-i[4]*i[1]-i[5]*(1-i[1]))
            i[7] = PH_E
            # цена (подсчет цен). Нужны для того, что бы определить какой вопрос задать первым.
            Price = abs(PHE - i[1]) + abs(PH_E - i[1])
            N = i[3]
            for j in certificate:
                if j[0] == N:
                    j[2] = Price  # записываю цену в список свидетельств
        print_masiv(certificate)

        #  выбор вопроса по цене
        max_list = []
        max_ce = 0
        for i in certificate:
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
        for i in certificate:
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

    print("Ответ:", Ph_list_film[max_Ph])

if __name__ == '__main__':
    main()
