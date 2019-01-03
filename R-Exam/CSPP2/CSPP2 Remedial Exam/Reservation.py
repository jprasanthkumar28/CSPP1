def main():
    room_data = {}
    count = 5
    number = int(input())
    for j in range(number):
        choice = input().split( )
        if choice[0] == "reserve":
            if len(room_data) >= count:
                print("All Rooms are reserved")
                # print("i value")
                # break
            elif room_data == {}:
                room_data[1] = choice[1]
                print(choice[1], 1)
            else:
                for i in range(1,count+1):
                    if i not in room_data.keys():
                        # print(i)
                        room_data[i] = choice[1]
                        print(choice[1], i)
                        break
        elif choice[0] == "reserveN":
            # print(len(room_data), "dict_len")
            if len(room_data) >= count:
                # print("length------------")
                print("All Rooms are reserved")
            elif int(choice[2]) in room_data.keys():
                print("Room is already reserved")
            else:
                room_data[int(choice[2])] = choice[1]
                print(choice[1], choice[2])

        elif choice[0] == "print":
            for key, value in sorted(room_data.items()):
                print(value, str(key))
        
        elif choice[0] == "build":
            # print(count, "  before count")
            count +=  int(choice[1])
            # print(count, "  count")
            print("Added", choice[1], "more rooms")

        elif choice[0] == "cancel":
            dict1 = room_data.copy()
            for key, value in dict1.items():
                if value == choice[1]:
                    room_data.pop(key, value)
            print(choice[1],"now has no reservations.")

if __name__ == '__main__':
    main()