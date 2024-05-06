# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:02:30 2024

@author: kusfi
"""

from prak10 import Persegi, PersegiPanjang, Segitiga, Lingkaran, Trapesium

print("==============")
print("Syahrul Arifin")
print("==============")


persegi1 = Persegi(4,)
print("Luas persegi:", persegi1.hitung_luas())

segitiga1 = Segitiga(3, 6)
print("Luas segitiga:", segitiga1.hitung_luas())

lingkaran1 = Lingkaran(5)
print("Luas lingkaran:", lingkaran1.hitung_luas())

persegi_panjang1 = PersegiPanjang(4, 8)
print("Luas persegi panjang:", persegi_panjang1.hitung_luas())

Trapesium1 = Trapesium(5, 6, 8)
print("Luas Trapesium:", Trapesium1.hitung_luas())

