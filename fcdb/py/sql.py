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
        fio = (name + " " + surname).rstrip()
        try:
            self.cursor.execute("INSERT INTO Болельщики(ФИО, Пол, Дата_рождения, ID_пользователя) "
                              "VALUES ('" + fio + "','" + gender + "', '" + birthday + "',"+ str(id) +")")
            self.cnxn.commit()
            return True
        except pyodbc.Error as e:
            print(e)
            return False

    def addPlayer(self, id, name, surname, nation, birthday, pos, number, height, weight):
        name = name.rstrip()
        surname = surname.lstrip()
        fio = (name + " " + surname).rstrip()
        if (pos == "Вратарь"):
            pos = "В"
        elif (pos == "Защитник"):
            pos = "З"
        elif (pos == "Полузащитник"):
            pos = "П"
        elif (pos == "Нападающий"):
            pos = "Н"
        try:
            self.cursor.execute("INSERT INTO Футболисты(ФИО, Национальность, Дата_рождения, Позиция, Номер_футболиста, Рост, Вес, ID_пользователя) "
                                "VALUES ('"+ fio +"', '" + nation +"', '" +birthday + "', '" +pos +"', " + str(number) +", " + str(height) + ", " + str(weight).replace(',','.') + ", "+ str(id) +")")
            self.cnxn.commit()
            self.cursor.execute("SELECT ID_футболиста from Футболисты where Номер_футболиста=" + number)
            row = self.cursor.fetchone()
            return True, row[0]
        except pyodbc.Error as e:
            print(e)
            return False, 0

    def updatePassword(self, login, password):
        cipher = Fernet(properties.cipher_key)
        encrypted_password = password.encode('utf8')
        encrypted_password = cipher.encrypt(encrypted_password)
        self.cursor.execute("UPDATE Пользователи SET Пароль='"+encrypted_password.decode("utf-8")+"' where Логин='"+login+"'")
        self.cnxn.commit()

    def updateContract(self, fid, salary, date):
        self.cursor.execute("UPDATE Контракты SET Зарплата="+ str(salary) +" where ID_футболиста="+ str(fid))
        self.cnxn.commit()
        self.cursor.execute("UPDATE Контракты SET Дата_окончания='" + date + "' where ID_футболиста=" + str(fid))
        self.cnxn.commit()

    def addCoach(self, uid, n, s, nat, d, w, t):
        name = n.rstrip()
        surname = s.lstrip()
        fio = (name + " " + surname).rstrip()
        if t is None:
            try:
                self.cursor.execute(
                    "INSERT INTO Тренеры_и_персонал(ФИО, Национальность, Дата_рождения, Должность, ID_пользователя) "
                    "VALUES ('" + fio + "', '" + nat + "', '" + d + "', '" + w + "', " + str(uid) + ")")
                self.cnxn.commit()
                return True
            except pyodbc.Error as e:
                print(e)
                return False
        else:
            self.cursor.execute("SELECT ID_команды from Команды where Команда='" + t + "'")
            row = self.cursor.fetchone()
            tid = row[0]
            try:
                self.cursor.execute(
                    "INSERT INTO Тренеры_и_персонал(ФИО, Национальность, Дата_рождения, Должность, ID_команды, ID_пользователя) "
                    "VALUES ('" + fio + "', '" + nat + "', '" + d + "', '" + w + "', " + str(
                        tid) + ", " + str(uid) + ")")
                self.cnxn.commit()
                return True
            except pyodbc.Error as e:
                print(e)
                return False

    def addManager(self, uid, n, s, nat, d):
        name = n.rstrip()
        surname = s.lstrip()
        fio = (name + " " + surname).rstrip()
        try:
            self.cursor.execute(
                "INSERT INTO Руководство(ФИО, Национальность, Дата_рождения, ID_пользователя) "
                "VALUES ('" + fio + "', '" + nat + "', '" + d + "', " + str(uid) + ")")
            self.cnxn.commit()

            row = self.cursor.execute("SELECT max(ID_владельца) from Руководство")
            row = self.cursor.fetchone()
            return True, row[0]
        except pyodbc.Error as e:
            print(e)
            return False, 0

    def changeManager(self, id, t):
        try:
            self.cursor.execute(
                "UPDATE Команды set ID_Владельца =" + str(id) + " where Команда ='" + t + "'")
            self.cnxn.commit()
            return True
        except pyodbc.Error as e:
            print(e)
            return False

