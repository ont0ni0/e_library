from tkinter import *
from tkinter import messagebox
import sqlite3


# db
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books(
    surname TEXT,
    name TEXT,
    second_name TEXT,
    title TEXT,
    publisher TEXT,
    year INTEGER,
    bookcase INTEGER,
    shelf INTEGER);
    """)
conn.commit()


# func
def add_book_btn_clicked():
    # focus
    author_surname_txt.focus()
    # hide
    welcome_message.grid_remove()
    add_book_btn.grid_remove()

    # show
    author_surname.grid()
    author_surname_txt.grid()

    author_name.grid()
    author_name_txt.grid()

    author_second_name.grid()
    author_second_name_txt.grid()

    title.grid()
    title_txt.grid()

    year.grid()
    year_txt.grid()

    publisher.grid()
    publisher_txt.grid()

    bookcase.grid()
    bookcase_txt.grid()

    shelf.grid()
    shelf_txt.grid()

    send_to_base_btn.grid()
    main_menu_btn.grid()


def send_to_base_btn_clicked():
    try:
        # get & clear
        surname_db = author_surname_txt.get()
        name_db = author_name_txt.get()
        second_name_db = author_second_name_txt.get()
        title_db = title_txt.get()
        publisher_db = publisher_txt.get()
        year_db = year_txt.get()
        bookcase_db = bookcase_txt.get()
        shelf_db = shelf_txt.get()

        book_info = (surname_db, name_db, second_name_db, title_db,
                     publisher_db, year_db, bookcase_db, shelf_db)

        cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?, ?);", book_info)
        conn.commit()

        author_surname_txt.delete(0, END)
        author_name_txt.delete(0, END)
        author_second_name_txt.delete(0, END)
        title_txt.delete(0, END)
        publisher_txt.delete(0, END)
        year_txt.delete(0, END)
        bookcase_txt.delete(0, END)
        shelf_txt.delete(0, END)

        # focus
        author_surname_txt.focus()

        # info
        messagebox.showinfo('Отправка', 'Успешно!')

    except:
        messagebox.showerror('Отправка', 'Ой, возникла проблемка, обратитесь в поддержку!')


def main_menu_btn_clicked():
    # hide
    author_surname.grid_remove()
    author_surname_txt.grid_remove()

    author_name.grid_remove()
    author_name_txt.grid_remove()

    author_second_name.grid_remove()
    author_second_name_txt.grid_remove()

    title.grid_remove()
    title_txt.grid_remove()

    year.grid_remove()
    year_txt.grid_remove()

    publisher.grid_remove()
    publisher_txt.grid_remove()

    bookcase.grid_remove()
    bookcase_txt.grid_remove()

    shelf.grid_remove()
    shelf_txt.grid_remove()

    send_to_base_btn.grid_remove()
    main_menu_btn.grid_remove()

    # show
    welcome_message.grid()
    add_book_btn.grid()


def return_begin(event):
    author_surname_txt.focus()


def return_surname(event):
    author_name_txt.focus()


def return_name(event):
    author_second_name_txt.focus()


def return_second_name(event):
    title_txt.focus()


def return_title(event):
    year_txt.focus()


def return_year(event):
    publisher_txt.focus()


def return_publisher(event):
    bookcase_txt.focus()


def return_bookcase(event):
    shelf_txt.focus()


def return_shelf(event):
    shelf_txt.focus()


# window
window = Tk()
window.title('E-Library')
window.geometry('700x550')
window.iconbitmap('D:\e_library\icons\icon_1.ico')
###

# labels
welcome_message = Label(window, text='E-Library ver. 1.0')
welcome_message.grid(row=1, column=1, padx=10, pady=10)

author_surname = Label(window, text='Фамилия:')
author_surname.grid(row=0, column=0, padx=10, pady=10)
author_surname.grid_remove()

author_name = Label(window, text='Имя:')
author_name.grid(row=0, column=2, padx=10, pady=10)
author_name.grid_remove()

author_second_name = Label(window, text='Отчество:')
author_second_name.grid(row=0, column=4, padx=10, pady=10)
author_second_name.grid_remove()

title = Label(window, text='Название:')
title.grid(row=1, column=0, padx=10, pady=10)
title.grid_remove()

year = Label(window, text='Год выпуска:')
year.grid(row=2, column=0, padx=10, pady=10)
year.grid_remove()

publisher = Label(window, text='Издательство:')
publisher.grid(row=3, column=0, padx=10, pady=10)
publisher.grid_remove()

bookcase = Label(window, text='Шкаф №:')
bookcase.grid(row=4, column=0, padx=10, pady=10)
bookcase.grid_remove()

shelf = Label(window, text='Полка №:')
shelf.grid(row=4, column=2, padx=10, pady=10)
shelf.grid_remove()
###

# buttons
add_book_btn = Button(window, text='Добавить книгу', command=add_book_btn_clicked)
add_book_btn.grid(row=2, column=1, padx=10, pady=10)

send_to_base_btn = Button(window, text='Отправить в базу', command=send_to_base_btn_clicked)
send_to_base_btn.grid(row=5, column=0, padx=10, pady=10)
send_to_base_btn.grid_remove()

main_menu_btn = Button(window, text='Главное меню', command=main_menu_btn_clicked)
main_menu_btn.grid(row=5, column=1, padx=10, pady=10)
main_menu_btn.grid_remove()
###

# entry
author_surname_txt = Entry(window, width=10)
author_surname_txt.grid(row=0, column=1, padx=10, pady=10)
author_surname_txt.bind('<Return>', return_surname)
author_surname_txt.bind('<Right>', return_surname)
author_surname_txt.bind('<Left>', return_shelf)
author_surname_txt.grid_remove()

author_name_txt = Entry(window, width=10)
author_name_txt.grid(row=0, column=3, padx=10, pady=10)
author_name_txt.bind('<Return>', return_name)
author_name_txt.bind('<Right>', return_name)
author_name_txt.bind('<Left>', return_begin)
author_name_txt.grid_remove()

author_second_name_txt = Entry(window, width=10)
author_second_name_txt.grid(row=0, column=5, padx=10, pady=10)
author_second_name_txt.bind('<Return>', return_second_name)
author_second_name_txt.bind('<Right>', return_second_name)
author_second_name_txt.bind('<Left>', return_surname)
author_second_name_txt.grid_remove()

title_txt = Entry(window, width=10)
title_txt.grid(row=1, column=1, padx=10, pady=10)
title_txt.bind('<Return>', return_title)
title_txt.bind('<Right>', return_title)
title_txt.bind('<Left>', return_name)
title_txt.grid_remove()

year_txt = Entry(window, width=10)
year_txt.grid(row=2, column=1, padx=10, pady=10)
year_txt.bind('<Return>', return_year)
year_txt.bind('<Right>', return_year)
year_txt.bind('<Left>', return_second_name)
year_txt.grid_remove()

publisher_txt = Entry(window, width=10)
publisher_txt.grid(row=3, column=1, padx=10, pady=10)
publisher_txt.bind('<Return>', return_publisher)
publisher_txt.bind('<Right>', return_publisher)
publisher_txt.bind('<Left>', return_title)
publisher_txt.grid_remove()

bookcase_txt = Entry(window, width=10)
bookcase_txt.grid(row=4, column=1, padx=10, pady=10)
bookcase_txt.bind('<Return>', return_bookcase)
bookcase_txt.bind('<Right>', return_bookcase)
bookcase_txt.bind('<Left>', return_year)
bookcase_txt.grid_remove()

shelf_txt = Entry(window, width=10)
shelf_txt.grid(row=4, column=3, padx=10, pady=10)
shelf_txt.bind('<Right>', return_begin)
shelf_txt.bind('<Left>', return_publisher)
shelf_txt.grid_remove()
###

window.mainloop()

conn.commit()
conn.close()
