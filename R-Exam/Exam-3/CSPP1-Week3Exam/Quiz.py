def check_response(data):
    # print(data)
    total_score = 0
    scored = {}
    global flag
    flag = 0
    full_Score = {}
    for text in data:
        # print(type(int(text[4])))
        try:
            if int(text[4]) == type(int):
                print("OKOK")
        except ValueError:
            print("Invalid")
            flag = 1
            break

            
            # print("Hi")
        # if text[4] == "":
        #     pass
        if text[0] not in scored:
                full_Score[text[0]] = int(text[4])
                # print(full_Score)
                scored[text[0]] = 0
                # print(scored[text[0]],"-----------")
        else:
            full_Score[text[0]] += int(text[4])
        if text[2] == text[3]:
            scored[text[0]] += int(text[4])
        else:
            scored[text[0]] -= int(text[4])

    # scored = sorted(scored)
    # total_score = sorted(total_score)
    # print(scored)
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