# Практическая работа. Сбор логов.
Выполнил Бакин Д.И., группа ББМО-01-23
## `1. Создание и настройка виртуальных машин`
![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/552d6858-1dbc-413b-abf7-43792df14417)

## `2. Обеспечение сетевого обмена`

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/aba75eca-aafc-4bc2-914e-ac18ad8aaeda)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/55c164f8-f281-4403-a0c8-4dd1b6388052)

## `3. rsyslog`

### Установка и настройка `rsyslog` на сервере

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/fc5af5e0-bc8e-4576-af02-1c5eec4b558a)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/87b02bf4-142e-4556-9847-22714e653523)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/203dd800-d2eb-4320-8e50-984c3dbd3ef6)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/d94909a5-a181-425d-8b9b-68f4e9396c89)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/9f708646-6b71-4478-937a-d3dadc952fd3)

### Установка и настройка `rsyslog` на клиенте

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/51f5d7c5-b650-4849-a402-7bb16d1896d9)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/ba12f711-30cf-4d33-aa7b-b0e6b9369737)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/07b4c3e0-bc58-412c-b832-33dd7b0ff113)

### Тут я резко понимаю что нужно изменить имена машин

![ИМЕНАХОСТОВ](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/a1c5afb6-481e-4d81-8958-bcb1b473d52e)

### Результат выполнения задания

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/77b9e065-8deb-4c49-9edf-b0fd8f8885f9)

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/d37114c9-4de5-464a-8fbc-c6f4d1de7f69)

## `4. Grafana Loki`

### Загрузка, установка, настройка и запуск compose-файла на сервере

![loki1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/9cb608d8-f055-4923-9930-982343230fd8)

![loki2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/59af87b7-a13b-4fd2-a5a3-cb59be8fa015)

### Редактирование compose-файла с целью отключения компонента `promtail` на сервере

![loki3 отключ promtail](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/b8b97daa-e671-4693-ba1a-b697c3f9304a)

### Запуск Loki

![loki4 запуск](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/1232a118-4fda-4db8-abd5-2a5d38b437b1)

### Редактирование конфигурации `promtail` на клиенте

![promtail cl1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/9d1714e9-d247-48cf-9777-0d549bdf6c66)

![promtail cl2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/2753c574-ffd2-430f-a0ab-277373c9b104)

тут должен был быть скриншот запуска promtail на клиенте, но он бесследно исчез(

### Настройка и просмотр логов клиента в Grafana

![](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/1614f150-e5b1-4f79-99c3-89534818b1ad)

## `5. Signoz`

### Запуск Signoz

Установка согласно https://signoz.io/docs/install/docker/#install-signoz-using-docker-compose

![signoz1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/406fd10d-34d8-46e4-9e39-95411849ac59)

![signoz2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/71dbd81f-1990-48cc-b70c-589fedfc15d8)

![signoz3](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/88f1a2ba-8d9b-49d1-ad90-865ea5a450dc)

![signoz4](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/24c0d1c4-7ca7-4512-aa3e-d8e85a4f016c)

### Установка клиентского приложения 

![signozcl1](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/644b9888-db36-4e85-93d2-0f74f88c9623)

![signozcl2](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/63445cc5-7663-428e-b4ce-e2deeb5e6488)

### Редактирование конфигурации клиентского приложения для отправки данных в Signoz

![signozcl3](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/61cb27a0-14f7-485b-85ac-aaa9bfecff91)

### Результат работы

![signozcl4](https://github.com/xoz0r/TOIB_Bakin/assets/145142526/c550e03b-901b-4483-aa76-002b2219db3c)
