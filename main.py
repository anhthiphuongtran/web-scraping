from bs4 import BeautifulSoup
import requests
import smtplib


TIKI_URL = "https://tiki.vn/storytelling-with-data-ke-chuyen-thong-qua-du-lieu-cuon-cam-nang-huong-dan-truc-quan-hoa-du-lieu-p76013378.html?spid=76013379"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Provide the email address and password to send email via smtp.
MY_EMAIL = "tulunpct92@gmail.com"
MY_PASSWORD ="jsmynkmnxobescgq"

# Set the lowest price you are willing to pay for the product (the cut-off price).
BUY_PRICE = 210

# Extract the price of the product from Tiki website.
response = requests.get(TIKI_URL, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")
price = soup.find(class_="product-price__current-price").text

# Show the price in terms of thousands.
price_k = int(price.split(".")[0])

# Compare the current price and the cut-off price of the product.
if price_k < BUY_PRICE:
    # Send email to notify if the current price is below the cut-off price
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:LOW PRICE!\n\nGreat! \nThe execellent book 'Storytelling with Data' is now only {price_k}.000 VND. TIME TO BUY!"
        )
