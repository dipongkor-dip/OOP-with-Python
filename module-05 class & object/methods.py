def call():
    print("call this function")
    return "cal done"


class Phone:
    price = 1200
    color = "blue"
    brand = "moto"
    features = ["camera", "speaker", "hammer"]

    def call(_):
        print("calling demo function")

    def send_sms(_, phone, sms):
        text = f"sending sms to: {phone} and message: {sms}"
        return text


my_phone = Phone()
print(my_phone.features)

print(my_phone.call())
text = my_phone.send_sms(121234, "I miss you")
print(text)
