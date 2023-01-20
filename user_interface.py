def menu():
    while True:
        num_type = input("Enter\n"
                        "1-compl\n"
                        "2-ra\n"
                        "3-ex\n")
        match num_type:
            case "1":
                pass
            case "2":
                menu_ra()
            case "3":
                break
            case _:
                print("Err")


# menu()