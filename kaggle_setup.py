def main():
  
  !pip install -r requirements.txt
  !kaggle datasets download -d matteocastrignano/mirflickr
  import zipfile

  with zipfile.ZipFile("mirflickr.zip", "r") as zip_ref:
      zip_ref.extractall(".")
  import os

  os.rename('mirflickr25k', 'data')
  os.remove("mirflickr.zip")

if __name__ == '__main__':
  main()