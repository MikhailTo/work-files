import os
import pandas as pd

slash = '\\'
rights = 0o777
exist_ok = True
name_input_file = 'data.xlsx'
name_input_folder = 'data'
name_result_folder = 'result'

def get_columns(column_numbers):
    list_colnums = column_numbers.split(',')
    print(list_colnums)
    return [int(colnum) for colnum in list_colnums]


def get_root(name_general_root_folder='result', name_root_folder=''):
    return os.getcwd() + slash + name_general_root_folder + slash + name_root_folder


def get_excel(path_input):
    return pd.read_excel(path_input)


def make_folders(paths, rights=0o777, exist_ok=True):
    for path in paths:
        os.makedirs(path, rights, exist_ok)


def get_paths(excel_file, path_result, cols):
    result = []
    path_str = ''
    df = excel_file
    for i, row in df.iterrows():
        for el in range(len(cols)):
            cell = str(row[cols[el]])\
                .lstrip()\
                .rstrip()\
                .replace("/", "-")\
                .replace(" ", "_") \
                .replace("\"", "") \
                .replace("\'", "") \
                .replace(":", "") \
                if not pd.isna(row[cols[el]]) \
                else ''

            if (cell != ''):
                path_str = path_str + slash + str(cell)

        if (path_str != ''):
            result.append(path_result + path_str)
        path_str = ''
    return list(set(result))


if __name__ == '__main__':
    # '0, 1, 2, 3, 4, 5' ["Цех", "Группа", "Преобразователь", "Тип преобразователя", "Помещение", "Шкаф/привод-Агрегат"]
    name_root_folder = input('Enter name of root folder:')
    column_numbers = input('Enter numbers of column (like \'0, 1, 4, 5\'):')

    excel = get_excel(get_root(name_input_folder, name_input_file))
    make_folders(get_paths(
                    excel,
                    get_root(name_result_folder, name_root_folder),
                    get_columns(column_numbers)))


