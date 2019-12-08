#### запустить сервисы
sudo docker-compose up -d
#### войти в контейнер
sudo docker exec -it opencart_opencart_1 bash
#### получить информацию о пакетах
sudo apt update
#### установить openssh
sudo apt --yes install openssh-server
#### скопировать конфиг
sudo cp /etc/ssh/sshd_config  /etc/ssh/sshd_config.original
#### старт сервиса
sudo /etc/init.d/ssh restart
#### сменить пароль bitnami
passwd bitnami
#### залогиниться по ssh
sudo ssh -l bitnami -p 1022 localhost
