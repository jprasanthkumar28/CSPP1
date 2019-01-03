def main():
    room_data = {}
    count = 6
    number = int(input())
    for i in range(number):
        choice = input().split()
        if choice[0] == "reserve":
            if room_data == {}:
                room_data[1] = choice[1]
                print(choice[1], 1)
            else:
                for i in range(1,count):
                    if i not in room_data.keys():
                        if i >= count:
                            print("All room are reserved")
                            break
                        room_data[i] = choice[1]
                        print(choice[1], i)
                        break
        if choice[0] == "reserveN":
            if len(room_data) >= count:
                print("All room are reserved")
            elif int(choice[2]) in room_data.keys():
                print("Room is already reserved")
            else:
                room_data[int(choice[2])] = choice[1]
                print(choice[1], choice[2])


        if choice[0] == "print":
            for key, value in sorted(room_data.items()):
                print(value + " " + str(key))
    # for key, value in room_data.items():
    #     print(value + " " + str(key))
    # # print(room_data)
    # for key, value in sorted(room_data.items()):
    #     print(value + " " + str(key))

if __name__ == '__main__':
    main()