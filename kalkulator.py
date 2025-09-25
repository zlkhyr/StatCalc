class kalkulator:
    def __init__(self):
        self.dataset = {}

    def menu(self):
        menu = [
            ["No", "Menu", "Deskripsi"],
            ["1", "Buat Dataset", "Membuat dataset baru"],
            ["2", "Lihat Dataset", "Menampilkan semua dataset"],
            ["3", "Input Data", "Memasukkan data ke dalam dataset"],
            ["4", "Hitung Mean", "Menghitung rata-rata data"],
            ["5", "Hapus Dataset", "Menghapus dataset tertentu"],
            ["0", "Keluar", "Keluar dari program"]
        ]

        print("=" * 50)
        for row in menu:
            print(f"{row[0]:<3} {row[1]:<15} {row[2]}")
        print("=" * 50)

    def setNamaDataset(self, nama:str) -> None:
        if nama in self.dataset:
            raise KeyError(f"Sudah ada dataset dengan nama {nama}!")
        
        self.dataset[nama] = []
        print(f"Dataset {nama} berhasil dibuat!")

    def lihatDataset(self) -> None:
        if not self.dataset:
            raise KeyError("Kosong. Belum ada Dataset!")
        
        for key, value in self.dataset.items():
            print(f"{key} => {value}")

    def hapusDataset(self, nama:str) -> None:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        del self.dataset[nama]
        print(f"Dataset {nama} berhasi dihapus!")

    
    def inputData(self, nama) -> None:
        while True:
            input_data = input("masukkan data (contoh: 1,2,3) : ").replace(',',' ')
            try:
                data = [float(data) for data in input_data.split()]
            except ValueError:
                print("Input tidak valid. Pastikan semua data adalah angka!")
                continue
            if not data:
                print("Input tidak boleh kosong. Silahkan coba lagi!")
                continue
            self.dataset[nama] = data
            break
    
                
    def mean(self, nama) -> int:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        return sum(self.dataset[nama])/len(self.dataset[nama])

def main():
    kalk = kalkulator()
    while True:
        try:
            kalk.menu()
            try:
                pilihan = int(input("No : "))
            except ValueError:
                raise ValueError("Input tidak valid. Input angka 0-5!")
            match pilihan:
                case 0:
                    print("Keluar")
                    break
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
        except (ValueError, KeyError) as e:
            print(e)
            continue


if __name__ == "__main__":
    main()