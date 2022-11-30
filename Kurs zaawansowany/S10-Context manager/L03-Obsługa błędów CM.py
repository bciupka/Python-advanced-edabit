import os, requests, zipfile

class downloadFile:
    def __init__(self, url, path, chunk_size=128):
        self.url = url
        self.path = path
        self.cs = chunk_size

# sposób preferowany z documentacji do pobierania zipów
    def downloading(self):
        c = requests.get(self.url, stream=True)
        with open(self.path, 'wb') as f:
            for chunk in c.iter_content(self.cs):
                f.write(chunk)

# sposób prostszy
    def downloading2(self):
        c = requests.get(self.url)
        with open(self.path, 'wb') as f:
                f.write(c.content)

    def __enter__(self):
        self.downloading() #może być też init jeżeli chce się korzystać z funkcjonalności bez 'with', a przy samej inicjacji (bez recznego wywoływania metody)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print('Nie znaleziono lokalizacji')
            return True
        elif exc_type == KeyError:
            print('Nie znaleziono pliku')
            return True
        else:
            return False

# UWAGA!!! Jeżeli błąd wystąpi w __enter__ to błąd nie zostanie obsłużony bo metoda __exit__ się nie wykona

path = r'D:\Projekty\PyCharm\temp\S10-L02\zipfile.zip'
url = r'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'

with downloadFile(url, path) as f:
    with zipfile.ZipFile(path, 'r') as z:
        file = z.namelist()[0]
        print(file)
        os.chdir(path.rstrip(r'file.zip')) #zmiana workspace-u
        print(path.rstrip(r'file.zip'))
        z.extract('file', '.', None)

