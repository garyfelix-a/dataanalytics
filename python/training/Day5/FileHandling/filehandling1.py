import os

# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# Content1 = file.readline()
# Content2 = file.readlines()
# file.close()

# file = open('file.txt', 'w')
# file.write("Hey Buddy!!!")
# file.write("Bye Buddy!!!")
# file.close()

# file = open('file.txt', 'a')
# file.write("Hey You!!!")
# file.close()


# if os.path.exists("file.txt"):
#     with open('file.txt', 'r') as file:
#         content = file.read()
#         print(content)

# else:
#     print("File does not exist!")

# file copy with another file.
try:
    with open('file.txt', 'r') as file:
        data = file.read()
    with open('file2.txt', 'w') as filewrite:
        filewrite.write(data)
    print("File copied successfully!")
    
except FileNotFoundError:
    print("Input or output operation failed!")
except IOError as e:
    print("I/O Exception: {e}")
except Exception as e:
    print("An unexpected exception")