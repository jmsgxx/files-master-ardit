class Bill:
    """
    payable amount and period
    """

    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    create a person name as flatmate, period
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class Pdfreport:
    """
    generate a pdf report
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, amount):
        pass


bill_month = Bill(amount=120, period="Aug 2021")
joven = Flatmate(name='joven', days_in_house=20)
mark = Flatmate(name='mark', days_in_house=25)

print(joven.pays(bill=bill_month, flatmate2=mark))

