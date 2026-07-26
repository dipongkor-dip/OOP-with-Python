# .csv comma separated values
# .txt text file

# write file data
with open("message.txt", "w") as file:
    content = "Hello, this is a sample message.\nThis is the second line of the message. This data is handled by file.py file in python."
    file.write(content)

# append
with open("message.txt", "a") as file:
    content = "finally, this is the third line of the message. This data is handled by file.py file in python."
    file.write(content)

# read file data
with open("message.txt", "r") as file:
    content = file.read()
    print(content)

