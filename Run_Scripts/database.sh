source ./Backend/.env
docker build -t database .
docker run --name database --env-file ./Backend/.env --network=mynetwork -d database:latest