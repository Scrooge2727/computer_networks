from ftplib import FTP
#ftp.thewrittenword.com
print("Введите адрес")
host = input()
ftp = FTP(host)
ftp.login()
ftp.retrlines('LIST')

print("Введите файл для загрузки")
file_name = input()

my_file = open(file_name, 'wb')
ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)

ftp.quit() # Завершить FTP-соединение  
my_file.close()
