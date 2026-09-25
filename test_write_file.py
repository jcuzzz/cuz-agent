from functions.write_file import write_file

print(write_file("calculator", "lorem.txt", "wait, this isn'y lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "lorem ipsum dolor sit amet"))
