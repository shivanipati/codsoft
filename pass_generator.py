import string
import random
if __name__ == '__main__':
    m1 = string.ascii_lowercase
    print(m1)

    m2 = string.ascii_uppercase
    print(m2)

    m3 = string.digits
    print(m3)

    m4 = string.punctuation
    print(m4)

    name = int(input("enter the password "))

    s =[]
    s.extend(list(m1))
    s.extend(list(m2))
    s.extend(list(m3))
    s.extend(list(m4))
    # print(s)
    random.shuffle(s)
    # print(s)

    print("your password is ....")
    print("".join(random.sample(s,name)))