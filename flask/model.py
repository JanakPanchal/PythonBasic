import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connector.connect(host='localhost',
										 database='fired',
										 user='root',
										 password='')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("You're connected to database: ", record)

except Error as e:
	print("Error while connecting to MySQL", e)


# insert , update , delete , alter
# three type of joins
# if we want data from more then one table that time we use join query
# inner join
# right join
# left join

def addnew_student(fname, lname, location):
	with connection.cursor() as cursor:
		query = "INSERT INTO `student` (`fname`, `lname`, `location`) VALUES (%s, %s, %s)"
		cursor.execute(query, (fname, lname, location))


def get_all_student():
	with connection.cursor() as cursor:
		sql = "SELECT fname , lname , location FROM `student`"
		cols = ['id', 'fname', 'lname', 'location']
		cursor.execute(sql)
		result = cursor.fetchall()
	return list(result)


def deleteuserfromdb(id):
	with connection.cursor() as cursor:
		sql = "DELETE FROM `paper` WHERE `id`=%s"
		cursor.execute(sql, id)
	return "true"


def updatestudent(id, fname):
	with connection.cursor() as cursor:
		sql = "UPDATE `student` SET `fname`=%s,`location`=%s WHERE `id` = %s"
		cursor.execute(sql, (id, fname, "canada"))
	return "Data is updated "