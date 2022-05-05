import pyfiglet as w
print(w.figlet_format("H A C K"))
#username
usernames = str(input("Username: "))
created = open(usernames, "x")
size = 42949672960
created.write("\0" * size)
