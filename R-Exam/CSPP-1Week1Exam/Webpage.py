def backgroundColors(data):
    list_color = []
    colors = data.split(";")
    tag = "background-color"
    endtag = ";"
    result = []
    for item in colors:
        if "background-color" in item:
            list_color.append(item)
            index = item.index(tag)
            item = val[index + len(tag) :]
            result.append(item)
    # print(list_color[1])
    # for val in list_color:
    #     if "background-color" in val:
    #         index = val.index(tag)
    #         val = val[index + len(tag) :]
    #         result.append(val)
            # end = val.index(endtag)
            # print(val[:end])
    # print(result)
    # tag1 = ":"
    # final = []
    # for color in result:
    #     if ":" in color:
    #         index = color.index(tag1)
    #         color = color[index + len(tag1) :]
    #         # print(color)
    #         final.append(color)
    set_color = set(result)
    sort = sorted(set_color)
    # print(sort)
    for i in sort:
        print(i)


def image(data):
    img = data.split("<img")
    # print(img)
    img = img[1:]
    tag = "src=\""
    endtag = "\""
    # string = ""
    string = []
    count = 0
    for item in img:
        if "src=\"" in item:
            # string += item
            index = item.index(tag)
            item = item[index+len(tag):]
            end = item.index(endtag)
            count += 1
            # string += item
            # string.append(item)
            print(item[:end])
    #         string.append(item)
    # print(string)
    print(count)
    # image_res = string.split(" data")

    # for res in image_res:
    # #     if "src=\"":
    # #         pass
    #   print(res)
    # <img src=
def getList(data):
    pass
    # get_List = list(data)
    # # print(get_List)
    # string = []
    # for i in range(len(get_List)):
    #     if get_List[i] == ">":
    #         string.append(get_List[i + 1])          
    #         if get_List[i] == "<":
    #             break
    # print(string)
def main():
    data = open("webpage5.html", errors = 'ignore').read()
    # print(data)
    choice = input()
    if choice == "image":
        image(data)
    elif choice == "background":
        backgroundColors(data)
    elif choice == "list":
        getList(data)

if __name__ == '__main__':
    main()