from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('450x330')

# создаем картеж.
number = 0
tpl = ('gray', 'blue')


# создаем класс со списком, атрибутоми и методами
class MyList:
    color_list = [1, 2, 3, 4]

    # создаю приватные атрибуты
    __a = color_list[0]
    __b = color_list[1]
    __c = color_list[2]
    __d = color_list[3]

    def List_atributs(self):
        print(self.__a, self.__b, self.__c, self.__d)

    # добавление новых элементов в конец списка
    def color_list_append(color):
        MyList.color_list += [color]

    # изминение элементов списка
    def change_element_list(number, NewElement):
        MyList.color_list[number] = NewElement

    # сортировка списка
    def sort_my_list(color_lost):
        MyList.color_list.sort(key=len)  # решил упростить себе жизнь и не изобретать велосипед

    # удаление элемента из списка
    def delete_element(number):
        for x in range(len(MyList.color_list)):
            if MyList.color_list[number - 1] == MyList.color_list[number]:
                del MyList.color_list[number]
                break
            elif number == len(MyList.color_list) - 1:
                del MyList.color_list[number]
                break
            MyList.color_list[number] = MyList.color_list[number + 1]
            number += 1

    # проверка списка на содержание
    def check_list_content(self):
        if len(MyList.color_list) == 0:
            print('Отсутствуют элементы списка!')

    # перестановка элементов в обратном направлении
    def list_mirroring(self):
        temp = [0, -1]
        temp_list = [0] * (len(MyList.color_list))
        for temp[0] in range(len(MyList.color_list)):
            temp_list[temp[0]] = MyList.color_list[temp[0]]
        temp[0] = 0
        for temp[0] in range(len(MyList.color_list)):
            MyList.color_list[temp[0]] = temp_list[temp[-1]]
            temp[1] -= 1
        del temp
        del temp_list

    # проверка на розмер списка
    def list_size_check(number):
        if number <= len(MyList.color_list):
            print('размер не превышается')
        else:
            print('превышается размер!')


# тут я проверял коректность работы
MyList.color_list_append('gray')
MyList.color_list_append('blue')
MyList.color_list_append('black')
MyList.color_list_append('white')

print(MyList.color_list)

#вывожу заданные атрибуты
MyList.List_atributs(MyList)

canvas = Canvas(root, width=800, height=600)
canvas.pack()

# добавил изменение цвета в нижней части экрана. Цвет зависит от данных нам цветов в кортеже.
frame = Frame(root, bg=tpl[number])
frame.place(relheight=1, rely=0.65, relwidth=1)


def load_image(name):
    img = Image.open(name)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def set_image(image):
    canvas.delete("all")
    canvas.create_image(100, 115, image=image)


image = load_image("air1.jpg")
image2 = load_image("air2.jpg")
image3 = load_image("air3.jpg")
image4 = load_image("air4.jpg")


def air():
    t1['text'] = "Літак №1"
    set_image(image)


def air2():
    t1['text'] = "Літак №2"
    set_image(image2)


def air3():
    t1['text'] = "Літак №3"
    set_image(image3)


def air4():
    t1['text'] = "Літак №4"
    set_image(image4)


t1 = Label(root)
t1.place(x=200, y=50)

# добавил надпись которая выводит содержимое списка.
t2 = Label(root)
t2.place(x=210, y=190)
t2['text'] = str(MyList.color_list[number])

btn1 = Button(root, text="1)Літак", width=25, command=air)
btn1.place(x=25, y=240)

btn2 = Button(root, text="2)Літак", width=25, command=air2)
btn2.place(x=240, y=240)

btn3 = Button(root, text="3)Літак", width=25, command=air3)
btn3.place(x=25, y=280)

btn4 = Button(root, text="4)Літак", width=25, command=air4)
btn4.place(x=240, y=280)

root.mainloop()
