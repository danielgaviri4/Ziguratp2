import requests
import json



def create_user(token,data):
    url = 'http://127.0.0.1:8000/api/users/'
    headers = {'Authorization': 'Token '+token}
    r = requests.post(url, headers=headers,data=data)
    
    if r.status_code == 200:
        print(json.loads(r.text))
    else:
        print(r.text)


def generate_token(user,password):
    url = 'http://127.0.0.1:8000/api-token-auth/'
    data = {
        'username':user,
        'password':password
    }
    r = requests.post(url, data=data)
    # print(dir(r))
    if r.status_code == 200:
        return json.loads(r.text)['token']
    else:
        return r.text



if __name__=='__main__':
    t = generate_token('juan','1234')
    print(t)
    user_data = {
        'username': 'Medntor',
        'first_name': 'Mentor',
        'email': 'santiagdo@mentor.com',
        'password':'1234',


    }
    create_user(t,user_data)