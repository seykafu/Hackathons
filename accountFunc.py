import sqlPython as sqlpy

# Syntax
'''
sqlpy.selectCmd("SELECT * FROM account WHERE password='hackers'")

'''

def createAccount(username, password):
	sqlCom = 'INSERT INTO account (username, password, coins, currCO2, currMilage) values (%s,%s,%s,%s,%s)'

	cursor = sqlpy.connection.cursor()
	try:
		cursor.execute(sqlCom, (username,password,0.0,0.0,0.0))
	except:
		print 'There was a problem creating an account in database'
		return -1
	cursor.fetchone()
	sqlpy.connection.commit()
	return 0

def getAccountInfoFromID(idNum):
	# We find an account based on the user id
	# If id does not exist, this returns None
	idNum = str(idNum)
	res = sqlpy.selectCmd("SELECT * FROM account WHERE id="+idNum+";")

	return res

def getCoinsById(idNum):
	# We get coins based on ID
	idNum = str(idNum)
	return sqlpy.selectCmd("SELECT coins FROM account WHERE id="+idNum+";")[0]

def updateCoinsById(idNum, coinValue):
	sqlpy.sequel("UPDATE account SET coins="+coinValue+" WHERE id="+idNum+";")



