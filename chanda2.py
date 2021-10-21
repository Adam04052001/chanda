import csv
with open('Corp_Summary.csv', 'r', encoding = 'utf-8') as file:
    my_reader = csv.reader(file, delimiter = ';') #импортируем наши данные в питон, изменив кодировку
    first_data = []
    for row in my_reader:
        first_data.append(row)


def ierarchy(first_data):
    departments = {}                                  # создадим словарь для иерархии и будем мутить словарь в словаре
    for line in first_data[1:]:                   
        if line[1] not in departments:
            departments[line[1]] = [line[2]]
        if line[2] not in departments[line[1]]:
            departments[line[1]].append(line[2])
    return departments
        
                                 
def report(departments):
    workers_info = {}                                  # создадим новый словарь, куда будем включать наш отчёт
    wage_info = {}
    for line in first_data[1:]:
        if line[1] not in departments:
            departments[line[1]] = [line[2]]
        if line[2] not in departments[line[1]]:
            departments[line[1]].append(line[2])
        if line[1] not in workers_info:
            workers_info[line[1]] = {'Численность': 1}
            wage_info[line[1]] = {'Зарплата': [int(line[-1])]}
        workers_info[line[1]]['Численность'] += 1
        wage_info[line[1]]['Зарплата'].append(int(line[-1]))
        workers_info[line[1]]["min"] = min(wage_info[line[1]]["Зарплата"])        # найдём минимальное и максимальные значения путём использования встроенных функций в питоне
        workers_info[line[1]]["max"] = max(wage_info[line[1]]["Зарплата"])        
        workers_info[line[1]]['Средняя зарплата'] = round(sum(wage_info[line[1]]["Зарплата"]) / workers_info[line[1]]['Численность'])       # найдём среднее значение зарплаты путём суммы всех зарплат, поделённое на численность людей в департаменте   
    return workers_info


def csv_transform(workers_info):
    header = ['Название департамента','Численность', 'Min', 'Max', 'Средняя зп']
    data = []
    for k,v in workers_info.items():
        data.append(k.split()+list(workers_info[k].values()))
    with open('report.csv', 'w', encoding='UTF8', newline='') as file: #Вносим итоги в словарь
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


def menu():                                             # создадим пункт меню по аналогии с дз1. Сделаем словарь и введём туда ключи 1,2,3 - идентификаторы получаемых пунктов. Вызвав функцию menu() мы получим на выбор 3 цифры, соответствующие выполняемому запросу
    print(
        'Выберите пункт меню'
    )
    option = ''
    options = {'1': True, '2': False, '3': False}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
 
    if option == '1':
        print (ierarchy(first_data))
    if option == '2':
        print (report(ierarchy(first_data)))
    if option == '3':
        print (csv_transform(report(ierarchy(first_data))))
