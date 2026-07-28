class Phone:
    manufactured = "China"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(_, phone, sms):
        text = f"sending to: {phone} {sms}"
        print(text)


my_phone = Phone("Sakira", "Oppo", 54000)

print(my_phone.owner, my_phone.brand, my_phone.price)

hasa_phone = Phone("Hasa", "Vivo", 76000)
print(hasa_phone.owner, hasa_phone.brand, hasa_phone.price)