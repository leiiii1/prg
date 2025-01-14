# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GLCrDvvkXXlpx3WU4DEnAHdXq59ZrohG
"""

print("Čauky mňauky, dnes si zahrajeme hru. Vygeneruji ti čtyřciferné číslo a ty ho budeš hádat")
import random

# Funkce pro generování čtyřciferného čísla s unikátními číslicemi
def vygeneruj_4ciferne_cislo():
  cislice = random.sample(range(1, 10), 1)  # První číslice nesmí být 0
  cislice += random.sample(range(0, 10), 3)  # Další tři číslice
  while len(set(cislice)) < 4:  # Kontrola na unikátní číslice
    cislice = random.sample(range(1, 10), 1) + random.sample(range(0, 10), 3)
  return int("".join(map(str, cislice)))

# Funkce pro hru Bulls and Cows
def bulls_and_cows():
    # Generování tajného čísla
    tajne_cislo = vygeneruj_4ciferne_cislo()
    print("Zkus uhodnout čtyřciferné číslo (každá číslice je unikátní).")

    while True:
        hadane_cislo = input("Zadej čtyřciferné číslo: ")

        # Ověření, že uživatel zadal správný formát čísla
        if len(hadane_cislo) != 4 or not hadane_cislo.isdigit() or len(set(hadane_cislo)) != 4:
            print("Prosím, zadej čtyřciferné číslo bez opakujících se číslic.")
            continue

        # Zkontrolujeme, zda číslo nezačíná nulou
        if hadane_cislo[0] == '0':
            print("Číslo nemůže začínat nulou. Zkus to znovu.")
            continue

        bulls = 0
        cows = 0

        # Počítání býků (bulls) a krav (cows)
        for i in range(4):
            if hadane_cislo[i] == str(tajne_cislo)[i]:
                bulls += 1
            elif hadane_cislo[i] in str(tajne_cislo):
                cows += 1

        print(f"Býci: {bulls}, Krávy: {cows}")

        # Když hráč uhodne správně
        if bulls == 4:
            print(f"Gratuluji! Uhodl jsi číslo: {tajne_cislo} čauky mňauky.  ")
            break

# Spustí hru
bulls_and_cows()