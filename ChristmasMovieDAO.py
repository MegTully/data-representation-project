import mysql.connector
import dbconfig as cfg

class ChristmasMovieDAO:
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
        sql="insert into ChristmasMovies (title, genre) values (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
   
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from christmasMovies"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from christmasMovies where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql="update christmasMovies set title= %s, genre=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from christmasMovies where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete complete")

    def convertToDictionary(self, result):
        colnames=['id','title','genre']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

    def createtable(self):
        cursor = self.getcursor()
        sql="create table ChristmasMovies(id int AUTO_INCREMENT NOT NULL PRIMARY KEY, Title varchar(250), genre varchar (250))"
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
        sql = "create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

ChristmasMovieDao = ChristmasMovieDAO()

if __name__ == "__main__":
    #ChristmasMovieDao.createdatabase()
    #ChristmasMovieDao.createtable()

    data = ("Die Hard","Action")
    ChristmasMovieDao.create(data)
    print("Done")