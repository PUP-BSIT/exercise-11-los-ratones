import requests

def download_and_save_image(image_url): 
    response = requests.get(image_url)

    image = "alden.jpg"
    with open(image, "wb") as file:
        file.write(response.content)

    print(f"Image downloaded and saved as {image}")

 




