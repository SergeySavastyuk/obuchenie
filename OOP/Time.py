from datetime import datetime

# ваш код:
class Product:
    @staticmethod
    def check_date(today, expiry):
        start = datetime.strptime(today,'%Y-%m-%d')
        finish = datetime.strptime(expiry,'%Y-%m-%d')
        print(['Срок годности в порядке','Срок годности истёк'][start>=finish])

# код ниже пожалуйста не удаляйте
today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)