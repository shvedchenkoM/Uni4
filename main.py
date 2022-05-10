import database

db = database.Database("occupation.db")


def if_obligatory(value: float):
    if value > 200.0:
        return (0, value - 1000)  # non obligatory
    else:
        if value == 0:
            return (-1, 0)  # not needed
        else:
            return (1, value)  # obligatory

def main():

    print("Hello blablabla")
    count_test = int(input("Give me now count of test your passed: "))
    print("Good now say me the name of speciality and mark that you get in format (name mark): ")
    specialities = dict()
    GPA = int(input("Give me your GPA: "))
    for i in range(0, count_test):
        name, val = input().split(" ")
        try:
            val = float(val)
        except:
            print("This  is not number:(")
            exit(-1)

        specialities[name] = val # pupla

    cources = list() # answer
    # print("111")
    # print(cources)
    for i in range(1, db.get_length()):
        # print(db.get_name_speciality(i))
        karma = 0
        non_obl = 0
        for specialitie in specialities.keys():
            mark = "3"
            try:
                mark = db.get_speciality(i, specialitie)
            except:
               print("we don't have such a speciality")
               exit(-1)
            if len(mark) == 0:
                continue

            mark = str(mark[0])
            mark = mark[1:-2]
            mark = float(mark)
            # print(mark)
            # if mark == 1130.0:
            #     print(111)
            (status, value) = if_obligatory(mark)
            if status == 1 and mark <= specialities[specialitie]: #Bug was here
                karma += 1
            if status == 0 and non_obl == 0 and mark >= value:
                karma += 1
                non_obl = 1

        try:
            gpa_m = db.get_speciality(i, "gpa")
        except:
            print("ggwp")
            exit(-1)
        if len(gpa_m) == 0:
            continue

        min_gpa = float(str(gpa_m[0])[1:-2])
        # print(min_gpa, GPA, karma)

        if karma >= 3 and GPA >= min_gpa:
            cources.append(db.get_name_speciality(i)[0])
            karma = 0
            non_obl = 0

    if len(cources) == 0:
        print("sorry, we don't have a speciality that fits you")
    else:
        print("You can choose one of the list:")
        for cource in cources:
            print("name of speciality: ", cource[0],
                  "; number of speciality: ", cource[1], "; name of the University: ", cource[2])
# db.delete_row(2)


print(db.get_name_speciality(11))
print(db.get_length())

main()
