import sqlite3 as sq


async def dp_connect():
    global db, cur #пока так для пр

    db = sq.connect('new.db')#если такой базы нет, то она будет создаваться(папка с базой данных)
    cur = db.cursor()#экземпляр курсора для взаимодействоя с базой данной с помощью этого инструмента

    cur.execute("CREATE TABLE IF NOT EXISTS pr(pr_id INTEGER PRIMARY KEY, title TEXT, photo TEXT)")#обращаемся к методу и составляем запррос, после создания таблицы. pr(указываем индентификатор.тк праймари кей то данное таблица бует содержать уникальные ..тип будет целочисленный тк

    db.commit()#далее после изм5енения.. завершаем нашу операцию
#берем все города из таблицы pr
async def get_all_pr():
    pr = cur.execute("SELECT * FROM pr").fetchall()#взять все из таблицы pr и отлавливаем
    return pr

async def create_new_pr(state):
    #воспользуемся ассинхронным менеджером контекста
    async with state.proxy() as data:
        pr = cur.execute("INSERT INTO pr (title, photo) VALUES(?, ?)", (data['title'], data['photo']))#cql запрос
        db.commit()
    # pr = cur.execute("INSERT INTO pr VALUES(?, ?)", (title, photo_id))#cql запрос
    # db.commit()

    return pr

async def delete_pr(pr_id: int)->None:#позволяет вносить изменения (удаляет). мы обращаемся к объекту курсора и вызываем execute
    cur.execute("DELETE FROM pr WHERE pr_id=?", (pr_id,))
    db.commit()
#
# #mysql
# def sqlite_start():
#     global base, cur
#     base = sq.connect("idname.db")
#     cur = base.cursor()
#     if base:
#         print('Data base connected OK!')
#     base.execute('CREATE TABLE IF NOT EXISTS name(name TEXT, id TEXT PRIMARY KEY)')
#     base.commit()
#
# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO name VALUES(?, ?)', tuple(data.values()))
#         base.commit()
#
#     base.close()


