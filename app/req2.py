import requests

base_url = 'https://petfriends.skillfactory.ru'

url = base_url + '/api/pets'
headers = {"accept": "application/json",
           "auth_key": "ff25b6f6b331d0645f0b7dbc388a810384da4dacaaa12f9df9e3efd9"}

with open("test.jpg", "rb") as file:
    files = {
        "name": (None, "Test"),
        "animal_type": (None, "animal"),
        "age": (None, "1"),
        "pet_photo": ("test.jpeg", file, "image/jpeg")
    }

    res = requests.post(url, headers=headers, files=files)

print(res.status_code)
print(res.json())