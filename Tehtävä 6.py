leiviskät = int(input("Leiviskät: "))
naulat = int(input("Naulat: "))
luodit = int(input("Luodit: "))

luodityhteensä = leiviskät * 20 * 32 + naulat * 32 + luodit
grammatyhteensä = luodityhteensä * 13.3

kilogrammat = int(grammatyhteensä // 1000)
grammat = grammatyhteensä % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat} grammaa.")
