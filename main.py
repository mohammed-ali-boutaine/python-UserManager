import datetime, os
import pickle
import ast
from prettytable import PrettyTable  # ! install library :  pip install PrettyTable


class info:
    def __init__(self, full_name="", cin="", age=0, fvrt_color='', born_city='', fvrt_city='', fvrt_habits=[],fvrt_sport=[]):
        self.full_name = full_name
        self.cin = cin
        self.age = age
        self.fvr_color = fvrt_color
        self.born_city = born_city
        self.fvrt_city = fvrt_city
        self.fvrt_habits = fvrt_habits
        self.fvrt_sport = fvrt_sport

    def saisir(self):

        while True:
            try:
                self.full_name = input("Etrez votre prenom et nom:")
                if os.path.isfile("text container/" + self.full_name + ".txt"):
                    print(f"The file {self.full_name} already exists.")
                    break
                else:
                    with open("text container/" + self.full_name + ".txt", "w") as f:

                        pass

                self.cin = input("Etrez votre CIN: ")
                self.age = int(input("Etrez votre age: "))

                self.born_city = str(input("cit de naissance: "))
                self.fvrt_city = input("city:")
                self.fvrt_habits = input("HAbits:")
                self.fvrt_sport = input("sport: ")
                self.datedecreation = str(datetime.datetime.now())
                f = open("text container/" + self.full_name + ".txt", "a")  # open file to read
                datalist = f"""[
                               ["full name", "{self.full_name}"],
                               ["cin", "{self.cin}"],
                               ["age", {self.age}],
                               ["born city", "{self.born_city}"],
                               ["favorite city", "{self.fvrt_city}"],
                               ["favorite habits", "{self.fvrt_habits}"],
                               ["favorite sport", "{self.fvrt_sport}"],
                               ["creation date", "{self.datedecreation}"]
                           ]"""
                f.write(datalist)
                f.close()
                with open("text container/" + self.full_name + ".txt", "r") as f:
                    data = f.read()

                my_list = ast.literal_eval(data)

                table = PrettyTable(["Attribute", "Value"])
                for row in my_list:
                    table.add_row(row)

                print(table)
                print("secces")
                break
            except Exception as e:
                print("error!!  ==> ", e)
                print()
                print("try again ")
                if os.path.isfile(self.full_name + ".txt"):
                    os.remove(self.full_name + ".txt")


# -----------------------------------------------------------------------------------------------------------------------
answer = ''


def menu():  # fonctin recursive  with try and except
    try:
        print('-------------------------------------------Menu-------------------------------------------------------------------------')
        global answer
        print('En trez votre choix: 1-Ajouter, 2-Afficher les Fichies, 3-Supprimer, 4-Modifier, 5-Rechercher et Afichier(full name), 0-Quitter : ')
        print("------------------------------------------------------------------------------------------------------------------------")
        answer = int(input("CHOIX: "))

    except:
        print("error")
        print("try again")
        menu()


menu()

while answer != 0:

    if answer < 0 or answer > 6:
        print("error")
        print("try again")
        menu()

    else:
        if answer == 1:
            test = info()
            test.saisir()
            menu()

        elif answer == 2:
            folder = "text container"
            print("Names :")
            for root, dirs, files in os.walk(folder):
                for name in files:
                    print(os.path.basename(name))
            for name in dirs:
                print(os.path.basename(name))
            pass
            menu()



        elif answer == 3:
            delet = input("enter first name or fullname : ")
            folder = "text container"
            for filename in os.listdir(folder):
                # Check if the file is a text file and starts with the value
                if filename.endswith(".txt") and filename.startswith(delet):
                    # Delete the file
                    os.remove(os.path.join(folder, filename))
                    print(f"Deleted file: {filename}")

            menu()

        elif answer == 4:

            change=input("enter the name of file you wanna change: ")
            os.remove("text container/"+change+".txt")
            test = info()
            test.saisir()
            menu()

        elif answer == 5:
            
            filename = input("Enter a filename: ")

            if os.path.isfile("text container/" + filename + ".txt"):
                with open("text container/" + filename + ".txt", "r") as f:
                    data = f.read()
                    my_list = ast.literal_eval(data)

                    table = PrettyTable(["Attribute", "Value"])
                    for row in my_list:
                        table.add_row(row)

                    print(table)

            else:
                print("file not fond")
            menu()



print("Fine de programme !!")