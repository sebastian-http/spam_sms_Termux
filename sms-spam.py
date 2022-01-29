import os
import time
import dee.logo
os.system('clear')

dee.logo.show()
option1=input('>>> ')


if option1=='a':
   print('go')

elif 'e' in option1:
   os.system('exit()')







else:
   while 'a' not in option1:
      print('ERROR')
      time.sleep(1)
      os.system('clear')
      dee.logo.show()
      option1=input('>>> ')




os.system('clear')
dee.logo.goo()

sms1=input('\x1b[1;30mINGRESA MENSAJE A ENVIAR >>>\x1b[00m ')
print('\n\n')
sms2=int(input('\x1b[1;30mINGRESA NUMERO DE TELEFONO >>>\x1b[00m '))


print('\n\n')
sms3=int(input('\x1b[1;30mINGRESA CANTIDAD DE MENSAJES A ENVIAR >>>\x1b[00m '))



def termux_api():
   os.system('clear')
   for i in range(sms3):
      print('\x1b[1;33mENVIANDO SPAM ...\x1b[00m')
      api=('termux-sms-send -n')
      e=' '
      api2= api+e+str(sms2)+e+sms1
      os.system(api2)
      print(i,'\x1b[1;31mse envio con exito....\x1b[00m')



termux_api()


os.system('clear')
print("\x1b[1;33m PROSESO DE SPAM FINALISADO.....\x1b[00m")








