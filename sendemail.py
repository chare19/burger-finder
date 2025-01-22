import smtplib
import gifget

class CreateMail:

    def __init__(self):
        self.from_email = "cam.python.test@gmail.com"
        self.to_email = "kaitbabin@gmail.com"
        self.password = "zyvnmqcsbkgxqoao"


    def sendmail(self, condition):
        giffer = gifget.GetGif()
        if condition:
            message = "🚨 IT IS HERE. THIS IS NOT A DRILL. 🚨"
        else:
            message = "It is not here 😔"

        link = f"Mood: {giffer.get_gif(condition)}"
        confirm = "See for yourself here: https://order.wendys.com/category/100/cheeseburgers?lang=en_CA"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.password)
            connection.sendmail(
                from_addr=self.from_email,
                to_addrs=self.to_email,
                msg="Subject:🍔 Monday Portabella Watch 👀\n\n"
                    f"Good morning Kait, happy Monday!\n\n"
                    f"{message}\n\n"
                    f"{link}\n\n"
                    f"{confirm}\n\n"
                    f"Hope you have a great week!\n".encode("utf-8")
            )

