import requests  # pip3 install requests

url =  # URL загружаемого файла

print("Downloading with requests...")
r = requests.get(url)
with open("download_file", "wb") as file:
    file.write(r.content)
