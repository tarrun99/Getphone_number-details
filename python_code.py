import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata

phone_number = phonenumbers.parse(  ) #enter mobile number

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_numer, 'en'))
print(phonemetadata.NumberFormat(phone_number, 'en'))
