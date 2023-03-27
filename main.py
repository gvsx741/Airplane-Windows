from tkinter import *
from PIL import ImageTk, Image
import sys

root = Tk()
root.geometry('450x330')
root.resizable(width=False, height=False)
root.title("Горностаєв В.С.")

canvas = Canvas(root, width=800, height=600)
canvas.pack()


# создаем класс со списком, атрибутоми и методами
class MyList:
    # Инициализация листа
    def __init__(
            self):  
        self.My_list = ["                                                    "] * 5

    # добавление новых элементов в конец списка
    def Mylist_append(self, element):
        self.My_list += [element]

    # изминение элементов списка
    def change_element_list(self, number, NewElement):
        self.My_list[number] = NewElement

    # сортировка списка
    def sort_my_list(self):
        self.My_list.sort(key=len)  # решил упростить себе жизнь и не изобретать велосипед

    # удаление элемента из списка
    def delete_element(self, number):
        for x in range(len(self.My_list)):
            if self.My_list[number - 1] == self.My_list[number]:
                del self.My_list[number]
                break
            elif number == len(self.My_list) - 1:
                del self.My_list[number]
                break
            self.My_list[number] = self.My_list[number + 1]
            number += 1

    # проверка списка на содержание
    def check_list_content(self):
        if len(self.My_list) == 0:
            print('Отсутствуют элементы списка!')

    # перестановка элементов в обратном направлении
    def list_mirroring(self):
        temp = [0, -1]
        temp_list = [0] * (len(self.My_list))
        for temp[0] in range(len(self.My_list)):
            temp_list[temp[0]] = self.My_list[temp[0]]
        temp[0] = 0
        for temp[0] in range(len(self.My_list)):
            self.My_list[temp[0]] = temp_list[temp[-1]]
            temp[1] -= 1
        del temp
        del temp_list

    # проверка на размер списка
    def list_size_check(self, number):
        if number <= len(self.My_list):
            print('размер не превышается')
        else:
            print('превышается размер!')


# создаём класс самолёт
class MyAirplane:
    def __init__(self, ImageName):
        self.image = self.load_image(ImageName)
        self.date_of_creation = tuple()
        self.data_of_airplane = MyList()

        self.LCompany = Label(root)
        self.LName = Label(root)
        self.LWeight = Label(root)
        self.LSpeed = Label(root)
        self.LDateOfCreation = Label(root)

    def set_company(self, company):
        self.data_of_airplane.My_list[0] = company
        self.LCompany = Label(root, text=f"Company: {self.get_company()}").place(x=210, y=60)

    def get_company(self):
        return self.data_of_airplane.My_list[0]

    def set_name(self, name):
        self.data_of_airplane.My_list[1] = name
        self.LName = Label(root, text=f"Name: {self.get_name()}").place(x=210, y=80)

    def get_name(self):
        return self.data_of_airplane.My_list[1]

    def set_weight(self, weight):
        self.data_of_airplane.My_list[2] = weight
        self.LWeight = Label(root, text=f"Weight: {self.get_weight()}").place(x=210, y=100)

    def get_weight(self):
        return self.data_of_airplane.My_list[2]

    def set_speed(self, speed):
        self.data_of_airplane.My_list[3] = speed
        self.LSpeed = Label(root, text=f"Speed: {self.get_speed()}").place(x=210, y=120)

    def get_speed(self):
        return self.data_of_airplane.My_list[3]

    def set_date_of_creation(self, date):
        del self.date_of_creation
        self.date_of_creation = (date)

    def load_image(self, ImageName):
        img = Image.open(f"{ImageName}.jpg")
        img.thumbnail((200, 200), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def set_image(self):
        canvas.delete("all")
        canvas.create_image(100, 115, image=self.image)

        self.LCompany = Label(root, text=f"Company: {self.get_company()}").place(x=210, y=60)
        self.LName = Label(root, text=f"Name: {self.get_name()}").place(x=210, y=80)
        self.LWeight = Label(root, text=f"Weight: {self.get_weight()}").place(x=210, y=100)
        self.LSpeed = Label(root, text=f"Speed: {self.get_speed()}").place(x=210, y=120)


# класс для ввода данных в новом доп. окне
class popupWindow:
    def __init__(self, element):
        self.element = element
        top = self.top = Toplevel(root)
        top.geometry("200x150")
        top.resizable(width=False, height=False)
        top.title(f"Set {self.element}")
        self.labelTop = Label(top, text=f"Enter {self.element}").place(relx=.35, rely=.2)
        self.entryTop = Entry(top)
        self.entryTop.pack()
        self.entryTop.place(relx=.22, rely=.4)
        self.buttonTop = Button(top, text="Save", width=8, command=self.save_text).place(relx=.35, rely=.6)

        global WhatAirplane
        if WhatAirplane == 0:
            self.temp = Airplane1
        elif WhatAirplane == 1:
            self.temp = Airplane2
        elif WhatAirplane == 2:
            self.temp = Airplane3
        elif WhatAirplane == 3:
            self.temp = Airplane4

    def save_text(self):
        if self.element == "Company":
            self.temp.set_company(self.entryTop.get())
            self.top.destroy()
        elif self.element == "Name":
            self.temp.set_name(self.entryTop.get())
            self.top.destroy()
        elif self.element == "Weight":
            self.temp.set_weight(self.entryTop.get())
            self.top.destroy()
        elif self.element == "Speed":
            self.temp.set_speed(self.entryTop.get())
            self.top.destroy()
        elif self.element == "Date of creation":
            self.temp.set_date_of_creation(self.entryTop.get())
            self.top.destroy()


# класс для работы с файлами через доп. окно
class popupSaveWnidow():
    def __init__(self):
        top = self.top = Toplevel(root)
        top.geometry("200x150")
        top.resizable(width=False, height=False)
        top.title("Save as")
        self.labelTop = Label(top, text="Enter text:").place(x=40, y=10)
        self.entryTop = Entry(top)
        self.entryTop.pack()
        self.entryTop.place(x=40, y=35)
        self.buttonSaveTxt = Button(top, text="Save .txt", width=8, command=self.save_as_txt).place(x=40, y=60)
        self.buttonSaveCsv = Button(top, text="Save .csv", width=8, command=self.save_as_csv).place(x=40, y=90)
        self.buttonSaveBin = Button(top, text="Save .bin", width=8, command=self.save_as_bin).place(x=40, y=120)
        self.buttonShowTxt = Button(top, text="Show .txt", width=8, command=self.show_file_txt).place(x=110, y=60)
        self.buttonShowCsv = Button(top, text="Show .csv", width=8, command=self.show_file_csv).place(x=110, y=90)
        self.buttonShowBin = Button(top, text="Show .bin", width=8, command=self.show_file_bin).place(x=110, y=120)

    def save_as_txt(self):
        self.file = open('text.txt', 'a')
        self.file.write(self.entryTop.get() + '\n')
        self.file.close()

    def save_as_csv(self):
        self.file = open('text.csv', 'a')
        self.file.write(self.entryTop.get() + '\n')
        self.file.close()

    def save_as_bin(self):
        self.file = open('text.bin', 'a')
        self.file.write(self.entryTop.get() + '\n')
        self.file.close()

    def show_file_txt(self):
        topWin = self.topWin = Toplevel(root)
        topWin.geometry("200x150")
        topWin.title(".txt")
        self.file = open('text.txt')
        self.temp = self.file.read()
        self.file.close()
        self.labelTopWin = Label(topWin, text=f"{self.temp}").place(x=40, y=20)
        self.buttonOK = Button(topWin, text="OK", width=8, command=self.ok).place(relx=0.35, rely=0.8)

    def show_file_csv(self):
        topWin = self.topWin = Toplevel(root)
        topWin.geometry("200x150")
        topWin.title(".csv")
        self.file = open('text.csv')
        self.temp = self.file.read()
        self.file.close()
        self.labelTopWin = Label(topWin, text=f"{self.temp}").place(x=40, y=20)
        self.buttonOK = Button(topWin, text="OK", width=8, command=self.ok).place(relx=0.35, rely=0.8)

    def show_file_bin(self):
        topWin = self.topWin = Toplevel(root)
        topWin.geometry("200x150")
        topWin.title(".bin")
        self.file = open('text.bin')
        self.temp = self.file.read()
        self.file.close()
        self.labelTopWin = Label(topWin, text=f"{self.temp}").place(x=40, y=20)
        self.buttonOK = Button(topWin, text="OK", width=8, command=self.ok).place(relx=0.35, rely=0.8)

    def ok(self):
        self.topWin.destroy()


Airplane1 = MyAirplane("air1")
Airplane2 = MyAirplane("air2")
Airplane3 = MyAirplane("air3")
Airplane4 = MyAirplane("air4")


def ChangeAirplane1():
    global WhatAirplane
    WhatAirplane = 0
    Airplane1.set_image()


def ChangeAirplane2():
    global WhatAirplane
    WhatAirplane = 1
    Airplane2.set_image()


def ChangeAirplane3():
    global WhatAirplane
    WhatAirplane = 2
    Airplane3.set_image()


def ChangeAirplane4():
    global WhatAirplane
    WhatAirplane = 3
    Airplane4.set_image()


def Set_Company():
    popupWindow("Company")


def Set_Name():
    popupWindow("Name")


def Set_Weight():
    popupWindow("Weight")


def Set_Speed():
    popupWindow("Speed")


def Set_Date_of_creation():
    popupWindow("Date of creation")


def Save_As():
    popupSaveWnidow()


btn1 = Button(root, text="Airplane1", width=25, command=ChangeAirplane1)
btn1.place(x=25, y=240)

btn2 = Button(root, text="Airplane2", width=25, command=ChangeAirplane2)
btn2.place(x=240, y=240)

btn3 = Button(root, text="Airplane3", width=25, command=ChangeAirplane3)
btn3.place(x=25, y=280)

btn4 = Button(root, text="Airplane4", width=25, command=ChangeAirplane4)
btn4.place(x=240, y=280)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
sevemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Set Company", command=Set_Company)
filemenu.add_command(label="Set Name", command=Set_Name)
filemenu.add_command(label="Set Weight", command=Set_Weight)
filemenu.add_command(label="Set Speed", command=Set_Speed)
filemenu.add_command(label="Set Date of creation", command=Set_Date_of_creation)
sevemenu.add_command(label="Save as", command=Save_As)

mainmenu.add_cascade(label="Add", menu=filemenu)
mainmenu.add_cascade(label="Save as", menu=sevemenu)

root.mainloop()
