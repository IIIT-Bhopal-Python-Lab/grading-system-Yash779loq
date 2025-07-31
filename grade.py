while True:
    print("enter the Marks OR QUIT to stop")
    user_input =input()

    if user_input == 'QUIT':
        print("program has stoped")
        break

    Marks = int(user_input)

    
    if Marks>=90 and Marks<=100 :
        print("Grade are A")
    elif Marks>=75 and Marks<=89  :
        print("Grade are B")  
    elif Marks>=60 and Marks<=74  :
        print("Grade are C")
    elif Marks>=40 and Marks<=59  :
        print("Grade are D")
    elif Marks>=0 and Marks<=40  :
        print("Grade are E")
    else :
        print("Invalid input")


    