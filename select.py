from tkinter import messagebox


def select(strng, type_q):
    con = connection()
    cur = con.cursor()

    type_name = dictt('dictionary_type', 'NONE')
    nam = dictt('dictionary_name', 'NONE')
    mag = dictt('dictionary_mag', 'NONE')

    query = ''
    sel = ['find all', 'show all', 'show the whole table', 'show everything', 'find everything']
    query += 'select '

    al = ''
    count = 0
    clone = 0
    more = 0

    query_d = ''
    query_d += 'delete from Tech'