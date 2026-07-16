def main():

    try:
        a = int(input("enter a number: "))
        return print(a)

    except Exception as e :
        return print(e)

    finally: 
        print("hey i am inside finally")


main()