import requests
import os
import sys

class DownloadFile:
    def __init__(self, f, overwrite=False):
        self.base_url = r'http://lstarnes.com/data/sfte2018'
        if (os.path.isdir(os.path.dirname(f)) and 
            os.path.dirname(f) != f and 
            os.path.lexists(os.path.dirname(f))):
            self.file = os.path.basename(f)
            self.path = f
        elif f == os.path.basename(f):
            self.path = os.path.join(os.getcwd(), 'data', f)
            self.file = f
        else:
            print(f'{f} must be either a full path or a filename.')
            sys.exit(1)

        self.url = f'{self.base_url}/{self.file}'

        if os.path.exists(self.path):
            if not overwrite:
                print(f'File ({self.path}) already exists and overwrite not enabled.')
                sys.exit(1)
            else:
                print(f'File ({self.path}) already exists, but overwrite enabled so downloading.')

        self.get()

    def get(self):
        url = 'http://google.com/favicon.ico'
        r = requests.get(self.url, allow_redirects=True)
        open(self.path, 'wb').write(r.content)
        print(f'{self.file} successfully downloaded to {self.path}')

if __name__ == "__main__":
    #Test
    DownloadFile('2018-06-11.h5-maptiles.p', overwrite=True)