all_pass = []

for password in map(str, range(347312, 805915)):
    i = 1
    increasing = True
    hasDubs = False
    while i < len(password):
        if password[i-1] > password[i]:
            increasing = False
        if password[i-1] == password[i]:
            if password.count(password[i]) == 2:
                hasDubs = hasDubs or True

        i = i+1

    if increasing and hasDubs:
        all_pass.append(password)

print(len(all_pass))
