def dictt(typ,new):
    con = connection()
    cur = con.cursor() 
    
    dictionary_name=[]
    dictionary_mag=[]
    dictionary_type=[]

    cur.execute("SELECT * FROM dictionary_name")
    rows = cur.fetchall()
    for r in rows:
        dictionary_name.append(r[0])
        
    cur.execute("SELECT * FROM dictionary_type")
    rows = cur.fetchall()
    for r in rows:
        dictionary_type.append(r[0])
    
    cur.execute("SELECT * FROM dictionary_mag")
    rows = cur.fetchall()
    for r in rows:
        dictionary_mag.append(r[0])
    
    if new == 'NONE':
        if typ == 'dictionary_name':
            return dictionary_name
        if typ == 'dictionary_type':
            return dictionary_type
        if typ == 'dictionary_mag':
            return dictionary_mag
    else:
        q=''
        q += "INSERT INTO "+ typ +" VALUES( '"+new+"');"
        #print(q)
        cur.execute(q)
        con.commit()