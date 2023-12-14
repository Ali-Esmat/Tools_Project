source ./frontend/.env
docker build -t frontend ./frontend/
docker run --name frontend --env-file ./frontend/.env -p $REACT_APP_PORT:$REACT_APP_PORT --network=mynetwork -d frontend:latest
docker ps -a