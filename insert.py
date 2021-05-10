def insert(strng):
    val = []
    count=0
    type_name = dictt('type_name')
    nam = dictt('name')
    mag = dictt('mag')
    
    #Проверка типа товара
    for i in range(len(type_name)):
        if type_name[i] in strng:
            val.append(type_name[i])
    if not val:
        t_n = input('What equipment did you buy?  ')
        val.append(t_n)
    #Проверка имени товара
    for i in range(len(nam)):
        if nam[i] in strng:
            val.append(nam[i])           
    if  len(val)==1:
        t_n= input(('What is your  company?' ))
        val.append(t_n)
    #Проверка магазина
    for i in range(len(mag)):
        if mag[i] in strng:
            val.append(mag[i])          
    if len(val) ==2:
        t_n= input(('Where did you buy the product?' ))
        val.append(t_n)
        
    #Проверка гарантии
    '''
    for i in range(len(strng)):
        if strng[i]== 'ends':
            print (strng[i]+ strng[i+1])'''
    t_n= input(('When does the warranty end?' ))
    
    t_n = DT.datetime.strptime(t_n, '%d.%m.%Y').date()
    val.append(t_n)
    t_n= input(('Add serial number:' ))
    val.append(t_n)
    t_n= input(('Add commet:' ))
    val.append(t_n)
    print(val)
    