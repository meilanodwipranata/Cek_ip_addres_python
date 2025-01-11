# By Meilano Dwi Pranata

# import kebutuhan
import requests

# URL Request
url = "https://ipinfo.io/json?"
# Request Terindikasi Client
headers = {"User-Agent": "chrome ,mozila"}

# Mengambil data dari URL
response = requests.get(url, headers=headers)
    
# Memastikan respons HTTP berhasil
response.raise_for_status()

# Mengubah json menjadi variable
data = response.json()

# print doang
print("Info Ip Addres:")


# perulangan list data ip
for ip, value in data.items():
        # menghilangkan data loc
        if ip != "loc":
                # menghilangkan data readme
                if ip != "readme":
                        print(f"{ip.capitalize()} : {value.capitalize()}")
                        print()

                        