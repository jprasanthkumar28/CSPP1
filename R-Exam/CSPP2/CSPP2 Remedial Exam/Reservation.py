def main():
    room_data = {}
    count = 6
    number = int(input())
    j = 0
    # for j in range(number+1):
    while j < number:
        choice = input().split( )
        if choice[0] == "reserve":
            if room_data == {}:
                room_data[1] = choice[1]
                print(choice[1], 1)
            else:
                for i in range(1,count):
                    if i not in room_data.keys():
                        # print(i)
                        if i >= count:
                            print("All Rooms are reserved")
                            break
                        room_data[i] = choice[1]
                        print(choice[1], i)
                        break
        if choice[0] == "reserveN":
            # print(len(room_data), "dict_len")
            if len(room_data) >= count:
                print("All Rooms are reserved")
            elif int(choice[2]) in room_data.keys():
                print("Room is already reserved")
            else:
                room_data[int(choice[2])] = choice[1]
                print(choice[1], choice[2])


        if choice[0] == "print":
            for key, value in sorted(room_data.items()):
                print(value, str(key))
        if choice[0] == "build":
            count +=  int(choice[1])
            print("Added", choice[1], "more rooms")
        j += 1

if __name__ == '__main__':
    main()