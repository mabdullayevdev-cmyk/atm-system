from atm import ATM


def main():
  bankomat = ATM("NBU Bankomat")

  while True:
    print("\n==============================")
    print(f"      {bankomat.nomi}")
    print("==============================")
    print("1) Yangi hisob yaratish")
    print("2) Tizimga kirish")
    print("3) Dasturni yakunlash")

    tanlov = input("Tanlovingizni kiriting (1-3): ")

    if tanlov == "1":
      bankomat.hisob_yaratish()
    elif tanlov == "2":
      if bankomat.tizimga_kirish():
        bankomat.menu()
    elif tanlov == "3":
      print("Dastur yakunlandi. Xayr!")
      break
    else:
      print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")


if __name__ == "__main__":
  main()