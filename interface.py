import add_to_doc
import input_data
import find_in_doc

def button_click():
    key = int(input('Введите 1,чтобы добавить в список\nВведите 0,чтобы показать список '))
    if key == 1:
        list = input_data.inp_data()
        add_to_doc.add_column(list)
        add_to_doc.add_line(list)
    elif key == 0:
        print(find_in_doc.all_list())
