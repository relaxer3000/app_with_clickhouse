Для запуска необходимо последовательн ввести команды:

docker compose up
docker exec -d app_task_9-app-1 python main.py 
docker exec -d app_task_9-app-1 faststream run rabbit/consumer:app 

подключиться к документации Swagger UI можно по адрессу: http://127.0.0.1:5001/docs