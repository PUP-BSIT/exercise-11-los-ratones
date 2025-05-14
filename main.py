from losratonespackage.campos import ice_cream_flavor
from losratonespackage.gonot import movie
from losratonespackage.manicio import generate_qr_with_text
from losratonespackage.rodriguez import basic_calculations
from losratonespackage.reduta import download_and_save_image

PAUSE_MESSAGE = "Press Enter to continue..."

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

        choice = int(input("Enter your choice(1-6): "))

        match choice:
            case 1:
                ice_cream_flavor()
                input(PAUSE_MESSAGE)

            case 2:
                movie()
                input(PAUSE_MESSAGE)
                
            case 3:
                generate_qr_with_text("Hello from Manicio!")
                input(PAUSE_MESSAGE)

            case 4:
                image_url = """https://preview.redd.it/gigil-ako-sa-mga-pet
                -owners-na-walang-konsensya-v0-5z50gy2a3kze1.jpeg?width=640
                &crop=smart&auto=webp&s=caaa94aa00921ee78d43a14fdff1a79b174
                d8be3"""

                download_and_save_image(image_url)
                input(PAUSE_MESSAGE)

            case 5:
                result = basic_calculations()
                print(result)
                input(PAUSE_MESSAGE)

            case 6:
                #Exit
                break

            case _:
                print("Invalid choice. Please select a valid choice.")

main()