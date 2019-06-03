# -*- coding: utf-8 -*-

gip = []
with open("gipoteza.txt") as handle:   #открываем файл с гипотезами
    for line in handle:
        gip.append([str(x) for x in line.split()])
handle.close()

svid = []
with open("svidetel.txt") as handle:   #открываем файл со свидетельсвами
    for line in handle:
        svid.append([str(x) for x in line.split()])
handle.close()

n = 0
while n < 7:
    Ce = 0  #цена
    N = 0
    
    for i in gip:
        Ce = ((float(i[4])*float(i[1]))/(float(i[4])*float(i[1])+float(i[5])*(1-float(i[1]))))-(((1-float(i[4]))*float(i[1]))/(1-float(i[4])*float(i[1])-float(i[5])*(1-float(i[1]))))
        if Ce < 0:
            Ce = Ce*(-1)
        N = i[3]
        for i in svid:
            if i[0] == N:
                i[2] = Ce
    #print(svid)
    
    for i in gip:
        PHE = (float(i[4])*float(i[1]))/(float(i[4])*float(i[1])+float(i[5])*(1-float(i[1])))
        i[6] = PHE
        PH_E = ((1-float(i[4]))*float(i[1]))/(1-float(i[4])*float(i[1])-float(i[5])*(1-float(i[1])))
        i[7] = PH_E
#выбор вопроса по цене    
    max_list = []
    max_ce = 0
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
        for i in gip:
            if i[3] == svid_pred_num:
                i[1] = i[6]
        for i in svid:
            if svid_pred_num == i[0]:
                i[3] = '1'
    elif yn == 'нет':
        for i in gip:
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
    for i in gip:
        if i[2] == '1':
            Ph_1 += float(i[1])
        if i[2] == '2':
            Ph_2 += float(i[1])
        if i[2] == '3':
            Ph_3 += float(i[1])
        if i[2] == '4':
            Ph_4 += float(i[1])
    Ph_list.append(Ph_1)
    Ph_list.append(Ph_2)
    Ph_list.append(Ph_3)
    Ph_list.append(Ph_4)
    Ph_list_film =['Припять','Мальчишник','Виноваты_звезды','Горько']
    for i in gip:
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
    