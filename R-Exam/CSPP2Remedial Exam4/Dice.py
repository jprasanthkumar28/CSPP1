def main():
    p_count = int(input())
    result = {}
    while True:
        try:
            # data = input()
            data = input().split(" ")
            if len(data) > 1:
                # print(data)
                if data[0] not in result and int(data[2] != 1):
                    result[data[0]] = int(data[2])

                elif data[2] == 1:
                    result[data[0]] = 0

                else:
                    result[data[0]] += int(data[2])
                # result[data] += int(data[2])
        except EOFError:
            break
    # print(result)
    ans = []
    maxi = 0

    for key, val in result.items():
        # print(val)
        ans.append(val)
        maxi = max(ans)
        if maxi == val:
            answer = key

    print(answer)
    # print(maxi)
    # print(ans)

if __name__ == '__main__':
    main()
