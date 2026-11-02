from transaction import Transaction


class Account:

  def __init__(self, id, egasi, karta_raqami, pin, balans=0.0):
    self.id = id
    self.egasi = egasi
    self.karta_raqami = karta_raqami
    self.pin = pin
    self.balans = balans
    self.tranzaksiyalar = []
    self._tranzaksiya_id_counter = 1

  def balansni_korish(self):
    print(
        f"\n--- Hisob egasi: {self.egasi} ---\nJoriy balans: {self.balans} so'm"
    )

  def pul_qoshish(self, summa):
    if summa > 0:
      self.balans += summa
      t = Transaction(self._tranzaksiya_id_counter, "Deposit", summa)
      self.tranzaksiyalar.append(t)
      self._tranzaksiya_id_counter += 1
      print(f"Muvaffaqiyatli! {summa} so'm hisobga qo'shildi.")
    else:
      print("Xatolik: Summa 0 dan katta bo'lishi kerak!")

  def pul_yechish(self, summa):
    if summa > 0:
      if self.balans >= summa:
        self.balans -= summa
        t = Transaction(self._tranzaksiya_id_counter, "Withdraw", summa)
        self.tranzaksiyalar.append(t)
        self._tranzaksiya_id_counter += 1
        print(f"Muvaffaqiyatli! {summa} so'm yechib olindi.")
        return True
      else:
        print("Xatolik: Hisobda yetarli mablag' mavjud emas!")
    else:
      print("Xatolik: Summa 0 dan katta bo'lishi kerak!")
    return False

  def pin_tekshirish(self, kiritilgan_pin):
    return self.pin == kiritilgan_pin

  def tranzaksiyalar_tarixini_korish(self):
    if not self.tranzaksiyalar:
      print("\nHozircha tranzaksiyalar tarixi mavjud emas.")
    else:
      print(f"\n--- {self.egasi} ning tranzaksiyalar tarixi ---")
      for tr in self.tranzaksiyalar:
        tr.malumot()