# -*- coding: utf-8 -*-
def open_file(massiv, file):
    with open(file) as handle:  # открываем файл с гипотезами
        for line in handle:
            massiv.append([str(x) for x in line.split()])
    return massiv

def main():
    hypothesis = []
    svid = []
    open_file(hypothesis, "hypothesis.txt")
    for i in hypothesis:
        i[1] = float(i[1])
        i[4] = float(i[1])
        i[5] = float(i[5])
    open_file(svid, "certificate.txt")
    print(hypothesis, '\n', svid)

    n = 0
    while n < len(svid):
        Price = 0  # цена (подсчет цен). Нужны для того, что бы определить какой вопрос задать первым.
        N = 0

        for i in hypothesis: # Высч
            Price = abs(((i[4]*i[1]) / (i[4]*i[1]+i[5]*(1-i[1]))) - (((1-i[4])*i[1]) / (1-i[4]*i[1]-i[5]*(1-i[1]))))
            N = i[3]
            for j in svid:
                if j[0] == N:
                    j[2] = Price  # записываю цену в список свидетельств
        #print(svid)

        for i in hypothesis:
            PHE = (i[4]*i[1])/(i[4]*i[1]+i[5]*(1-i[1]))
            i[6] = PHE
            PH_E = ((1-i[4])*i[1])/(1-i[4]*i[1]-i[5]*(1-i[1]))
            i[7] = PH_E

    #  выбор вопроса по цене
        max_list = []
        for i in svid:
            if i[3] == '0':
                max_list.append(i[2])
                max_ce = max(max_list)
                if i[2] == max_ce:
                    svid_pred = i[4]
                    svid_pred_num = i[0]

        print(svid_pred)
        yn = input("Да/Нет/Не знаю: ")
        yn = yn.lower()

        if yn == 'да':
            for i in hypothesis:
                if i[3] == svid_pred_num:
                    i[1] = i[6]
            for i in svid:
                if svid_pred_num == i[0]:
                    i[3] = '1'
        elif yn == 'нет':
            for i in hypothesis:
                if i[3] == svid_pred_num:
                    i[1] = i[7]
            for i in svid:
                if svid_pred_num == i[0]:
                    i[3] = '1'
        else:
            for i in svid:
                if svid_pred_num == i[0]:
                    i[3] = '1'

        n += 1
        Ph_1 = 0.0
        Ph_2 = 0.0
        Ph_3 = 0.0
        Ph_4 = 0.0
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
        Ph_list.append(Ph_1)
        Ph_list.append(Ph_2)
        Ph_list.append(Ph_3)
        Ph_list.append(Ph_4)
        Ph_list_film = ['Припять', 'Мальчишник', 'Виноваты_звезды', 'Горько']
        for i in hypothesis:
            max_Ph = Ph_list.index(max(Ph_list))
            max_Ph = str(max_Ph)

    if max_Ph == '0':
        print(Ph_list_film[0])
    elif max_Ph == '1':
        print(Ph_list_film[1])
    elif max_Ph == '2':
        print(Ph_list_film[2])
    else:
        print(Ph_list_film[3])


if __name__ == '__main__':
    main()
