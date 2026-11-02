import random
from account import Account


class ATM:

  def __init__(self, nomi="UzCard ATM"):
    self.nomi = nomi
    self.hisoblar = []
    self.joriy_hisob = None
    self.urinishlar = 0
    self._account_id_counter = 1

  def hisob_yaratish(self):
    print("\n--- Yangi Bank Hisobini Yaratish ---")
    egasi = input("Ism va familiyangizni kiriting: ")
    pin = input("4 xonali PIN-kod o'rnating: ")

    if len(pin) != 4 or not pin.isdigit():
      print("Xatolik: PIN-kod aniq 4 xonali raqam bo'lishi kerak!")
      return

    karta_raqami = "8600" + "".join([str(random.randint(0, 9)) for _ in range(12)])
    boshlangich_balans = float(
        input("Boshlang'ich balansni kiriting (so'm, 0 bo'lsa bo'sh qoldiring): ")
        or 0
    )

    yangi_hisob = Account(
        self._account_id_counter,
        egasi,
        karta_raqami,
        pin,
        boshlangich_balans,
    )
    self.hisoblar.append(yangi_hisob)
    self._account_id_counter += 1

    print(f"\nTabriklaymiz, hisob muvaffaqiyatli yaratildi!")
    print(f"Sizning karta raqamingiz: {karta_raqami}")
    print(f"Hisob ID: {yangi_hisob.id}")

  def hisobni_topish(self, karta_raqami):
    for hisob in self.hisoblar:
      if hisob.karta_raqami == karta_raqami:
        return hisob
    return None

  def tizimga_kirish(self):
    print("\n--- Tizimga Kirish ---")
    karta_raqami = input("Karta raqamini kiriting: ")
    hisob = self.hisobni_topish(karta_raqami)

    if not hisob:
      print("Xatolik: Bunday karta raqami topilmadi!")
      return False

    self.urinishlar = 0
    while self.urinishlar < 3:
      pin = input(
          f"PIN-kodni kiriting (Urinish {self.urinishlar + 1}/3): "
      )
      if hisob.pin_tekshirish(pin):
        self.joriy_hisob = hisob
        print(f"\nXush kelibsiz, {hisob.egasi}!")
        return True
      else:
        self.urinishlar += 1
        print("Xato PIN-kod!")

    print(
        "Diqqat: Noto'g'ri PIN-kod 3 marta kiritildi! Karta vaqtincha"
        " bloklandi."
    )
    return False

  def menu(self):
    while self.joriy_hisob:
      print("\n==============================")
      print(f"      USER MENU ({self.nomi})")
      print("==============================")
      print("1) Balansni tekshirish")
      print("2) Pul kiritish (Deposit)")
      print("3) Pul yechish (Withdraw)")
      print("4) Tranzaksiyalar tarixini ko'rish")
      print("5) PIN-kodni o'zgartirish")
      print("6) Tizimdan chiqish")

      tanlov = input("Tanlovingizni kiriting (1-6): ")

      if tanlov == "1":
        self.joriy_hisob.balansni_korish()
      elif tanlov == "2":
        summa = float(input("Kiritmoqchi bo'lgan summani kiriting (so'm): "))
        self.joriy_hisob.pul_qoshish(summa)
      elif tanlov == "3":
        summa = float(input("Yechib olmoqchi bo'lgan summani kiriting (so'm): "))
        self.joriy_hisob.pul_yechish(summa)
      elif tanlov == "4":
        self.joriy_hisob.tranzaksiyalar_tarixini_korish()
      elif tanlov == "5":
        eski_pin = input("Joriy PIN-kodni kiriting: ")
        if self.joriy_hisob.pin_tekshirish(eski_pin):
          yangi_pin = input("Yangi 4 xonali PIN-kodni kiriting: ")
          if len(yangi_pin) == 4 and yangi_pin.isdigit():
            self.joriy_hisob.pin = yangi_pin
            print("PIN-kod muvaffaqiyatli o'zgartirildi!")
          else:
            print("Xatolik: Yangi PIN-kod 4 xonali raqam bo'lishi kerak!")
        else:
          print("Xatolik: Joriy PIN-kod noto'g'ri!")
      elif tanlov == "6":
        print(f"\n{self.joriy_hisob.egasi} tizimdan chiqdi.")
        self.joriy_hisob = None
        break
      else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")