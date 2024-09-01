from Variable_stored import *  
import requests


def get_token():
    try:
        response = requests.post(access_token_url, data=data)        
        token = response.json().get('access_token')
        if not token:
            print('No token found in the response')
        
        return token
    except Exception as e:
        print(f'An error occurred: {e}')
    return None

def get_semester_info():
    global headers 
    token = get_token()
    if not token:
        print('Failed to get token')
        return None
    
    headers = access_token(token)
    update_variable(headers)
    try:
        user_response = requests.get(user_url, headers=headers)
        return user_response.json()
    except Exception as e:
        print(f'An error occurred: {e}')
    return None

def semester():
    semester_info = get_semester_info()
    if not semester_info:
        print('No semester info available')
        return
    
    try:
        semester_register_periods = semester_info.get('semesterRegisterPeriods', [])

        if isinstance(semester_register_periods, list):
            print("Semester Register Periods:")
            for period in semester_register_periods:
                if isinstance(period, dict):
                    name = period.get('name', 'Not Available')
                    period_id = period.get('id', 'Not Available')
                    print(f"ID: {period_id}\t Semester: {name}")
        else:
            print("Semester Register Periods data is not in the expected format")
    except Exception as e:
        print(f'Error processing semester info: {e}')

def subject(semester_ID):
   global headers 
   subject_response = requests.get(subject_url + str(semester_ID), headers=headers)
   subject = subject_response.json()
   content = subject.get('courseRegisterViewObject', {})
   semester_register_subject = content.get('listSubjectRegistrationDtos', [])
   return subject_response.json(),semester_register_subject