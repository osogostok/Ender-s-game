# Day 06 - Python Bootcamp

* Прежде чем приступить к работе рекомендуем создать виртуальное пространство и установить необходимые библиотеки    
    ```bash 
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Exercise 00: Kirov Reporting

1) Сгенерируте файлы __*.proto__:  
    ```bash 
    python3 -m grpc_tools.protoc -I ./protos --python_out=./protos --pyi_out=./protos  --grpc_python_out=./protos  ./protos/file.proto
    ```

2) Зайдите в папку __protos__ и сделайте изменения в файле __file_pb2_grpc__ изменить строчку 5 на:
    ```python 
    import protos.file_pb2 as file__pb2
    ```
    *Примечание: это связано с расположением папок*

3) Теперь перейдите в папку __ex00__ и запустите сервер:
    ```bash
    cd ex00
    python3 reporting_server.py  
    ```
4) Создайте новый терминал и зайдите в виртуальной пространство 
4) Теперь вы сможете запустить файл и __reporting_client.py__ и увидеть список короблей
    ```bash
    python3 reporting_client.py  12.3 12 104 5
    ```
## Exercise 01: Data Quality

1) Перейдите в папку __ех01__ и запустите файл __reporting_client_v2.py__
    ```bash
    cd ../ex01
    python3 reporting_client_v2.py  12.3 12 104 5
    ```
2) Также вы можете запустить тесты и проверить работу функции фильтров

## Exercise 02: Keeping Records
1) Перейдите в папку __ех02__
2) Запустите *PostgreSQL*
3) Зайдите в файл __.env__ и зполните поле __PASSWORD__ 
4) Зпуските скрипт файла __create_bd.py__
5) После вы можете запустить файл __reporting_client_v3.py__
    ```bash
    python3 reporting_client_v3.py scan 17 45 40.0409 00 28.118
    ```
6) Чтобы увидеть список придателей введите: 
    ```bash
    python3 reporting_client_v3.py list_traitors
    ```