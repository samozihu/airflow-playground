docker build . -f Dockerfile --pull --tag my-image:0.0.1

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up airflow-init

