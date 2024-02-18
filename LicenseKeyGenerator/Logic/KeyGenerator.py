# This is a sample Python script.
#|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
# 3,4 - Store Product Code [A1]
# 14,15 - Store Month of Expiry date [08]
# 5,6 - Store Day of Expiry date [20]
# 18,19 - Store Year of Expiry date [96]
# 11,12,13 - Store Hash of all chars except 11,12,13 positions. []
# 
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import string
from datetime import datetime

class KeyGenrator():
    value = ""

    def GetRandomStr(self):
        Key = [random.choice(string.ascii_uppercase+string.digits) for _ in range(20)]
        return Key

    def AddProductCode(self,product,key):
        if product == "Software1":
            key[3:5] = "A1"
        elif product == "Software2":
            key[3:5] = "B2"
        elif product == "Software3":
            key[3:5] = "C1"
        elif product == "Software4":
            key[3:5] = "D3"

    def AddExpiryDate(self,key, lic_date=datetime.now()):
        date_list = lic_date.strftime("%m:%d:%y").split(":")
        key[14:16] = list(date_list[0])
        key[5:7] = list(date_list[1])
        key[18:20] = list(date_list[2])

    def AddHash(self,key):
        hash = self.GetHash(key)
        key[11:14] = hash

    def GetHash(self,key):
        combined_hash = sum([ord(val) for i,val in enumerate(key) if (i!=11 and i!=12 and i!=13)])
        return list(hex(int(combined_hash)))[2:]

    def CheckHash(self,key):
        hash = self.GetHash(key)
        if hash == key[11:14]:
            return True
        return False

    def CheckProductCode(self,key):
        if key[3:5] == "A1":
            return True
        elif key[3:5] == "B2":
            return True
        elif key[3:5] == "C1":
            return True
        elif key[3:5] == "D3":
            return True
        return False

    def GetExpiryDays(self,key):
        current_date = datetime.now().date()
        day = int(''.join(key[5:7]))
        month = int(int(''.join(key[14:16])))
        year = 2000 + int(int(''.join(key[18:20])))
        expiry = datetime(year,month,day).date()
        return (expiry - current_date).days

    def GenerateKey(self,software_name,expiry_date):
        key = self.GetRandomStr()
        self.AddProductCode(software_name, key)
        self.AddExpiryDate(key, expiry_date)
        self.AddHash(key)
        return ''.join(key)

    def ValidateKey(self,key):
        if type(key) == str:
            key = list(key)

        if self.CheckHash(key):
            days = self.GetExpiryDays(key)
            if days < 0:
                raise Exception("License key is expired. Please contact AA Pvt. Ltd for renewal of the key.")
        else:
            raise Exception("Provided key is not valid.")
        return True

    def DaysConversionIntoMonthsAndYears(self,days):
        years = days//365
        months = (days - years * 365)//30
        days = (days - years * 365 - months * 30)
        return (years, months, days)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = "RZ4C108U12342602RU24"
    KeyGenrator().ValidateKey(key)
    """
    for _ in range(100):
        software_code = "Software2"
        if _ % 2 == 0:
            software_code = "Software1"
        elif _ % 3 == 0:
            software_code = "Software3"
        mon = random.randint(1,12)
        end = 30
        if mon == 2:
            end=29
        day = random.randint(1,end)
        print(mon,',',day)
        obj = KeyGenrator()
        key = obj.GenerateKey(software_code,datetime(2024,mon,day))
        print(''.join(key))
        print(obj.ValidateKey(key))
        
        if d > 0:
            print("Your software will expire in: ",d)
        elif d == 0:
            print("Your software will expire today.")
        print()
        """

