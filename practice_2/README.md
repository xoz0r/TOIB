# Идентификация и аутентификация 

### 1. Создать виртуальную машину на базе ОС Debian 12
![Виртуальная машина запущена](https://imgur.com/TSqOnhb)

### 2. Создать пользователя super_BDI, наделить его привилегиями суперпользователя 
```bash
sudo useradd super_BDI
sudo usermod -a -G sudo super_BDI
```
![Создание и добавление пользователя в группу sudo](https://imgur.com/CL1aroW)

### 3. Зайти под созданным пользователем и создать группу group-bbmo0123
```bash
su super_BDI
sudo groupadd group-bbmo0123
```
![Вход под пользователем и Создание группы](https://imgur.com/ss8Kc7z)

### 4. Добавить пользователя super_BDI в группу group-bbmo0123
```bash
sudo usermod -a -G group-bbmo0123 super-BDI
```
![Добавление пользователя в группу](https://imgur.com/ss8Kc7z)

### 5. Продемонстрировать наличие пользователя в группе
```bash
groups super_BDI
```
![Список групп пользователя](https://imgur.com/ceDX6AZ)

### 6. Создать пользователя user-BDI, добавить его в группу group-bbmo0123
```bash
sudo useradd user-BDI
sudo usermod -a -G group-bbmo0123 user-BDI
```
![Создание и добавление пользователя](https://imgur.com/eTR3T8Q)

### 7. Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod)  пользователя user-BDI по созданию и удалению файлов в домашнем каталоге пользователя super_BDI
![Создание домашнего каталога (его не было)](https://imgur.com/N8fVjXm)
![Наделение полномочиями](https://imgur.com/6eWTBMO)
```bash
sudo chmod 770 ~
sudo chown super_BDI:group-bbmo0123
```
### 8. Продемонстрировать работу механизмов разграничения доступа
```bash
whoami
cd /home/super_BDI
touch 1.txt
rm 1.txt
```
![Демонстрация работы](https://imgur.com/P7YOgCi)

```bash
https://imgur.com/a/xTrIOok
```

