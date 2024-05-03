
# Vault - PDV


Este projeto foi feito visando melhorar o armazenamento de produtos online para processos como dropshipping e diversos. Os dados estão armazenados em um servidor apache local, você pode criar o seu próprio usando o XAMPP.


## Tecnlogias utilizadas

**Front-end:** Html, CSS, Js, Bootstrap, Jquery

**Back-end:** Python, Flask

**Banco de Dados**: MySQL


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/lmaurici0/python-pdv.git
```

Entre no diretório do projeto

```bash
  cd python-pdv
```

Instale as dependências

```bash
  pip install pymsql, flask
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar criar variaveis de ambiente .env, se não tiver uma ainda você pode criar com 

```bash
python -m venv venv
cd venv 
scripts/activate
```


## Instalação

Por fim, para executa-lo você pode colar isto no terminal

```bash
    cd venv
    scripts/activate
    cd ../
    py main.py
```

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
