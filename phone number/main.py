from phonenumbers import timezone  # timezone is used to get the timezone
from phonenumbers import carrier  # carrier is used to get the carrier name
from phonenumbers import geocoder  # geocoder is used to get the country name
import phonenumbers

# ********* Taking Input *********
number = input("Enter yout Phone No:")
print("Phone Number: "+number)

# ********* Country code *********
# CH is the country code passed to the parse function to get the country name
ch_number = phonenumbers.parse(number, "CH")
# description_for_number is used to get the country name in english
Country_name=geocoder.description_for_number(ch_number, "en")
print("Country: "+ Country_name  )

# ********* carrier name *********
# RO is the country code passed to the parse function to get the carrier name
service_number = phonenumbers.parse(number, "RO")
# name_for_number is used to get the carrier name in english
Carrier_Name=carrier.name_for_number(service_number, "en")
print("Carrier: "+Carrier_Name)

# ********* timezone *********
# GB is the country code passed to the parse function to get the timezone
gb_number = phonenumbers.parse(number, "GB")
# time_zones_for_number is used to get the timezone
Timezone = timezone.time_zones_for_number(gb_number)
print("Timezone: "+ Timezone)
