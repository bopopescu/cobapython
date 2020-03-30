class segitiga:
        def __init__(self):
            self.alas = 0.0
            self.tinggi = 0.0

obj = segitiga()
obj.alas = 5
obj.tinggi = 3

luas = (obj.alas * obj.tinggi) / 2

print('Luas Segitiga = %.2f' % luas)
