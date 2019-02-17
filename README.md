# API FACE RECOGNITION

# 1a Crie o ambiente da amplicação:

* pip install venv
* python3 -m venv venv
* . venv/bin/activate (Para ativar o ambiente)
* deactivate (Para desativar o ambiente)


# 2a Instale as bibliotecas dependentes:

* sudo apt-get update -y
* sudo apt-get install build-essential cmake
* sudo apt-get install libgtk-3-dev
* sudo apt-get install libboost-all-dev


# 3a Instale os modulos Python do projeto

* pip install wheel setuptools
* pip install -r requirements.txt


# 5a Instale o MongoDB para a aplicação

* sudo apt-get install mongodb


# 6a Execute o script que cria a coleção necessária no MongoDB para a aplicação

* python utils/create_database.py


# 4a Suba o servidor da API

* python api.py


## Uso da API

# Para cadastrar um usuário:

* Faça uma requisição POST em 'localhost:5000/api/register' passando o json com um identificador do usuário, pode ser o CPF

```json
{"_id": "015.698.794-95"}
```

# Para inserir imagens a serem treinadas 

* Faça uma requesição POST em 'localhost:5000/api/insert' passando o json com um identificador do usuário, pode ser o CPF, e o diretório temporario com as imagens. A API as copiará para a pasta devida em './dataset'

```json
{
    "_id": "058.694.891-58",
    "path_files": [
        "/home/login/temporaria/aluno1/001.jpg",
        "/home/login/temporaria/aluno1/002.jpg",
        "/home/login/temporaria/aluno1/003.jpg",
        "/home/login/temporaria/aluno1/004.jpg"
    ]
}
```

# Para solicitar uma ação de treinamento

* Faça uma requesição POST em 'localhost:5000/api/train' passando o json com um identificador do usuário, pode ser o CPF, e o método de treinamento a ser utilizado [cnn ou hog], recomendado 'cnn'.

```json
{
    "_id": "016.748.612-58",
    "method_training": "cnn"
}
```

Após o core da API realizar o treinamento ela salvará o modelo em './model' em um arquivo específico e individual de cada aluno.

o JSON  de resposta será:
```json
{
    "status": "sucess",
    "_id": "a2e63ee01401aaeca78be023dfbb8c59",
    "model_id": "w8y63ee01401aaeca78be023dfbb8f71.pickle",
    "datetime": "2019-02-15 20:04:09",
    "time_training": "0:03:06.827312"
}
```

# Para autenticar o login de um usuário

* Faça uma requesição POST em 'localhost:5000/api/login' passando o json com um identificador do usuário, pode ser o CPF, e o diretório da imagem a ser comparada, em caso de login aprovado a imagem será inserida no dataset automaticamente, e o core da API retornará o seguinte:

```json
{
    "_id": "",
    "status": "sucess",
    "authorized": "authorized"
}
```

Request:
```json
{
    "_id": "a2e63ee01401aaeca78be023dfbb8c59",
    "image": "/home/guilherme/_temporaria"
}
```

## Observações:

* Veja exemplos de requests e responses de json em ./test_utils/examples