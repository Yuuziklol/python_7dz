def add_column(data):
    with open('column_base.txt', 'a', encoding='utf=8') as file:
        file.write(f'Фамилия: {data[0]}; Имя: {data[1]}; Номер телефона: {data[2]}; Описание: {data[3]}\n')
def add_line(data):
     with open('line_base.txt', 'a',encoding='utf=8') as file:
        file.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nОписание: {data[3]}\n\n')