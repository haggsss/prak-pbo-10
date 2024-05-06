# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:55:53 2024

@author: kusfi
"""

from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(BangunDatar):
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2

class Trapesium(BangunDatar):
    def __init__(self, sisi_a, sisi_b, tinggi):
        self.sisi_a = sisi_a
        self.sisi_b = sisi_b
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * (self.sisi_a + self.sisi_b) * self.tinggi



