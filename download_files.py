import requests
import os
import sys
from http.client import responses

class DownloadFile:
    def __init__(self, f, overwrite=False):
        self.base_url = r'http://lstarnes.com/data/sfte2018'
        self.success = False

        data_dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

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
                self.success = True
            else:
                print(f'File ({self.path}) already exists, but overwrite enabled so downloading.')
                self.get()
        else:
            self.get()

        

    def get(self):
        r = requests.get(self.url, allow_redirects=True)
        if r.status_code == 200:
            print(f'Downloading {self.file}.')
            open(self.path, 'wb').write(r.content)
            print(f'{self.file} successfully downloaded to {self.path}.')
            self.success = True
        else:
            print(f'Bad status code ({r.status_code} - {responses[r.status_code]}) for {r.url}. Unable to download.')
            

if __name__ == "__main__":
    #Test
    DownloadFile('2018-06-11.h5-maptiles.p', overwrite=True)
    #bad file
    DownloadFile('2018-06-11.h5-jibberish.p', overwrite=False)