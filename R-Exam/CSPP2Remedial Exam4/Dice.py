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
    for key, val in result.items():
        ans = list(key)
        ans = list(val)


if __name__ == '__main__':
    main()
