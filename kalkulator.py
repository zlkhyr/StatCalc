class kalkulator:
    def __init__(self):
        self.dataset = {}

    def menu(self):
        menu = [
            ["No", "Menu", "Deskripsi"],
            ["1", "Buat Dataset", "Membuat dataset baru"],
            ["2", "Lihat Dataset", "Menampilkan semua dataset"],
            ["3", "Input Data", "Memasukkan data ke dataset"],
            ["4", "Mean", "Menghitung rata-rata"],
            ["5", "Median", "Menghitung median"],
            ["6", "Mode", "Menghitung mode"],
            ["7", "Range", "Menghitung range"],
            ["8", "Quartile", "Menghitung quartile 1/2/3"],
            ["9", "IQR", "Menghitung IQR"],
            ["10", "Varians", "Menghitung varians"],
            ["11", "Std", "Menghitung standard deviation"],
            ["12", "Summary", "Menghitung rata-rata data"],
            ["13", "Hapus Dataset", "Menghapus dataset tertentu"],
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
        return self.quartil(nama, 2) 

    #Masih belum sempurna    
    def mode(self, nama) -> list:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        freq = {}
        for i in self.dataset[nama]:
            freq[i]=freq.get(i, 0) + 1

        max_freq = max(freq.values())
        return [key for key, value in freq.items() if value == max_freq]
    
    def range(self, nama) -> int:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        return max(self.dataset[nama]) - min(self.dataset[nama])
    
    def quartil(self, nama, kuartil) -> float:
        if nama not in self.dataset:
            raise KeyError(f"Dataset {nama} tidak ditemukan!")
        
        if not self.dataset[nama]:
            raise ValueError("Tidak bisa melakukan perhitungan pada dataset kosong")
        
        data = sorted(self.dataset[nama])
        n = len(data)
        tengah = n // 2

        if n % 2 == 1:
            bawah = data[:tengah]
            atas = data[tengah + 1:]
        else:
            bawah = data[:tengah]
            atas = data[tengah:]

        if kuartil == 1:
            data = bawah
        if kuartil == 2:
            pass
        if kuartil == 3:
            data = atas

        if len(data)%2 == 1:
            return data[int(len(data)/2)]
        else:
            return (data[int(len(data)/2)] + data[int(len(data)/2)-1])/2 


    def iqr(self, nama) -> float:
        return self.quartil(nama, 3) - self.quartil(nama, 1)

    def varians(self, nama) -> float:        
        rata2 = self.mean(nama)
        xi_x2 = []
        for xi in self.dataset[nama]:
            xi_x2.append((xi - rata2)**2)
        return sum(xi_x2)/(len(self.dataset[nama])-1)

    def standard_deviation(self, nama) -> float:
        return self.varians(nama) ** (1/2)

    def summary_statistics(self, nama) -> None:
        menu = [
            ["Mean", self.mean(nama)],
            ["Median", self.median(nama)],
            ["Mode", self.mode(nama)],
            ["Range", self.range(nama)],
            ["Quartile 1", self.quartil(nama, 1)],
            ["Quartile 2", self.quartil(nama, 2)],
            ["Quartile 3", self.quartil(nama, 3)],
            ["IQR", self.iqr(nama)],
            ["varians", self.varians(nama)],
            ["Standard deviation", self.standard_deviation(nama)]
        ]

        print("=" * 50)
        for row in menu:
            print(f"{row[0]:<20} : {row[1]}")
        print("=" * 50)
    
    # perhitungan statistika lainya ...

def main():
    kalk = kalkulator()
    #test
    kalk.menu()
    
    # Interaksi dengan kalkulator melalui CLI
    while True:
        try:
            try:
                pilihan = int(input("No : "))
            except ValueError:
                print("Input tidak valid. Input angka 0-5!")
                continue
            match pilihan:
                case 0:
                    print("Keluar")
                    break
                case 1:
                    nama = input("Nama Dataset : ")
                    kalk.setNamaDataset(nama)
                case 2:
                    kalk.lihatDataset()
                case 3|4|5|6|7|8|9|10|11|12|13:
                    nama = input("Nama Dataset : ")
                    if pilihan == 3:
                        kalk.inputData(nama)
                    elif pilihan == 4:
                        print(f"Mean : {kalk.mean(nama)}")
                    elif pilihan == 5:
                        print(f"Median : {kalk.median(nama)}")
                    elif pilihan == 6:
                        print(f"Mode : {kalk.mode(nama)}")
                    elif pilihan == 7:
                        print(f"Range : {kalk.range(nama)}")
                    elif pilihan == 8:
                        print(f"Quartile : {kalk.quartil(nama, kuartil=1)}")
                    elif pilihan == 9:
                        print(f"IQR : {kalk.iqr(nama)}")
                    elif pilihan == 10:
                        print(f"Varians : {kalk.varians(nama)}")
                    elif pilihan == 11:
                        print(f"Standar deviasi: {kalk.standard_deviation(nama)}")
                    elif pilihan == 12:
                        kalk.summary_statistics(nama)
                    elif pilihan == 13:
                        kalk.hapusDataset(nama)
                case _:
                    print(f"tidak ada menu ke-{pilihan}")
        except (ValueError, KeyError) as e:
            print(e)
            continue

if __name__ == "__main__":
    main()