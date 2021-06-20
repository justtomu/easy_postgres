from post import Postgres
from icecream import ic

sql = Postgres()

sql.create_table('users', """
    username varchar,
    user_id bigint,
    history varchar
""")


ic(sql.insert('users', ('aaaa', 2223123, None)))
ic(sql.insert('users', ('aaab', 3223123, None)))
ic(sql.insert('users', ('wwww', 4223123, None)))
ic(sql.insert('users', ('qqqq', 5223123, None)))

ic(sql.select('users', 'username, user_id', 'username = %s', values=('wwww',), one=True))
ic(sql.select('users', '*'))
sql.update('users', 'username = %s where user_id = %s', values=('qqqq', 2223123))
sql.delete('users', 'user_id = %s', values=(7,))
ic(sql.show_table('users'))
ic(sql.get_count('users'))

sql.delete_all('users')
sql.disconnect()

