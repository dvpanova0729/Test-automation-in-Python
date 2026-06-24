from smartphone import Smartphone

catalog = [
    Smartphone('Xiaomi', '14 Ultra', '+7 (900) 123-33-44'),
    Smartphone('Samsung', 'Galaxy Z', '+7 (900) 333 33 33'),
    Smartphone('Apple', '17 Pro Max', '+7 (910) 986 66 77'),
    Smartphone('Apple', '17 Pro', '+7 (910) 986 55 77'),
    Smartphone('Apple', '14 Pro Max', '+7 (910) 932 82 97')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
