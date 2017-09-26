class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        if (self.year == other.year) & (self.month == other.month) & (self.day == other.day):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.month:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class Etudiant(object):

    def __init__(self, firstName, lastName, birthday):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.email = self.adresselec()
        self.age = self.age()

    def adresselec(self):
        str = self.firstName.lower() + "." + self.lastName.lower() + "@etu.univ-tours.fr"
        return str

    def age(self):
        age = 2017 - int(self.birthday.year)
        return age



if __name__=='__main__':
    import csv
    list=[]
    csv_reader = csv.reader(open('fichetu.csv'))
    for row in csv_reader:
        tmp = "".join(row)
        lastName,firstName,birth = tmp.split(";")
        day, month, year = birth.split("/")
        birthday = Date(year,month,day)
        etu = Etudiant(firstName, lastName, birthday)
        list.append(etu)
    for stu in list:
        info = stu.firstName + " " + stu.lastName + " " + stu.birthday.day + "/" + stu.birthday.month + "/" + stu.birthday.year + " " + stu.email + " " + str(stu.age)
        print(info)
