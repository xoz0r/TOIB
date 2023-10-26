Практическая работа №3, keycloak


На ВМ1 был развернут сервис keycloak с помощью docker контейнера

![1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/c0411382-aa97-4560-8aaa-65d21f49670b)
![1 1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/4563483b-5ac1-46fb-b235-b3ff77b79924)
![2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/4b53d220-c0b7-4276-aa37-c6c79ac4e64e)

Создал новый реалм

![4](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/8192ee06-1479-4dea-9717-8385538ae446)
![4 1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/4b00845b-517f-4b42-a6c6-82e648fed1df)

В реалме создал тестовых пользователей

![5  appadmin](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/e8f8183f-e7eb-4db2-9da6-a20e03d14667)
![6  2ppolz](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/053e9d8e-2700-40e0-aeba-829f154a74dc)

В качестве приложения на ВМ 2 для реализации аутентификации при помощи keycloak выбрал Jupyter Hub, создаю клиента для него

![6 1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/d46f6803-2292-444f-9d1b-d1468adf95bb)

Для Jupyter Hub был написан данный конфиг для успешной привязки сервисов друг к другу

![7 4 psd](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/425fe705-2e8f-43ac-9976-eaa0d274d632)

Сервис успешно запустился со сторонним сервисов аутентификации

![7, jupyt](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/ce58c869-5d1d-4f00-a2df-935a4d38f26b)
Тут я забыл обновить страницу

Аутентификация успешно прошла с помощью заданной связки логин-пароль в keycloak

![8 2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/44a84392-3da5-4711-8cf6-592b85ccbac3)

Далее включаем OTP в настройках приложения в keycloak

![9](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/2e00ddf6-2003-49c8-9cb1-3c5372fca589)

При перезаходе в приложение нам предложило добавить запись в OTP клиент

![end psd](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/6654ca0a-5da4-43cd-bdca-16b67d254d20)
