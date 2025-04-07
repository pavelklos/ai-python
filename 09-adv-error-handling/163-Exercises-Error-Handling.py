# 163 : Exercises: Error Handling
# TODO: we add finally block to the try-except block

while True:
    # noinspection PyBroadException # TODO: CHECK PyBroadException
    try:
        age = int(input("What is your age: "))
        division = 10 / age
        print(age)
        # break                                 # TODO:break the loop
    # except:
    #     print("Please enter a number")
    except ValueError:
        print("Please enter a number")
        # continue                              # TODO: continue to the next iteration
    except ZeroDivisionError:
        print("Please enter a number other than zero")
        # break                                         # TODO: break the loop
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e))
        # break                                         # TODO: break the loop
    else:
        print("Thank you!")
        break
    finally:
        print("Finally block always executes")
    print("This is important line")  # TODO: this line will never be executed
