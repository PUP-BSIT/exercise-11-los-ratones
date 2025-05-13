import pyfiglet

def ice_cream_flavor():
    banner = pyfiglet.figlet_format("Ice Cream Time!")
    print(banner)

    name = input("Choose a name (Ruby, Ayumu, Shiki or your name): ")
    if name == 'Ruby':
        print("Ruby chan! <3")
        print("Your Ice cream is Choco Minto! <3")
    elif name == 'Ayumu':
        print("Ayumu chan! <3")
        print("Your Ice cream is Sutoraberi Fureiba! <3")
    elif name == 'Shiki':
        print("Shiki chan! <3")
        print("Your Ice cream is Kuki ando kurimu! <3")
    else:
        print(f"{name} chan! <3")
        print("Yori mo anata! <3")
