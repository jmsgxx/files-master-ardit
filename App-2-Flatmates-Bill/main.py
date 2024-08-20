class Bill:
    """
    payable amount and period
    """

    def __init__(self, total_bill: int, period: str):
        self.total_bill = total_bill
        self.period = period


class Flatmate:
    """
    create a person name as flatmate, period
    """

    def __init__(self, name: str, days_in_house: int):
        self.total_bill = None
        self.amount_each = None
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, total_bill):
        self.amount_each = self.total_bill / self.days_in_house





class Pdfreport:
    """
    generate a pdf report
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill_month = Bill(total_bill=120, period="Aug 2021")
joven = Flatmate(name='joven', days_in_house=15)
mark = Flatmate(name='mark', days_in_house=25)

print(mark.pays(bill=bill_month))
