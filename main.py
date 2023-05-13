login = str(input("Введите свой логин:"))
password = str(input("Введите свой пароль:"))
sub = "login: "
subs = "pass: "
with open('data.txt', 'w') as f:
    f.write(sub + login)
    f.write("\n")
    f.write(subs + password)