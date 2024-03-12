#Description

For this project, we have three main components:
a home section, which requires a Raspberry Pi, and sensors are connected directly to the Raspberry Pi using Internet of Things (IoT) protocols or wired connections.
Secondly, we have a server section where we install RabbitMQ and Flask on servers.
We utilize RabbitMQ for data transmission and queuing, and Flask on the server side for client handling.
For ease of server configuration, we use Ansible.

For configuring RabbitMQ, you need to change the domain name you have considered for the server from the path ansible/inventory/main.yml.
Additionally, you need to modify the queue names, vhost name, username, and password from the path ansible/inventory/group_vars.

install rabbitmq on server :
```shell
ansible-playbook playbook/rabbitmq.yml 
```

