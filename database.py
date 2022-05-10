import sqlite3


class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def add_speciality(self, Id, Name, Number, NameOfUni, Math, Physics, Ukrainian, Engilish, German, Biology,
                       Chemistry, Law,
                       History, Geography, gpa):
        self.cursor.execute(
            "INSERT OR IGNORE INTO Speciality (id, name, number, nameofuni, math, physics, ukrainian, engilish, german, biology, chemistry, law, history, geography, gpa) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (Id, Name, Number, NameOfUni, Math, Physics, Ukrainian, Engilish, German, Biology, Chemistry, Law,
             History, Geography, gpa))
        self.conn.commit()

    def delete_speciality(self, ID):
        self.cursor.execute("DELETE FROM Speciality where Id=?", (ID,))
        self.conn.commit()

    def get_speciality(self, ID, field):
        self.cursor.execute(f"SELECT {field} from Speciality where Id=?", (ID,))
        records = self.cursor.fetchall()
        return records

    def get_name_speciality(self, ID,):
        self.cursor.execute(f"SELECT Name, Number, NameOfUni from Speciality where Id=?", (ID,))
        records = self.cursor.fetchall()
        return records

    def get_length(self):
        self.cursor.execute("SELECT * from Speciality")
        records = self.cursor.fetchall()
        return len(records)

