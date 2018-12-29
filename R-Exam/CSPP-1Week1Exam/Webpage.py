

def backgroundColors(data):
    list_color = []
    colors = data.split(";")
    for item in colors:
        if "background-color" in item:
            list_color.append(item)
    # print(list_color[1])
    tag = "background-color"
    endtag = ";"
    result = []
    for val in list_color:
        if "background-color" in val:
            index = val.index(tag)
            val = val[index + len(tag) :]
            result.append(val)
            # end = val.index(endtag)
            # print(val[:end])
    # print(result)
    tag1 = ":"
    final = []
    for color in result:
        if ":" in color:
            index = color.index(tag1)
            color = color[index + len(tag1) :]
            # print(color)
            final.append(color)
    set_color = set(final)
    sort = sorted(set_color)
    for i in sort:
      print(i)

def image(data):
    img = data.split("><")
    # print(img)
    tag = "img src="
    endtag = " data-"
    # string = ""
    string = []
    count = 0
    for item in img:
        if "img src=\"" in item and " data-" in item:
            # string += item
            index = item.index(tag)
            item = item[index+len(tag):]
            end = item.index(endtag)
            count += 1
            # string += item
            # string.append(item)
            print(item[:end])
            # string.append(item[:end])
    print(count)
    # print(string)
    # image_res = string.split(" data")

    # for res in image_res:
    # #     if "src=\"":
    # #         pass
    #   print(res)
    # <img src=
def getList(data):
    pass

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