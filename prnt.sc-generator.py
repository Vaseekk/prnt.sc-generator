import random

def generuj_odkazy(pocetOdkazu):
    pismenko = "abcdefghijklmnopqrstuvwxyz"
    cislicko = "1234567890"
    for _ in range(pocetOdkazu):
        print("https://prnt.sc/" + random.choice(pismenko) + random.choice(pismenko) + random.choice(cislicko) + random.choice(cislicko) + random.choice(cislicko) + random.choice(cislicko))

def main():
    jeLiboDalsi = True

    while jeLiboDalsi:
        print("Kolik odkazů je libo?:")
        pocetOdkazu = int(input())

        generuj_odkazy(pocetOdkazu)

        print("Znovu?[y/N]: ")
        anoNe = input()
        if anoNe != "y":10
            jeLiboDalsi = False

if __name__ == "__main__":
    main()
