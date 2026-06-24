from address_info import Address
from mailing import Mailing

to_address = Address('249039', 'Обнинск', 'проспект Ленина', '5', '6')
from_address = Address('284576', 'Саратов', 'проспект Ленина', '27', '136')

mailing = Mailing(to_address,
                  from_address,
                  cost=1200,
                  track='124204PU023984')

print(mailing)
