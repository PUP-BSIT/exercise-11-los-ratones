#TODO(Kenji Enishi Campos): Module 1
#TODO(Jedi Duncan Gonot): Module 2
#TODO(Dion Manicio): Module 3
from losratonespackage.reduta import download_and_save_image
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
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                image_url = "https://preview.redd.it/gigil-ako-sa-mga-pet-owners-na-walang-konsensya-v0-5z50gy2a3kze1.jpeg?width=640&crop=smart&auto=webp&s=caaa94aa00921ee78d43a14fdff1a79b174d8be3"
                download_and_save_image(image_url)
                input("Press Enter to continue...")
            case 5:
                pass
            case 6:
                break
            case _:
                print("Invalid choice. Please select a valid choice.")

main()