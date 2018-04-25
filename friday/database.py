import MySQLdb
conn = MySQLdb.connect( host='table', user= 'manish', password= 'gupta' )
cursor = conn.cursor()
cursor.execute(' Create database table ')
    cursor.execute('use table')
    table ='create table friend(friend_name char(30),friend_type char(30))'
    cursor.execute(table)
    cursor.execute('select * from table )
