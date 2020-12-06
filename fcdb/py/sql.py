import pyodbc
from cryptography.fernet import Fernet

import properties

class Sql:
    def __init__(self, database, server="DESKTOP-1IVLKJU\SQLSERVER"):
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.cursor = self.cnxn.cursor()

    def checkPassword(self, login, password):
        cipher = Fernet(properties.cipher_key)
        self.cursor.execute("SELECT ID_пользователя, Пароль, Роль FROM Пользователи where Логин='" + login + "'")
        row = self.cursor.fetchone()
        if row is not None:
            passw = cipher.decrypt(str.encode(row[1])).decode('utf8')
            if passw == password:
                return True, row[2], row[0]
            else:
                return False, row[2], row[0]
        else:
            return False, 0, 0

    def addUser(self, login, password, role):
        cipher = Fernet(properties.cipher_key)
        encrypted_password = password.encode('utf8')
        encrypted_password = cipher.encrypt(encrypted_password)
        try:
            self.cursor.execute("INSERT INTO Пользователи(Логин, Пароль, Роль) "
                              "VALUES ('" + login + "','" + encrypted_password.decode("utf-8") + "'," + str(role) + ")")
            self.cnxn.commit()
            self.cursor.execute("SELECT ID_пользователя from Пользователи where Логин='" + login + "'")
            row = self.cursor.fetchone()
            return True, row[0]
        except pyodbc.Error as e:
            print(e)
            return False, 0

    def addFan(self, id, name, surname, gender, birthday):
        name = name.rstrip()
        surname = surname.lstrip()
        fio = name + " " + surname
        try:
            self.cursor.execute("INSERT INTO Болельщики(ФИО, Пол, Дата_рождения, ID_пользователя) "
                              "VALUES ('" + fio + "','" + gender + "', '" + birthday + "',"+ str(id) +")")
            self.cnxn.commit()
            return True
        except pyodbc.Error as e:
            print(e)
            return False


    def updatePassword(self, login, password):
        cipher = Fernet(properties.cipher_key)
        encrypted_password = password.encode('utf8')
        encrypted_password = cipher.encrypt(encrypted_password)
        self.cursor.execute("UPDATE Пользователи SET Пароль='"+encrypted_password.decode("utf-8")+"' where Логин='"+login+"'")
        self.cnxn.commit()