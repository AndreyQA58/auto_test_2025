import requests


class Pets:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'

    def add_pet(self, id, category, name, photoUrls, tags, status):
        headers = {'accept': 'application/json',
                   'Content-Type': 'application/json'}
        data = {'id': id,
                'category': category,
                'name': name,
                'photoUrls': photoUrls,
                'tags': tags,
                'status': status
                }
        res = requests.post(self.base_url + '/pet',
                            headers=headers,
                            json=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except ValueError:
            result = res.text
        return status, result
        print(status)


p = Pets()
p.add_pet(123456777778, {"id": 0, "name": "string"},
                'test2', ["string"],
                [{"id": 0, "name": "string"}], 'available')
