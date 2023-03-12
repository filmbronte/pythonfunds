directory = input().split("\\")
last = directory[-1]

file_name, file_extension = last.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


