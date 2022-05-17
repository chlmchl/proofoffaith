from unittest import result
import requests
#import datetime
import time
import serial

#setup
arduino = serial.Serial(port='/dev/cu.usbmodem21101', baudrate=9600, timeout=1)
url = "https://www.bitstamp.net/api/v2/transactions/btcusd/"

#getting data
payload={}
headers = {}
    
#sending data to arduino
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Say something: ") # Taking input from user
    if(num == 'start'):
        while True:
            response = requests.request("GET", url, headers=headers, data=payload)
            response = response.json()
            #hash = response['txs'][0]['hash']
            #time = time.gmtime(response['txs'][0]['time'])
            hash = response[0]['tid']
            #time = time.localtime(int(response[0]['date']))
            amountBTC = response[0]['amount']
            valueBTC = response[0]['price']
            amountUSD = int(float(amountBTC) * float(valueBTC))
            type = int(response[0]['type'])

            if type == 0:
                tx = 'bought'
            elif type == 1:
                tx = 'sold'
            else: 
                tx = 'error'

            #print(hash, tx)
            #print(time)

            sentence = '#' +  str(hash) + ' just ' + str(tx) + ' ' + str(amountBTC) + ' BTC (~' + str(amountUSD) + ' USD)'
            print(sentence)
            value = write_read(sentence)
            time.sleep(5)
    #print(value) # printing the value
