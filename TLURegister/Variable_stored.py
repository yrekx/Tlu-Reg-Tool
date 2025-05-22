import os
from datetime import datetime


clear = lambda: os.system('cls')
S_DICT = {"S_ID":None}
simplified_data = {}
subject_name = []
access_token = ''
simplified_data = {}
header = {}

access_token_url = "https://sinhvien1.tlu.edu.vn:8098/education/oauth/token"                
user_url = "https://sinhvien1.tlu.edu.vn:8098/education/api/semester/semester_info"                        #update the new url here if its changed
subject_url = "https://sinhvien1.tlu.edu.vn:8098/education/api/cs_reg_mongo/findByPeriod/***"              #enter your User-specific API Endpoints
register_url = "https://sinhvien1.tlu.edu.vn:8098/education/api/cs_reg_mongo/add-register/***"


data = {
        'client_id': 'education_client',
        'grant_type': 'password',
        'username': '***',
        'password': '***',
        'client_secret': 'password'
    }   


proxies = {
    'http':'127.0.0.1:8080',
    'https':'127.0.0.1:8080'
}

def update_variable(value):
    global header
    header = value


def access_token(access_token):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 129.0) Gecko/20100101 Firefox/129.0',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding':'gzip, deflate, br',
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
                'origin':'https: //sinhvien1.tlu.edu.vn',                                                #here
                'Referer': 'https: //sinhvien1.tlu.edu.vn/' 
                }
    return headers 



def convert_timestamp(timestamp):
    timestamp_in_seconds = timestamp / 1000.0
    dt = datetime.fromtimestamp(timestamp_in_seconds)
    return dt.strftime('%H:%M')


