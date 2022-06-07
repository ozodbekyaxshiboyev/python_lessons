"""
22/12/2020

Dasturlash asoslari

#21-dars: FUNKSIYAGA RO'YXAT UZATISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar


talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
