# Идентификация и аутентификация 

### 1. Создать виртуальную машину на базе ОС Debian 12
![Виртуальная машина запущена](https://disk.yandex.ru/i/qduQjwAMO7QnFw)

### 2. Создать пользователя super_BDI, наделить его привилегиями суперпользователя 
```bash
sudo useradd super_BDI
sudo usermod -a -G sudo super_BDI
```
![Создание и добавление пользователя в группу sudo](https://disk.yandex.ru/i/cZVMoto7SUVwvA)

### 3. Зайти под созданным пользователем и создать группу group-bbmo0123
```bash
su super_BDI
sudo groupadd group-bbmo0123
```
![Вход под пользователем](https://disk.yandex.ru/i/UWKs4DiUX06Mbg)

![Создание группы](https://disk.yandex.ru/i/GaCYxyYRXR5eQA)

### 4. Добавить пользователя super_BDI в группу group-bbmo0123
```bash
sudo usermod -a -G group-bbmo0123 super-BDI
```
![Добавление пользователя в группу](https://disk.yandex.ru/i/GaCYxyYRXR5eQA)

### 5. Продемонстрировать наличие пользователя в группе
```bash
groups super_BDI
```
![Список групп пользователя](https://disk.yandex.ru/i/sXAuzNvXcESuXw)

### 6. Создать пользователя user-BDI, добавить его в группу group-bbmo0123
```bash
sudo useradd user-BDI
sudo usermod -a -G group-bbmo0123 user-BDI
```
![Создание и добавление пользователя](https://disk.yandex.ru/i/zJLK2PfnxXPYAg)

### 7. Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod)  пользователя user-BDI по созданию и удалению файлов в домашнем каталоге пользователя super_BDI
![Создание домашнего каталога (его не было)](https://disk.yandex.ru/i/Vghiy-AEEO5pVw)
![Наделение полномочиями](https://disk.yandex.ru/i/aFiGfYfdGLCLFg)
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
![Демонстрация работы](https://disk.yandex.ru/i/fBnu5GwIqBfaIg)

