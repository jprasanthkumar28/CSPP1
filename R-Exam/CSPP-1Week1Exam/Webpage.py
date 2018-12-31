def backgroundColors(data):
    list_color = []
    colors = data.split(";")
    tag = "background-color"
    endtag = ";"
    result = []
    tag1 = ":"
    for item in colors:
        if "background-color" in item:
            # list_color.append(item)
            index = item.index(tag)
            item = item[index + len(tag) :]
            end = item.index(tag1)
            result.append(item[end:])
    # print(list_color[1])
    sort = set(result)
    # sort = sorted(set_color)
    count = 0
    final = []
    for i in sort:
        if "!" not in i:
            i = i[1:].replace(" ","")
            final.append(i)
            count += 1
            # if "{" in i:
            #     i = i[:7]
            #     final.append(i)            
            #     count += 1
    # prashu = []
    for p in final:
        if "}" in p:
            index = p.index("}")
            # print(index)
            p = p[:index]
            final.append(p)
    final1 = sorted(final)
    # print(final1)
    for x in final1:
        if "}" not in x:
            print(x)
    print(count)

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
            string.append(item)
    # print(string)
    print(count)
def getList(data):
    list1 = data.split("</li>")
    tag = "<li"
    mid = ">"
    endtag = "<"
    string = []
    count = 0
    for item in list1:
        if "<li>" in item and "<li" in item:
            # string += item
            index = item.index(tag)
            mid_index = index + item.index(mid)
            # print(mid_index)
            # end = item.index(endtag)
            item = item[index+len(tag):]
            # count += 1
            # string += item
            # print(item)
            string.append(item)
            # string.append(item)
    text_count = 0
    for x in string:
        if ">" in x:
            index1 = x.index(">")
            x = x[index1+len(">"):]
            index2 = x.index("<")
            x = x[:index2+len("<") - 1]
            text_count += 1
            print(x)
    print(text_count)

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