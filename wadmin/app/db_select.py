import os
os.environ["NLS_LANG"] = "Russian.AL32UTF8"

import cx_Oracle

db_login = 'login'
db_pass = 'pass'
db = '@host/base'

#получаем количество клиентов ик
def get_active_ik():
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select count(*) from table where some_condition')
    count_ik = []
    for result in cur:
    	count_ik.append(result[0])
    cur.close()
    con.close()
    return "Активных клиентов ик: " + str(count_ik[0])

#получаем количество клиентов бк
def get_active_bk():
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select count(*) from table where some_condition')
    count_bk = []
    for result in cur:
    	count_bk.append(result[0])
    cur.close()
    con.close()
    return "Активных клиентов бк: " + str(count_bk[0])

#получаем арм клиента
def get_client_arm(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select item from table where inn = ' + str(inn))
    client_arm = []
    for result in cur:
    	client_arm.append(result[0])
    cur.close()
    con.close()
    return client_arm

#получаем название клиента
def get_client_name(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select item from table where inn = ' + str(inn))
    client_name = []
    for result in cur:
    	client_name.append(result[0])
    cur.close()
    con.close()
    return client_name

#получаем статус клиента
def get_client_fenabled(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select item from table where inn = ' + str(inn))
    client_fenabled = []
    for result in cur:
    	client_fenabled.append(result[0])
    cur.close()
    con.close()
    if client_fenabled[0] == 1.0:
        return "блокирован"
    else:
        return "активный"

#получаем дату начала обслуживания клиента
def get_client_start_date(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select date from table where inn = ' + str(inn))
    client_start = []
    for result in cur:
    	client_start.append(result[0])
    cur.close()
    con.close()
    return client_start

#получаем дату блокировки клиента
def get_client_finish_date(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select date from table where inn = ' + str(inn))
    client_finish = []
    for result in cur:
    	client_finish.append(result[0])
    cur.close()
    con.close()
    return client_finish

#получаем информацию о логине
def get_login_info(login):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select item from table where login = ' + str(login))
    login = []
    for result in cur:
    	login.append(result[0])
    cur.close()
    con.close()
    if len(login) == 0:
        con = cx_Oracle.connect(db_login + db_pass + db)
        cur = con.cursor()
        cur.execute('select item from table where login = ' + str(login))
        login_new = []
        for result in cur:
        	login_new.append(result[0])
        cur.close()
        con.close()
        if len(login_new) == 0:
            return "Логин не предназначен для подключения к ЮЛ"
        else:
            return "Логин предназначен для подключения к ЮЛ"
    else:
        return "Логин пренадлежит подписанту: " + str(login[0])

#получаем запрос клиента для обработки акта
def get_akt(inn):
    con = cx_Oracle.connect(db_login + db_pass + db)
    cur = con.cursor()
    cur.execute('select item from table  where inn = '+str(inn))
    query = []
    for result in cur:
    	query.append(result[0])
    cur.close()
    con.close()
    if len(query) == 0: #если у клиента нет подходящих ключей для запроса
        return "Нет запроса"
    else: #если у клиента есть подходящий ключ
        con = cx_Oracle.connect(db_login + db_pass + db)
        cur = con.cursor()
        #получаем информацию о запросе
        cur.execute('select arm, date, time from table where inn ='+str(inn))
        arm = []
        date = []
        time = []
        for result in cur:
            arm.append(result[0])
            date.append(result[1])
            time.append(result[2])
        cur.close()
        con.close()
        if len(arm) != 0:
            return str(arm[0])+'_'+str(date[0])+'_'+str(time[0])+'.req' #имя файла запроса
        else:
            return "Нет запроса"
