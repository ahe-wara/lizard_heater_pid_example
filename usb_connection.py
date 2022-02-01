import sys
#import io
#import serial
import time

#todo: seperater thread auslagern
class Usb_Connection:

        #funktioniert! gepürft mit putty
        def write(self, input):
            string = str(input) + '\n'
            data = sys.stdout.write(string + '\n')
            #print('wrote something')            
        
        #funktioniert! Aber in extra thrat auslagern; gepürft mit putty
        def read(self):          
            data = sys.stdin.readline()
            #file.write(str(data))
            print(str(data))                 
            return str(data)
            

'''
PS> $port= new-Object System.IO.Ports.SerialPort COM3,9600,None,8,one
PS> $port.Open()
PS> $port.ReadLine()
'''

'''
while True:
        file = open('testfile.txt', 'w')
        file.flush()
        print('read something1')
        data = sys.stdin.readline(4)
        print('read something2')
        input = data.decode('utf-8')
        print('read something3')
        file.write(input + "\n")
        print('read something4')
        file.flush()
        print('read something5')
    
    #data = sys.stdout.write('Test' + '\n')
    #print('wrote something')
    #time.sleep_ms(5000)
        
        while True:
    sys.stdout.write(b'X')
    time.sleep_ms(5000)
'''    