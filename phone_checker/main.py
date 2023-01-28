import phonenumbers as phn
from phonenumbers import geocoder

phone = input("Enter the phone: Ex.: +5511999999999 ")

phone_number = phn.parse(phone)

print(geocoder.description_for_number(phone_number, "pt"))
