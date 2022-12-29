import mysql.connector
import dbconfig as cfg

class rateDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into Christmas Movies (title, genre) values (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid



    def createtable(self):
        cursor = self.getcursor()
        sql="create table Christmas Movies (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, Title varchar(250), genre varchar (250))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql = "create database"+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

rateDao = rateDAO()

if __name__ == "__main__":
    rateDAO.createdatabase()
    rateDao.createtable()
    print("Done")