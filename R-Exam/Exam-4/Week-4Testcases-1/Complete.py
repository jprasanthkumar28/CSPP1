# global temp
# temp = ''
# global temp1
# temp1 = ''
# global temp2
# temp2 = ''
# global temp3
# temp3 = ''
# global temp4
# temp4 = ''

def FoodLog(food, string):
    lst = string.split(",")
    if lst[1] not in storage_Food:
        storage_Food[lst[1]] = {lst[2]:lst[0]}
        # print(storage_Food)
    else:
        storage_Food[lst[1]].update({lst[2]:lst[0]})
#         # print(storage_Food)
    return storage_Food
def Waterlog(water, string1):
    lst = string1.split(",")
    if lst[1] not in storage_Water:
        storage_Water[lst[1]] = {lst[2]:lst[0]}
    else:
        storage_Water[lst[1]].update({lst[2]:lst[0]})
    return storage_Water
def PhysicalLog(physical, string2):
    # print("storage_Physical")
    lst = string2.split(",")
    if lst[1] not in storage_Physical:
        storage_Physical[lst[1]] = {lst[2]:lst[0]}
    else:
        storLogical[lst[1]].update({lst[2]:lst[0]})
    return storage_Physical
def weightLog(weight, string3):
    lst = string3.split(",")
    if lst[1] not in storage_Weight:
        storage_Weight[lst[1]] = {lst[2]:lst[0]} 
    else:
        storage_Weight[lst[1]].update({lst[2]:lst[0]})
    return storage_Weight
def SleepLog(sleep, string4):
    lst = string4.split(",")
    if lst[1] not in storage_Sleep:
        storage_Sleep[lst[1]] = {lst[2]:lst[0]}
    else:
        storage_Sleep[lst[1]].update({lst[2]:lst[0]})
    return storage_Sleep


def Summary():
    print("Summary:")
    for k in sorted(storage_Food, reverse = True):
        print(k + ":")
        print(temp+":", end = "\n")
        for i  in storage_Food[k]:
            print("- "+ i + ": " + storage_Food[k][i])

    for k in sorted(storage_Water, reverse = True):
        print(k + ":")
        print(temp1+":", end = "\n")
        for i  in storage_Water[k]:
            print("- "+ i + ": " + storage_Water[k][i])
   
    for k in sorted(storage_Physical, reverse = True):
        print(k + ":")
        print(temp2+":", end = "\n")
        for i  in storage_Physical[k]:
            print("- "+ i + ": " + storage_Physical[k][i])
   
    for k in sorted(storage_Weight, reverse = True):
        # print(k+":", end = "\n")
        print(k + ":")
        print(temp3+":", end = "\n")
        for i  in storage_Weight[k]:
            print("- "+ i + ": " + storage_Weight[k][i])
   
    for k in sorted(storage_Sleep, reverse = True):
        print(k + ":")
        print(temp4+":", end = "\n")
        for i  in storage_Sleep[k]:
            print("- "+ i + ": " + storage_Sleep[k][i])
def main():
    global storage_Food
    global storage_Water
    global storage_Physical
    global storage_Weight
    global storage_Sleep
    global temp
    global temp1
    global temp2
    global temp3
    global temp4
    storage_Food = {}
    storage_Water = {}
    storage_Physical = {}
    storage_Weight = {}
    storage_Sleep = {}
    n = int(input())
    for i in range(n):
        string = input();
        string1 = string.split(" ")
        if len(string1) > 1:
            if string1[0] == "Food":
                temp = string1[0]
                storage_Food = FoodLog(string1[0], string1[1])
                # print(storage_Food)
            if string1[0] == "Water":
                temp1 = string1[0]
                # print(temp1)
                storage_Water = Waterlog(string1[0], string1[1])
            if string1[0] == "PhysicalActivity":
                temp2 = string1[0]
                # print(temp2)
                storage_Physical = PhysicalLog(string1[0], string1[1])
            if string1[0] == "Weight":
                temp3 = string1[0]
                storage_Weight = weightLog(string1[0], string1[1])
            if string1[0] == "Sleep":
                temp4 = string1[0]
                storage_Sleep = SleepLog(string1[0], string1[1])
        else:
            if string1[0] == "Foodlog":
                print(temp+":")
                for k in sorted(storage_Food):
                    print(k+":")
                    for i in storage_Food[k]:
                        print("- "+ i + ": " + storage_Food[k][i])
            if string1[0] == "Waterlog":
                print(temp1+":")
                for k in sorted(storage_Water):
                    print(k+":")
                    for i in storage_Water[k]:
                        print("- "+ i + ": " + storage_Water[k][i])
            if string1[0] == "PhysicalActivitylog":
                print(temp2+":")
                for k in sorted(storage_Physical):
                    print(k+":")
                    for i in storage_Physical[k]:
                        print("- "+ i + ": " + storage_Physical[k][i])
            if string1[0] == "Weightlog":
                print(temp3+":")
                for k in sorted(storage_Weight):
                    print(k+":")
                    for i in storage_Weight[k]:
                        print("- "+ i + ": " + storage_Weight[k][i])
            if string1[0] == "Sleeplog":
                print(temp4+":")
                for k in sorted(storage_Sleep):
                    print(k+":")
                    for i in storage_Sleep[k]:
                        print("- "+ i + ": " + storage_Sleep[k][i])
            if string1[0] == "Summary":
                Summary()
main()