<h2><u>Variações de Médias Móveis Simples (BRLBTC e BRLETH)</u></h2>

Requer 
Compile a imagem Docker executando o comando abaixo no mesmo local onde os arquivos são encontrados ```Dockerfile``` e ``` docker-compose.yml```

```
docker-compose build
```

```
docker-compose up
docker-compose up -d
```

Comando para executar o migrate
```
docker exec -it moving_average_change_web_1 python3 manage.py migrate
```

<h4>Rodar o Cron de Incremento Diário de Registros na Tabela</h4>

Verificar se o serviço de cron do container está ativo.

```bash
docker exec -it moving_average_change_web_1 service cron status
```

Caso esteja inativo, para rodar:

```bash
docker exec -it moving_average_change_web_1 service cron start
```

Depois que os serviço estiver ativo é necessário rodar o 
django-crontab para adicionar o cron no container.

```bash
docker exec -it moving_average_change_web_1 python3 manage.py crontab add
```

caso queira verificar se já existe um cron adicionado basta:

```bash
docker exec -it moving_average_change_web_1 python3 manage.py crontab show
```

<h4>Documentação das Apis</h4>
https://documenter.getpostman.com/view/6583936/TzmCgsxq

*Obs: Processo de carga inicial dos dados é acionado via POST.