docker build -t database .
docker build -t backend ./Backend/
docker build -t frontend ./frontend/
docker network create mynetwork
docker run --name database --network=mynetwork -d database:latest
sleep 5
docker run --name backend --env-file ./Backend/.env -p 8000:8000 --network=mynetwork -d backend:latest
docker run --name frontend --env-file ./frontend/.env -p 3000:3000 --network=mynetwork -d frontend:latest