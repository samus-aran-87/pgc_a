import requests
from bs4 import BeautifulSoup
import time
import smtplib


# https://www.google.com/search?rlz=1C5CHFA_enRU868RU868&sxsrf=ALeKk024wlDSsagV6Q7-bHj086sGvPVNSA%3A1584813096116&ei=KFR2XrrVBs_h6QS30I6QCQ&q=my+user+agent&oq=my+user+a&gs_l=psy-ab.3.0.0l2j0i203l2j0j0i203l2j0j0i203l2.53764.60108..60914...4.4..0.179.1088.14j1......0....1..gws-wiz.....10..0i71j0i10i1j35i305i39j0i67j0i10j0i22i10i30j0i22i30j0i10i1i42j35i362i39j35i39j0i10i203.-lCtyWyDj1A
# https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&rlz=1C5CHFA_enRU868RU868&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&aqs=chrome..69i57j69i65.6593j0j7&sourceid=chrome&ie=UTF-8

class Currency:
    url = "https://www.google.com/search?q=%D0%BA%D1%" + \
          "83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%" + \
          "B0%D1%80%D0%B0&rlz=1C5CHFA_enRU868RU868&oq=%" + \
          "D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0" + \
          "%BB%D0%B0%D1%80%D0%B0&aqs=chrome..69i57j69i65." + \
          "6593j0j7&sourceid=chrome&ie=UTF-8"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel M" +
                             "ac OS X 10_15_3) AppleWebKit/537.36 (KH" +
                             "TML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    # pas = "zzbslsbogapofuyu"

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_pryce().replace(",", "."))

    def get_currency_pryce(self):
        full_page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_pryce().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос!")
            self.send_mail()
        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал!")
            self.send_mail()
        print("Сейчас курс: 1 доллар = " + str(currency) + " руб.")
        time.sleep(10)
        self.check_currency()

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("1178817@gmail.com", "zzbslsbogapofuyu")

        subject = "Currency"
        body = "Course has been changed!"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            "abcfox7@gmail.com",
            "1178817@gmail.com",
            message
        )
        server.quit()


currency = Currency()
currency.check_currency()
