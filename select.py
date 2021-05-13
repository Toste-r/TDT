import psycopg2

def select(strng, type_q):
    con = connection()
    cur = con.cursor()

    #type_name = dictt('dictionary_type', 'NONE')
    #nam = dictt('dictionary_name', 'NONE')
    #mag = dictt('dictionary_mag', 'NONE')

    query = ''
    sel = ['find all', 'show all', 'show the whole table', 'show everything', 'find everything']
    query += 'select '

    al = ''
    count = 0
    clone = 0
    more = 0

    query_d = ''
    query_d += 'delete from Tech'
    
    #Вывести все в таблице
    for i in range(len(strng)):
        al+=strng[i]+' '
    #al.rstrip()
    #print(al)
    if al =='show all ':
        query+= "* FROM Tech"
        for i in range(len(type_name)):
            if type_name[i] in strng:
                if "* FROM Tech" not in query:
                    query += "* FROM Tech"
                more += 1
                if count < 1:
                    query += " WHERE Type_ = '" + type_name[i] + "'"
                    query_d += " WHERE Type_ = '" + type_name[i] + "'"
                    count += 1
                elif count >= 1 and more > 1:
                    query += " or  Type_ = '" + type_name[i] + "'"
                    query_d += " or  Type_ = '" + type_name[i] + "'"
                    count += 1
                else:
                    if clone == 0:
                        query += " and  Type_ = '" + type_name[i] + "'"
                        query_d += " and  Type_ = '" + type_name[i] + "'"
                        count += 1
                        clone += 1
                    elif clone != 0:
                        query += " or Type_ = '" + type_name[i] + "'"
                        query_d += " or Type_ = '" + type_name[i] + "'"
                        count += 1
                        clone += 1
        more = 0
        for i in range(len(nam)):
            if nam[i] in strng:
                if "* FROM Tech" not in query:
                    query += "* FROM Tech"
                more += 1
                if count < 1:
                    query += " WHERE Name_ = '" + nam[i] + "'"
                    query_d += " WHERE Name_ = '" + nam[i] + "'"
                    count += 1
                elif count >= 1 and more > 1:
                    query += " or  Name_ = '" + nam[i] + "'"
                    query_d += " or  Name_ = '" + nam[i] + "'"
                    count += 1
                else:
                    if clone == 0:
                        query += " and  Name_ = '" + nam[i] + "'"
                        query_d += " and  Name_ = '" + nam[i] + "'"
                        count += 1
                        clone += 1
                    elif clone != 0:
                        query += " or Name_ = '" + nam[i] + "'"
                        query_d += " or Name_ = '" + nam[i] + "'"
                        count += 1
                        clone += 1
        more = 0
        for i in range(len(mag)):
            if mag[i] in strng:
                if "* FROM Tech" not in query:
                    query += "* FROM Tech"
                more += 1
                if count < 1:
                    query += " WHERE Mag = '" + mag[i] + "'"
                    query_d += " WHERE Mag = '" + mag[i] + "'"
                    count += 1
                elif count >= 1 and more > 1:
                    query += " or  Mag = '" + mag[i] + "'"
                    query_d += " or  Mag = '" + mag[i] + "'"
                    count += 1
                else:
                    if clone == 0:
                        query += " and  Mag = '" + mag[i] + "'"
                        query_d += " and  Mag = '" + mag[i] + "'"
                        count += 1
                        clone += 1
                    elif clone != 0:
                        query += " or Mag = '" + mag[i] + "'"
                        query_d += " or Mag = '" + mag[i] + "'"
                        count += 1
                        clone += 1
                        more = 0
                        for i in range(len(strng)):
                            if strng[i] == 'number' and strng[i - 1] == 'serial':
                                if strng[i - 2] == 'no':
                                    if "* FROM Tech" not in query:
                                        query += "* FROM Tech"
                                    more += 1
                                    if count < 1:
                                        query += " WHERE Serial_n = 'none'"
                                        query_d += " WHERE Serial_n = 'none'"
                                        count += 1
                                    elif count >= 1 and more > 1:
                                        query += " or  Serial_n = 'none'"
                                        query_d += " or  Serial_n = 'none'"
                                        count += 1
                                    else:
                                        if clone == 0:
                                            query += " and  Serial_n = 'none'"
                                            query_d += "and  Serial_n = 'none'"
                                            count += 1
                                            clone += 1
                                        elif clone != 0:
                                            query += " or Serial_n = 'none'"
                                            query_d += " or Serial_n = 'none'"
                                            count += 1
                                            clone += 1
                            if len(strng) > 3:
                                if strng[i - 3] == 'serial' and strng[i - 2] == 'number' and strng[i - 1] == 'is':
                                    if "* FROM Tech" not in query:
                                        query += "* FROM Tech"
                                    more += 1
                                    if count < 1:
                                        query += " WHERE Serial_n = '" + strng[i] + "'"
                                        query_d += " WHERE Serial_n = '" + strng[i] + "'"
                                        print(strng[i])
                                        count += 1
                                    elif count >= 1 and more > 1:
                                        query += " or  Serial_n = '" + strng[i] + "'"
                                        query_d += " or  Serial_n = '" + strng[i] + "'"
                                        count += 1
                                    else:
                                        if clone == 0:
                                            query += " and  Serial_n = '" + strng[i] + "'"
                                            query_d += " and  Serial_n = '" + strng[i] + "'"
                                            print(strng[i])
                                            count += 1
                                            clone += 1
                                        elif clone != 0:
                                            query += " or Serial_n = '" + strng[i] + "'"
                                            query_d += " or Serial_n = '" + strng[i] + "'"
                                            print(strng[i])
                                            count += 1
                                            clone += 1

                        # print(query)
                        # print(query_d)
                        str_q = 0
                        str_d = 0
                        de = []
                        de_q = ''
                        de_q += 'delete from Tech '

                        td = []
                        if query == 'select ':
                            print('ERROR! VALUES DO NOT EXIST')
                            # messagebox.showerror("BogDan's ERROR","ERROR! VALUES DO NOT EXIST")
                        else:
                            if type_q == 'select':
                                show_table(query)
                                cur.execute(query)
                                rows = cur.fetchall()
                                for r in rows:
                                    str_q += 1
                                    # print(r)
                                    for i in range(len(r)):
                                        td.append(r[i])

                                th = ['TYPE', 'NAME', 'MAG', 'DATE', 'SERIAL NUMBER', 'COMMENT']
                                columns = len(th)
                                table = PrettyTable(th)

                                td_data = td[:]
                                while td_data:
                                    table.add_row(td_data[:columns:])
                                    td_data = td_data[columns:]

                                print(table)  # Печатаем таблицу
                            elif type_q == 'delete':
                                cur.execute(query)
                                rows = cur.fetchall()
                                for r in rows:
                                    str_q += 1
                                if str_q == 1:
                                    cur.execute(query_d)
                                elif str_q >= 2:
                                    cur.execute(query)
                                    rows = cur.fetchall()
                                    for r in rows:
                                        print(r)
                                    str_q = input('Enter line number: ')
                                    for r in rows:
                                        str_d += 1
                                        if str_d == int(str_q):
                                            for i in range(len(r)):
                                                de.append(r[i])
                                # print(de)
                                de_q += "where type_='" + str(de[0]) + "' and name_='" + str(
                                    de[1]) + "' and mag='" + str(de[2]) + "' and date_end='" + str(
                                    de[3]) + "' and serial_n ='" + str(de[4]) + "' and сomnt ='" + str(de[5]) + "';"
                                # print(de_q)
                                cur.execute(de_q)
                                con.commit()