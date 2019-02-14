O sistema de reconhecimento facial é dividido em 3 partes.

* 1a Passo: 

Primeiro precisamos ter um dataset das faces da pessoa a ser reconhecida. Neste sistema o script
build_face_dataset.py abre a webcam para poder capturar imagens da pessoa. 


## Como executar.

$ python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/FULANO

haarcascade_frontalface_default.xml: arquivo do modelo de faces pré treinado
dataset/FULANO/: diretorio onde serão salvos as imagens.
[ATENÇÃO]: CADA PESSOA A SER RECONHECIDA DEVE TER UMA PASTA COM SEU NOME, PARA O LAB RECOMENDO SALVAR COM O ID DO BANCO DE DADOS E SALVAR O PATH DO DATASET EM UMA TABELA 

PRECIONA A TELA K EM EXECUÇÃO PARA SALVAR A IMAGEM DAQUELE INSTANTE DA WEBCAM NO DIRETORIO PASSADO

2a Passo:

Agora necessário codificar as faces coletadas.

##Como executar.

$ python3 decodificador_faces.py --dataset dataset/ --encodings encodings/encodings.pickle --detection-method cnn
ou
$ python3 decodificador_faces.py --dataset dataset/ --encodings encodings/encodings.pickle --detection-method hog

dataset/: dataset das faces
encodings.pickle: local do arquivo que sera gerado apartir das decodificações
cnn ou hog: metodo usado na rede neural, fazer teste pra saber o melhor a ser usado. Recomendo o cnn, é mais preciso.
[ATENÇÃO]: PARA MELHOR VELOCIDADE RECOMENDO MONTAR UM ARQUIVO PICLE PARA CADA ALUNO DO LAB COM O ID DELE NO NOME DE ARQUIVO E GUARDE SEU PATH EM UM BANCO DE DADOS
3a Passo:

Por fim executar e fazer o teste

##Como executar.

$ python3 main.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

------------------- [ATENÇÃO] -----------------------
Este projeto possui dependencias antes de executar instale elas usando:

$ pip3 install -r requirements.txt

Caso dê erro instale as bibliotecas dlib e face_recognition manualmente


NECESSARIO FAZER ADAPTAÇÕES PARA TORNAR ÚTIL AO PROJETO, NÃO É NECESSÁRIO DAR RETORNO DE VÍDEO, SOMENTE PROCESSAR E RETORNAR UM JSON
