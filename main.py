
import csv
import time
from datetime import date

class Pizza:
    def get_description(self):
        """Description of pizza getter"""
        pass

    def get_cost(self):
        """Cost of pizza getter"""
        pass

class Classic(Pizza):
    def get_description(self):
     return "Classic Pizza"


    def get_cost(self):
            return 5

class Margarita(Pizza):
    def get_description(self):
        return "Margarita Pizza"

    def get_cost(self):
        return 6


class Turkish (Pizza):
    def get_description(self):
       return "Turkish Pizza"

    def get_cost(self):
       return 7

class Plain(Pizza):
    def get_description(self):
       return "Sade Pizza"

    def get_cost(self):
       return 8


class Decorator:
    def get_description(self):
        "Description of decorator getter"
        pass

    def get_cost(self):
        "Description of cost getter"
        pass

class Olive(Decorator):
    def get_description(self):
         return "This is awesome with olive"

    def get_cost(self):
         return 5

class Mushroom(Decorator):
    def get_description(self):
       return "This is awesome with mushroom"

    def get_cost(self):
       return 6

class GoatCheese(Decorator):
    def get_description(self):
        return "This is awesome with goat cheese"

    def get_cost(self):
        return 5


class Meat(Decorator):
    def get_description(self):
       return "This is awesome with meat"

    def get_cost(self):
       return 5

class Onion(Decorator):
    def get_description(self):
      return "This is awesome with onion"

    def get_cost(self):
      return 5


class Sweetcorn(Decorator):
    def get_description(self):
        return "This is awesome with sweetcorn"

    def get_cost(self):
        return 5


def calculate_pizza_price(lst):
    """Total price calculator

    Keyword arguments:
    lst -- Selection list
    """
    total = 0
    for item in lst:
        total += item.get_cost()
    return total


def create_selection_description(lst):
    """Description creator

    Keyword arguments:
    lst -- Selection list
    """
    desc = str()
    for item in lst:
        desc += (item.get_description() + "-")
    return desc



def main():
    t = time.localtime()
    today = date.today()
    f=open("menu.txt","r")
    database_f=open('Orders_Database.csv',mode='w')
    database_f_writer=csv.writer(database_f,delimiter=',')
    selectionList = []
    database_f_writer.writerow(["Name", "IDNumber","CardInfo", "CardPW", "OrderTime", "OrderDescription", "Price"])
    
    while 1:
        print(f.read())
        base = int(input("Pizza Tabani Seçin(Cikmak icin -1): "))
        if base == -1:
            exit()
        while base < 1 or base > 5:
            print("Hatali secim yaptiniz.")
            base = int(input("Pizza Tabani Seçin: "))

        if base == 1:
            selectionList.append(Classic())
        elif base == 2:
            selectionList.append(Margarita())
        elif base == 3:
            selectionList.append(Turkish())
        elif base == 4:
            selectionList.append(Plain())

        sauce = int(input("Lütfen dilediginiz kadar sos seciniz. (-1 girildiginde durur): "))
        while sauce != -1:
            if sauce == 11:
                selectionList.append(Olive())
            elif sauce == 12:
                selectionList.append(Mushroom())
            elif sauce == 13:
                selectionList.append(GoatCheese())
            elif sauce == 14:
                selectionList.append(Meat())
            elif sauce == 15:
                selectionList.append(Onion())
            elif sauce == 15:
                selectionList.append(Sweetcorn())
            else:
                print("Yanlis secim yaptiniz.")
            sauce = int(input("Lütfen dilediginiz kadar sos seciniz. (-1 girildiginde durur): "))

        price = calculate_pizza_price(selectionList)
        desc = create_selection_description(selectionList)
        name = input("Isminiz: ")
        id_number = input("TC Kimlik: ")
        credit_card_number = input("Kredi Karti Numarasi: ")
        credit_card_password = input("Kredi Karti Şifresi: ")
        current_time = today.strftime("%d_%m_%Y_") + time.strftime("%H-%M-%S", t)
        database_f_writer.writerow([str(name), str(id_number), str(credit_card_number), str(credit_card_password), str(current_time), str(desc), str(price)])
        print("Siparisiinz olusturuldu :)")



if __name__ == "__main__":
    main()
