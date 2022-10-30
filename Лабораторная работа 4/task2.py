main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
diсt_ = {}


def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    for klych in str_:
        if klych.isalpha() and klych not in diсt_:
            diсt_[klych] = 1
        else:
            if klych.isalpha():
                diсt_[klych] += 1
    return diсt_


def new_diсt_(diсt_):
    sum_ = sum(diсt_.values())
    for new in diсt_:
        diсt_[new] = round((diсt_[new] / sum_) * 100, 1)
    return diсt_

print(get_count_char(main_str))
print(new_diсt_(diсt_))