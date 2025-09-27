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
    
    def median(self, nama) -> int:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        data = sorted(self.dataset[nama])

        if len(data)%2 == 1:
            return data[int(len(data)/2)]
        else:
            return (data[int(len(data)/2)] + data[int(len(data)/2)-1])/2 
        
    def mode(self, nama) -> int:
        pass
    
    def range(self, nama) -> int:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        return max(self.dataset[nama]) - min(self.dataset[nama])
    
    def quartil(self, nama, kuartil) -> float:
        pass

    def iqr(self, nama) -> float:
        pass

    def varians(self, nama) -> float:
        pass

    def standard_deviation(self, nama) -> float:
        pass

    def summary_statistics(self, nama) -> float:
        pass
    
    # perhitungan statistika lainya ...

def main():
    kalk = kalkulator()
    #test
    kalk.setNamaDataset('tinggi')
    kalk.inputData('tinggi')
    print(kalk.median("tinggi"))
    print(kalk.mean("tinggi"))
    print(kalk.range("tinggi"))
    
    # Interaksi dengan kalkulator melalui CLI
    # while True:
    #     try:
    #         kalk.menu()
    #         try:
    #             pilihan = int(input("No : "))
    #         except ValueError:
    #             print("Input tidak valid. Input angka 0-5!")
    #             continue
    #         match pilihan:
    #             case 0:
    #                 print("Keluar")
    #                 break
    #             case 1:
    #                 nama = input("Nama Dataset : ")
    #                 kalk.setNamaDataset(nama)
    #             case 2:
    #                 kalk.lihatDataset()
    #             case 3:
    #                 nama = input("Nama Dataset")
    #                 kalk.inputData(nama)
    #             case 4:
    #                 nama = input("Nama Dataset : ")
    #                 print(f"Mean : {kalk.mean(nama)}")
    #             case 5:
    #                 nama = input("Nama Dataset : ")
    #                 kalk.hapusDataset(nama)
    #             case 6:
    #                 # fungsi lain
    #                 pass
    #             case _:
    #                 print(f"tidak ada menu ke-{pilihan}")
    #     except (ValueError, KeyError) as e:
    #         print(e)
    #         continue

if __name__ == "__main__":
    main()