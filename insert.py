def insert(strng):
    val = []
    count=0
    type_name = dictt('dictionary_type','NONE')
    nam = dictt('dictionary_name','NONE')
    mag = dictt('dictionary_mag','NONE')
    con=connection()
    cur = con.cursor()
    
    root = Tk()
    root.title("GUI на Python")
    root.geometry("300x250")
    
    #Проверка типа товара
    for i in range(len(type_name)):
        if type_name[i] in strng:
            val.append(type_name[i])
    if not val:

        t_n = input('What equipment did you buy?  ')
        val.append(t_n)
        if t_n not in type_name and t_n !='':
            dictt('dictionary_type',t_n)
        
    #Проверка имени товара
    for i in range(len(nam)):
        if nam[i] in strng:
            #print(nam[i])
            #print(strng)
            val.append(nam[i])           
    if  len(val)==1:
        t_n= input(('which company is your product?  ' ))
        val.append(t_n)
        if t_n not in nam and t_n !='':
            dictt('dictionary_name',t_n)
        
    #Проверка магазина
    for i in range(len(mag)):
        if mag[i] in strng:
            val.append(mag[i])
    if len(val) ==2:
        try:
            for i in range(len(strng)):
                if strng[i]=='from':
                    val.append(strng[i+1])
                    if t_n not in mag and t_n !='':
                        dictt('dictionary_mag',strng[i+1])
        except :
            if len(val)==2:
                t_n= input(('Where did you buy the product?  ' ))
                val.append(t_n)
                if t_n not in mag and t_n !='':
                    dictt('dictionary_mag',t_n)
        if len(val)==2:
            t_n= input(('Where did you buy the product?  ' ))
            val.append(t_n)
            if t_n not in mag and t_n !='':
                dictt('dictionary_mag',t_n)
            
    #Проверка ввода гарантии
    t_n= input(('When does the warranty end?  ' ))
    try:
        t_n = DT.datetime.strptime(t_n, '%d.%m.%Y').date()
        val.append(t_n)
    except ValueError:
        val.append('0001-01-01')
        #val.append('')
    
    #Ввод серийника
    t_n= input(('Add serial number: ' ))
    val.append(t_n)
    
    #Ввод комментария
    t_n= input(('Add comment:  ' ))
    val.append(t_n)
    for i in range(len(val)):
        if val[i]=='' :#and i != 3:
            val[i]=NONE
    if val[0]==NONE and val[1]==NONE:
        print('ADD TYPE AND NAME')
        messagebox.showerror("BogDan's ERROR","ADD TYPE AND NAME")
    else:
        for i in range(len(val)):
            val[i]=str(val[i])
            val[i]=val[i].lower()
        q=''
        q += "insert into tech values('"+str(val[0])+"','"+str(val[1])+"','"+str(val[2])+"','"+str(val[3])+"','"+str(val[4])+"','"+str(val[5])+"');"
        print(q)
        cur.execute(q)
        con.commit()