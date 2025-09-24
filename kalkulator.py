class kalkulator:
    def __init__(self):
        self.dataset = {}

    def setNamaDataset(self, nama:str) -> None:
        try:
            if nama in self.dataset.keys():
                raise ValueError("Nama Sudah digunakan!")
            else:
                self.dataset[nama] = []
                print(f"Dataset {nama} berhasil dibuat!")
        except ValueError as e:
            print(e)

    def lihatDataset(self) -> None:
        if not self.dataset:
            print("Kosong. Belum ada Dataset!")
        else:
            for key, value in self.dataset.items():
                print(f"{key} => {value}")

    def hapusDataset(self, nama:str) -> None:
        try:
            if nama in self.dataset.keys():
                del self.dataset[nama]
                print(f"Dataset {nama} berhasi dihapus!")
            else:
                raise ValueError("Dataset tidak ditemukan!")
        except ValueError as e:
            print(e)
    
    def inputData(self, nama) -> None:
        while True:
            try:
                input_data = input("masukkan data (contoh: 1,2,3) : ").replace(',',' ')
                data = [float(data) for data in input_data.split()]
                if not data:
                    print("Input tidak boleh kosong. Coab lagi!")
                    continue
                self.dataset[nama] = data
                break
            except ValueError:
                print("Input tidak valid. Pastikan semua data adalah angka!")
            except Exception as e:
                print(e)
                
    

def main():
    kalk = kalkulator()

    kalk.setNamaDataset("tinggi")
    kalk.lihatDataset()
    kalk.inputData('tinggi')
    kalk.lihatDataset()
    kalk.hapusDataset("tinggi")
    kalk.lihatDataset()

if __name__ == "__main__":
    main()