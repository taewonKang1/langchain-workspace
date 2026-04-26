f = open("example_basic.txt", "w", encoding="utf8")
f.write("첫 줄\n")
f.write("둘째 줄\n")
f.write("셋째 줄\n")
f.close()

# f = open("example_basic.txt", "r", encoding="utf8")
# content = f.read()

# content = f.readline()
# print(content, end="")
# content = f.readline()
# print(content, end="")
# content = f.readline()
# print(content, end="")

# content_list = f.readlines()
# print(content_list)

# f.close()