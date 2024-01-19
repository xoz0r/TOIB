# Идентификация и аутентификация 

### 1. Создать виртуальную машину на базе ОС Debian 12

![Виртуальная машина запущена](https://imgur.com/TSqOnhb)

![TSqOnhb1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/cb99aecd-f44a-441c-a4a6-02954f1cae1a)

### 2. Создать пользователя super_BDI, наделить его привилегиями суперпользователя 
```bash
sudo useradd super_BDI
sudo usermod -a -G sudo super_BDI
```

![Создание и добавление пользователя в группу sudo](https://imgur.com/CL1aroW)

![TSqOnhb2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/08408459-9c06-413c-bb25-2f230981f35c)

### 3. Зайти под созданным пользователем и создать группу group-bbmo0123
```bash
su super_BDI
sudo groupadd group-bbmo0123
```

![Вход под пользователем и Создание группы](https://imgur.com/ss8Kc7z)

![TSqOnhb3](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/f7385d00-77de-4e01-acb1-a52b86961710)

### 4. Добавить пользователя super_BDI в группу group-bbmo0123
```bash
sudo usermod -a -G group-bbmo0123 super-BDI
```

![Добавление пользователя в группу](https://imgur.com/ss8Kc7z)

![TSqOnhb4](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/a18612de-370d-4495-b159-d9a9057a6360)

### 5. Продемонстрировать наличие пользователя в группе
```bash
groups super_BDI
```

![Список групп пользователя](https://imgur.com/ceDX6AZ)

![TSqOnhb5](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/fbe7e01d-21ab-49af-8380-12652658a8f7)

### 6. Создать пользователя user-BDI, добавить его в группу group-bbmo0123
```bash
sudo useradd user-BDI
sudo usermod -a -G group-bbmo0123 user-BDI
```

![Создание и добавление пользователя](https://imgur.com/eTR3T8Q)

![TSqOnhb6](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/f060e5ad-65a7-4e00-9c08-61f2cda3bb2e)

### 7. Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod)  пользователя user-BDI по созданию и удалению файлов в домашнем каталоге пользователя super_BDI

![Создание домашнего каталога (его не было)](https://imgur.com/N8fVjXm)

![TSqOnhb7](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/d1fcef92-dc9a-4ae6-8622-76e8519d5b31)

![Наделение полномочиями](https://imgur.com/6eWTBMO)

![TSqOnhb8](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/271c938c-2ecb-468b-9521-002b83ad6be8)

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

![TSqOnhb9](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/8f64cbf0-35da-46c7-a1f1-1cd0c0f948cc)

```bash
https://imgur.com/a/xTrIOok
```

