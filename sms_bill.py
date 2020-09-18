


# please go through readme file first !

import requests
import time

import datetime
now = datetime.datetime.now()
a=now.strftime("%d-%m-%Y %H:%M:%S")


authorization_code ="Paste your authorization code here"
def send_sms():

    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {"authorization":authorization_code
                   ,"sender_id":"Rupak","message":actual_message,"language":"english","route":"p","numbers":number}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    print(response.text)

    





def number():
    global number
    try:
        number=int(input("Enter Coustoner Number : "))
    except Exception as e:
        print("Invalid Mobile Number. Please Try Again!")
        number()
        
def advace_amount():
    global advance
    try:
        advance=int(input("Enter Advance : "))
        balance=total-advance
        print("Balance amount is : ",balance)
    except Exception as ae:
        print("Invalid Amount Enterd. Please try again!",end='\n')
        advace_amount()
        
def total_amount():
    global total
    try:
        total=int(input("Enter Total amount : "))
    except Exception as te:
        print("Invalid Amount Enterd. Please try again!",end='\n')
        total_amount()

        




def details_receipt():
    global balance
    global number
    global job_number
    global total
    global advance
    global actual_message
    
    balance=0
    name=input("Name of coustomer : ").lower()
    try:
        number=int(input("Mobile. No. : "))
    except Exception as e:
        print("Invalid Mobile Number. Please Try Again!",end='\n')
        number()
    
    photos_size=input("Photo size : ")
    
    photo_number=input("Enter Photo Number : ")
    
    
    try:
        total=int(input("Enter Total amount : "))
    except Exception as te:
        print("Invalid Amount Enterd. Please try again!",end='\n')
        total_amount()
        
        
    try:
        advance=int(input("Enter Advance : "))
        balance=total-advance
        print("Balance amount is : ",balance)
    except Exception as ae:
        print("Invalid Amount Enterd. Please try again!",end='\n')
        advace_amount()
        
    b=name[0:1]
    j=now.strftime("%d%m%M%S")
    msg_date=now.strftime("%d-%m-%Y")
    job_number=j+b
    actual_message="Rupak "+"\n"+"Date :"+msg_date+"\n"+"Name: "+name+"\n"+"Photo size: "+str(photos_size)+"\n"+"Photo No.: "+str(photo_number)+"\n"+"Adv. Amt: "+str(advance)+"\n"+"Balance Amt: "+str(balance)+"\n"+"NOTE: COLLECT YOUR PHOTO WITHIN 5 WORKING DAYS.\nTHIS MESSAGE IS VALID FOR 7 DAYS ONLY \n T&C* \n \nThank you for Visiting!"
    
    
    csv_message="\n"+a+","+job_number+","+name+","+str(number)+","+str(photos_size)+","+str(photo_number)+","+str(total)+","+str(advance)+","+str(balance)
    fh = open("data.csv", "a")
    lines_of_text = csv_message
    fh.write(lines_of_text)
    fh.close()
        
    for_sms=input("Do you want to send sms to the coustomer : ")
    
    if (("y" in for_sms) or ("Y" in for_sms)):
        send_sms()
    if (("n" in for_sms) or ("N" in for_sms)):
        print()
        print("Thank you!")
        
        
    for_repeat=input("Do you want to create another bill ? : ")
    if (("y" in for_repeat) or ("yes" in for_repeat)):
        details_receipt()
    if (("n" in for_repeat) or ("no" in for_repeat)):
        print("Thank you")
        time.sleep(2)

    
details_receipt()
