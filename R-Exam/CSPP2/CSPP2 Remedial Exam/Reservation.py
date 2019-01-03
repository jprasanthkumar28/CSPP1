def reserve(data, room_Num):
    count = 5
    if room_Num == {}:
        room_Num[1] = data[1]
    else:
        for i in range(1,count+1):
            if i not in room_Num.keys():
                room_Num[i] = data[1]
                # print(data[1], i)
                break
            # print(i)
        # room_Num = 
        # sorted
    # return room_Num
    # return room_Num.keys()
    # for key in sorted(room_Num):
    #         print(room_Num[key], key)

def main():
    # global room_Num
    room_data = {}
    number = int(input())
    # print(number)
    for i in range(number):
        choice = input().split()
        if choice[0] == "reserve":
            # print("reserve")
            reserve(choice,room_data)
        elif choice[0] == "reserveN":
            room_data[int(choice[2])] = choice[1]
    for key, value in room_data.items():
        print(value + " " + str(key))
    # print(room_data)
    for key, value in sorted(room_data.items()):
        print(value + " " + str(key))

if __name__ == '__main__':
    main()