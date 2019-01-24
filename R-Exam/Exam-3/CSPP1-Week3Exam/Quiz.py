def check_response(data):
    # print(data)
    total_score = 0
    scored = {}
    global flag
    flag = 0
    full_Score = {}
    for item in data:
        # print(type(int(item[4])))
        try:
            if int(item[4]) == type(int):
                print("OKOK")
        except ValueError:
            print("Invalid Points")
            flag = 1
            break
        # print("Hi")
        # if item[4] == "":
        #     pass
        if item[0] not in scored:
                full_Score[item[0]] = int(item[4])
                # print(full_Score)
                scored[item[0]] = 0
                # print(scored[item[0]],"-----------")
        else:
            full_Score[item[0]] += int(item[4])
        if item[2] == item[3]:
            scored[item[0]] += int(item[4])
        else:
            scored[item[0]] -= int(item[4])

    # scored = sorted(scored)
    # total_score = sorted(total_score)
    # print(scored,"Scored")
    # print(full_Score)
    for got in sorted(scored):
        for total in sorted(full_Score):
            if flag == 0:
                if got == total:
                    final = int((scored[got]/full_Score[total]) * 100)
                    if final <= 0:
                        final = 0.0
                        print(got + ": " + str(final) + "%")
                    else:
                        print(got + ": " + str(float(final)) + "%")


    #     if int(value[0]) in dict1:
    #         # if value[2] == value[3]:
    #         dict1[int(value[0])] += int(value[4])
    #         # else:
    #         #     dict1[int(value[0])] -= int(value[4])
    #     else:
    #         dict1[int(value[0])] = int(value[4])
    # print(dict1)
    # for item in data:
    #     for key,val in dict1.items():
    #         if int(item[0]) == key:
    #             print(key)


def main():
    number = int(input())
    global questions
    questions = []
    for i in range(number):
        questions.append(input().split("|"))
    # print(questions)
    check_response(questions)

if __name__ == '__main__':
    main()