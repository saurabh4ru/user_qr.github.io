import pandas as pd
import qrcode

# Read the CSV file into a DataFrame
df = pd.read_csv('user_info.csv')

# Loop through each row and generate QR code
for index, row in df.iterrows():
    email = row['Email']
    name = row['Name']

    # Construct the URL with email and name parameters
    url = f'https://yourwebsite.com/redirect-page?email={email}&name={name}'

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with a unique filename
    img.save(f'qr_codes/{email}_qr.png')
