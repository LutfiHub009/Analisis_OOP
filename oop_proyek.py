# proyek toko elektronik dengan OOP
# by M.Lutfilah Zaki/25
from abc import ABC, abstractmethod



# ABSTRACT CLASS (Abstraction)
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0                # private attribute
        self.__harga_dasar = harga_dasar  # private attribute

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Getter harga dasar (dipakai anak class)
    def _get_harga_dasar(self):
        return self.__harga_dasar

    # Method tambah stok (Encapsulation)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    @abstractmethod
    def tampilkan_detail(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass



# CHILD CLASS: Laptop
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.10
        subtotal = self.hitung_harga_total(jumlah)

        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {harga:,.0f} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.10
        return (harga + pajak) * jumlah



# CHILD CLASS: Smartphone

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.05
        subtotal = self.hitung_harga_total(jumlah)

        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {harga:,.0f} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.05
        return (harga + pajak) * jumlah



# POLYMORPHISM: Keranjang Belanja
def proses_transaksi(daftar_barang):
    total = 0
    print("\n--- STRUK TRANSAKSI ---")
    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail(jumlah)
        total += barang.hitung_harga_total(jumlah)

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")


# MAIN PROGRAM (User Story)
print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)   # harus gagal
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)
