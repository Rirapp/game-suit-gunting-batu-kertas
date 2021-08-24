##gunting,batu,kertas 
##feat bot


#---input fungsi yang dibutuhin---#
from time import sleep
from random import randint
from os import system

#variabel?
menang = 0
kalah = 0
seri = 0
r = 0

#listing code 
def instructions ():
  print('''''
  Batu,Gunting,Kertas \n 
  Ketik "1" untuk Batu, "2" untuk kertas dan "3" untuk gunting''''')
instructions()
uty = int(input('\nMau Main Berapa Ronde?\n'))
#mencegah User bandel 
while uty != r:
  movimento_bot = randint(1 , 3)
  movimento = int(input('\nPilih Apa:'))
  if movimento > 3 or movimento < 1:
    while movimento > 3 or movimento < 1 :
      print('\nTida ada dipilihan, Ulangi.\n')
      movimento = int(input('pilih apa: '))
#HERE WE GO  
  for tempo in range (3,0,-1):
    print(f'{tempo}...')
    sleep(0.5)
  print(f"Musuh Milih: {movimento_bot}")
#kalo seri  
  if movimento == movimento_bot:
    print ('\nSeri!')
    seri += 1
#kalo menang
  elif movimento == 1 and movimento_bot == 3:
    print('\nCIIE MENANG!')
    menang += 1
  elif movimento == 2 and movimento_bot == 1:
    print('\nCIIE MENANG!')
    menang += 1
  elif movimento == 3 and movimento_bot == 2:
    print('\nCIIE MENANG!')
    menang += 1
#kalo kalah
  else:
    print('\nSabar ya,Yuk Bisa Yuk!')
    kalah += 1
#Pe(round)ean duniawi
  r += 1 
  if r != uty:
    print("\nPindah Round....\n")
  sleep(2)
  system('clear')
  instructions()
system('clear')
#give u the fookin score
print(f'''\n\nSCORE AKHIR\n
Menang: {menang}
Kalah: {kalah}
Seri: {seri} ''')
#the end

