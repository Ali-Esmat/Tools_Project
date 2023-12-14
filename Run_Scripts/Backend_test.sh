source ./Backend/.env
docker build -t backend ./Backend/
docker run --name backend --env-file ./Backend/.env -p $INTERNAL_PORT:$INTERNAL_PORT --network=mynetwork -d backend:latest
docker ps -a