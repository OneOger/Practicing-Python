# CodeForces
# 131A


def caps():
    a = input()

    if a == a.upper():
        a = a.lower()
    elif a == a[0].lower() + a[1:].upper():
        a = a[0].upper() + a[1:].lower()

    return a


print(caps())

















