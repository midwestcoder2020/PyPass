import random

def makeOne():
    lets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    pword=""
    for x in range(random.randint(10,14)):
        pword+=lets[random.randint(0,len(lets)-1)]
    return pword

def main():
    while True:
        pword = makeOne()
        print("\nHere is a new password")
        print(pword)
        key = input("\nenter (y) to keep or any other enter to generate another one" )
        if key == "y":
            print("\nOk you decided to keep password :" + pword)
            break


if __name__ == '__main__':
    main()






