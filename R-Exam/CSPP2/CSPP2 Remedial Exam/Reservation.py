def main():
    room_data = {}
    number = int(input())
    for i in range(number):
        choice = input().split()
        if choice[0] == "reserve":
            count = 5
            if room_data == {}:
                room_data[1] = data[1]
            else:
                for i in range(1,count+1):
                    if i not in room_data.keys():
                        room_data[i] = data[1]
                        # print(data[1], i)
                        break
        elif choice[0] == "reserveN":
            room_data[int(choice[2])] = choice[1]
    for key, value in room_data.items():
        print(value + " " + str(key))
    # print(room_data)
    for key, value in sorted(room_data.items()):
        print(value + " " + str(key))

if __name__ == '__main__':
    main()