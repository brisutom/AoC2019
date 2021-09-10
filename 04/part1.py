all_pass = []

for password in range(347312, 805915):
    i = 1
    increasing = True
    hasDubs = False
    while i < len(str(password)):
        if int(str(password)[i-1]) > int(str(password)[i]):
            increasing = False
        if int(str(password)[i-1]) == int(str(password)[i]):
            hasDubs = True

        i = i+1

    if increasing and hasDubs:
        all_pass.append(password)

print(len(all_pass))
