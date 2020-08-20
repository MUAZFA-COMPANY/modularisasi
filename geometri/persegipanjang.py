from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, le):
        self.p = p
        self.le = le

    def info(self):
        return f'Ini adalah object dari Persegi Panjang dengan panjang = {self.p} dan lebar = {self.le}'

    def hitung_luas(self):
        return self.p * self.le
