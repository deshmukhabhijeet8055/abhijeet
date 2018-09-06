#Connecting to database and retriving the data

import cx_Oracle

con_string = cx_Oracle.connect('abhijeet/abhijeet@inosnlt059:1521/NLTSFO59')
cur = con_string.cursor()
cur.execute('select * from DEPT')
for each_row in cur:
	print("{} - {} - {} ".format(each_row[0],each_row[1],each_row[2]))
cur.close()
con_string.close()

new_string = cx_Oracle.connect('REFUSER/REFUSER@inosnlt059:1521/NLTSFO59')
cur_1 = new_string.cursor()
cur_1.execute("select * from ASC_CONFIG where NAME = 'SFO_KitLayer.conf'")
print(type(cur_1))
for each_row in cur_1:
	abc = print("{}".format(each_row[1]))
	print(str(abc))
	with open('abc.xml','w') as f:
		f.write(abc)
	
cur_1.close()
new_string.close()