# ===========================================================
# 🐍 PYTHON DASTURLASH TILINI 0 DAN O'RGANISH — TUSHUNTIRUVCHI MISOLLAR
# Muallif: Bilolbek uchun tayyorlandi
# Mazmuni: Har bir buyruq yonida tushuntiruvchi izoh bor
# ===========================================================

# === 1. Konsolga chiqarish ===
# print() funksiyasi — ekranga yozuv chiqaradi
print("Salom, dunyo!")  # natija: Salom, dunyo!

# === 2. O'zgaruvchilar ===
# O'zgaruvchi — ma'lumotni saqlovchi nom
ism = "Bilol"
yosh = 18
print("Mening ismim:", ism)
print("Men", yosh, "yoshdaman")

# === 3. Ma'lumot turlari ===
# str (matn), int (butun son), float (kasr son), bool (True/False)
ism = "Aziza"
yosh = 22
bal = 4.5
studentmi = True
print(type(ism))        # <class 'str'>
print(type(yosh))       # <class 'int'>
print(type(bal))        # <class 'float'>
print(type(studentmi))  # <class 'bool'>

# === 4. Foydalanuvchidan ma'lumot olish ===
# input() — foydalanuvchidan kiritilgan ma'lumotni oladi (har doim matn sifatida)
# yosh = input("Yoshingizni kiriting: ")
# print("Siz", yosh, "yoshdasiz")

# === 5. Arifmetik amallar ===
a = 10
b = 3
print("Qo‘shish:", a + b)
print("Ayirish:", a - b)
print("Ko‘paytirish:", a * b)
print("Bo‘lish:", a / b)
print("Butun bo‘lish:", a // b)
print("Qoldiq:", a % b)
print("Daraja:", a ** b)

# === 6. Shart operatorlari (if, elif, else) ===
son = 5
if son > 0:
    print("Musbat son")
elif son < 0:
    print("Manfiy son")
else:
    print("Nol")

# === 7. Mantiqiy operatorlar ===
# and, or, not
x = 7
print(x > 5 and x < 10)  # True
print(x < 5 or x == 7)   # True
print(not(x == 7))       # False

# === 8. Ro‘yxatlar (list) ===
mevalar = ["olma", "banan", "gilos"]
print(mevalar)
print(mevalar[0])        # birinchi element
mevalar.append("nok")    # yangi element qo‘shish
print(mevalar)
mevalar.remove("banan")  # elementni o‘chirish
print(mevalar)

# === 9. Takrorlash operatorlari (for, while) ===
# for - ma'lum miqdordagi aylanish
for i in range(5):  # 0 dan 4 gacha
    print("i =", i)

# while - shart to‘g‘ri bo‘lsa davom etadi
x = 0
while x < 3:
    print("x =", x)
    x += 1

# === 10. Funksiyalar ===
# def - yangi funksiya yaratish
def salom_ber(ism):
    print("Salom,", ism)

salom_ber("Bilol")

# === 11. Return qiymat ===
def kvadrat(son):
    return son ** 2

natija = kvadrat(5)
print("5 ning kvadrati:", natija)

# === 12. Lug‘atlar (dictionary) ===
talaba = {"ism": "Anvar", "yosh": 20, "kurs": 2}
print(talaba["ism"])
talaba["bahosi"] = 4.7  # yangi juftlik
print(talaba)

# === 13. To‘plamlar (set) ===
sonlar = {1, 2, 3, 3, 4}
print(sonlar)  # takroriy element yo‘q

# === 14. Tuple (o‘zgarmas ro‘yxat) ===
oylar = ("yanvar", "fevral", "mart")
print(oylar[1])

# === 15. Fayllar bilan ishlash ===
# Fayl yaratish va yozish
with open("malumot.txt", "w", encoding="utf-8") as f:
    f.write("Bu birinchi faylimiz.\n")
    f.write("Python juda oson!")

# Faylni o‘qish
with open("malumot.txt", "r", encoding="utf-8") as f:
    print("\n=== Fayldan o‘qilgan ma’lumot ===")
    print(f.read())

# === 16. Xatolikni ushlash (try-except) ===
try:
    son = int(input("Son kiriting: "))
    print("Natija:", 100 / son)
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
except ValueError:
    print("Faqat son kiriting!")

# === 17. Modul chaqirish ===
import math
print("Pi:", math.pi)
print("Kvadrat ildiz (64):", math.sqrt(64))

# === 18. Class va obyektlar ===
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def tanishtir(self):
        print(f"Men {self.ism}, {self.yosh} yoshdaman.")

t1 = Talaba("Bilol", 18)
t1.tanishtir()

# === 19. Ro‘yxatni filtrlash va list comprehension ===
sonlar = [1, 2, 3, 4, 5, 6]
juftlar = [s for s in sonlar if s % 2 == 0]
print("Juft sonlar:", juftlar)

# === 20. Kutubxonalar haqida ===
# Kutubxona — bu tayyor funksiyalar to‘plami.
# Masalan, random kutubxonasi tasodifiy sonlar bilan ishlaydi.
import random
print("Tasodifiy son:", random.randint(1, 10))

# === 21. Yakun ===
print("\n🎉 Siz Python asoslarini o‘rgandingiz! Endi amaliy loyihalarga o‘ting.")
