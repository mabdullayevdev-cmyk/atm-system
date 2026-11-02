from datetime import datetime


class Transaction:

  def __init__(self, id, turi, summa):
    self.id = id
    self.turi = turi  # "Deposit" yoki "Withdraw"
    self.summa = summa
    self.sana = datetime.now()

  def malumot(self):
    sana_str = self.sana.strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"Tranzaksiya ID: {self.id} | Turi: {self.turi} | Summa: {self.summa}"
        f" so'm | Vaqti: {sana_str}"
    )