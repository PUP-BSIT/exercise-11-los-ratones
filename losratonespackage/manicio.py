import qrcode

FILE_NAME = "manicio_qr.png"

def generate_qr_with_text(text):
    qr = qrcode.make(text)

    qr.save(FILE_NAME)
    
    print(f"QR code generated and saved as '{FILE_NAME}'")