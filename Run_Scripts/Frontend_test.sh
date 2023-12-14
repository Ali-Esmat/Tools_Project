source ./frontend/.env
docker build -t frontend ./frontend/
docker run --name frontend --env-file ./frontend/.env -p $PORT:$PORT --network=mynetwork -d frontend:latest
docker ps -a