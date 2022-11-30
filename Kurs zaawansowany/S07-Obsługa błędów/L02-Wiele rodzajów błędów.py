import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = r'D:\Projekty\PyCharm\temp\S07-L01'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    os.remove(tmpfile_path) if os.path.isfile(tmpfile_path) else None
    # save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)
except requests.exceptions.ConnectionError as e:
    print(e)
except PermissionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Problem: {}'.format(e))
else:
    print('Udało się')
finally:
    os.remove(tmpfile_path) if os.path.isfile(tmpfile_path) else None