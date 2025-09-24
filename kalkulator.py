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
    

def main():
    kalk = kalkulator()

    kalk.setNamaDataset("tinggi")
    kalk.setNamaDataset("berat")
    kalk.lihatDataset()
    kalk.setNamaDataset("tinggi")
    kalk.hapusDataset("berat")
    kalk.hapusDataset("tinggi badan")
    kalk.lihatDataset()

if __name__ == "__main__":
    main()