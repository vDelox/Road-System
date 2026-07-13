Hiz = int(input("Hızınız nedir: "))

Komut = input("Mevcut yol kodunu girin (A1, A2, A3): ")

if Komut == "A1" or Komut == "a1":
    if Hiz <= 40:
        print("Kurallara uyduğunuz için teşekkürler.")
    elif Hiz > 40:
        print("Lütfen kurallara uyun.")

if Komut == "A2" or Komut == "a2":
    if Hiz <= 100:
        print("Kurallara uyduğunuz için teşekkürler.")
    elif Hiz > 100:
        print("Lütfen kurallara uyun.")

if Komut == "A3" or Komut == "a3":
    if Hiz <= 150:
        print("Kurallara uyduğunuz için teşekkürler.")
    elif Hiz > 150:
        print("Lütfen kurallara uyun.")
