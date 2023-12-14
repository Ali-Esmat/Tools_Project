docker build -t database .
docker build -t backend ./Backend/
docker build -t frontend ./frontend/
docker network create mynetwork
docker run --name database -p 5432:5432 --network=mynetwork -d database:latest
sleep 5
docker run --name backend -p 8000:8000 --network=mynetwork -d backend:latest
docker run --name frontend -p 3000:3000 --network=mynetwork -d frontend:latest