# Demo Flask service

### Architecture

```
.
├── BACK.md
├── Makefile
├── controllers
│   ├── __init__.py
│   └── black_white.py
├── requirements.txt
├── runner.py
├── tests.py
└── views.py
```

### Setup Linux
1. Установка необходимого ПО
    ```
    $sudo apt install python
    $sudo apt install python3-pip
    $sudo apt install make
    ```

2. Настройка проекта
    ```
    $make clear
    $make venv
    $make install_requirements
    ```
   
### Run server

1. Создать файл .env в корне проекта и указать в нем PORT, например:
    ```
    PORT=5001
    ```
   
2. Запустить работу сервера
    ```
    $make run
    ```
   
### Testing

- Для тестирования достаточно выполнить 
    ```
    $make test
    ```

### API

- Получение черно-белого изображения `method='GET'`
  (пока отдает тестовую строку 'Hello world!')
    ```
    /black-white/
    ```