import Variable_stored
import requests
def send(ID):
    for i in range(int(input("Enter the request's number:"))):
        # num_threads = 5
        # threads = []

        # for i in range(num_threads):
        #     thread = threading.Thread(target=submit,args=(subject_url,List_of_sub[index]))
        #     threads.append(thread)
        #     thread.start()

        # for thread in threads:
        #     thread.join()

      
        submiting = requests.post(Variable_stored.register_url +str(ID) ,json = Variable_stored.simplified_data,headers= Variable_stored.header)
        submit_response = submiting.json()
        if 'Bạn đã đăng ký thành công' in submit_response.get('message'):
            print("You got it!")
            break 
        else:
            print(submiting.status_code)

