from losratonespackage.campos import ice_cream_flavor
#TODO(Jedi Duncan Gonot): Module 2
#TODO(Dion Manicio): Module 3
#TODO(Paul Benidict Reduta): Module 4
#TODO(John Paul Rodriguez): Module 5

def main():
    while True:
        print("Welcome To Los Ratones Modules!",
            "1. Campos Module",
            "2. Gonot Module", 
            "3. Manicio Module",
            "4. Reduta Module",
            "5. Rodriguez Module", 
            "6. Exit",
            sep="\n")
        
        choice = int(input("Enter your choice(1-5): "))

        match choice:
            case 1:
                ice_cream_flavor()
                input("Press Enter to continue...")
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Invalid choice. Please select a valid choice.")

main()