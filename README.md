# Teste Técnico – Desenvolvedor Fullstack CloudPark


## Descrição do Projeto

Este projeto é um **sistema de gestão de chamados internos** desenvolvido como parte do desafio técnico da CloudPark.

O sistema possui duas interfaces principais:

1. **Frontend Web (Django Template + Bootstrap)**: voltado para atendentes.
2. **Frontend SPA (Vue 3)**: voltado para técnicos.

O objetivo é permitir a abertura, listagem e gerenciamento de chamados internos, com regras de acesso diferentes para atendentes e técnicos.

---

## Funcionalidades

### 1. Autenticação

* Login por **e-mail e senha**
* Interfaces separadas:

  * Django Template para atendentes
  * Vue.js SPA para técnicos
* Autenticação via **JWT**

### 2. Cadastro de Chamados

* Abertura de chamados com os campos:

  * Título (obrigatório)
  * Descrição
  * Prioridade (Baixa / Média / Alta) (obrigatório)
  * Setor
  * Status (Aberto / Em Atendimento / Resolvido / Cancelado) (obrigatório)
* Chamado associado ao usuário que abriu

### 3. Listagem e Edição

* **Atendentes**: visualizam e editam chamados via Django Template
* **Técnicos**: visualizam e alteram status via SPA em Vue.js
* Atualizações **assíncronas** via Axios/Fetch no Vue

### 4. Regras do Sistema

* Apenas técnicos podem mudar o status para **Resolvido**
* Filtro por status disponível na interface
* Campos obrigatórios: título, prioridade e status

---

## Tecnologias Utilizadas

### Backend

* Python 3.10+
* Django 4+
* Django REST Framework
* SQLite

### Frontend

* **Atendente**: Django Templates + Bootstrap
* **Técnico**: Vue 3 + Axios/Fetch para consumo da API

### Outras Tecnologias

* Autenticação JWT
* Git com histórico limpo e commits claros

---

## Estrutura do Projeto

```text
├── Backend
│   ├── accounts/
│   ├── authentication/
│   ├── core/
│   ├── db.sqlite3
│   ├── frontend/
│   ├── manage.py
│   └── tickets/
├── README.md
└── vue_frontend/
```

> Estrutura resumida para facilitar visualização; pastas incluem modelos, views, serializers e templates.

---

## Instalação e Setup

## Rodando com Docker

Para subir todo o sistema rapidamente usando Docker e Docker Compose:

1. Certifique-se de ter Docker e Docker Compose instalados.
2. No diretório raiz do projeto, execute:

```
docker-compose up --build
```

Isso irá criar os containers para o backend e frontend, rodar as migrações, popular dados de exemplo e iniciar os servidores.

---

### Backend (Django)

1. Crie e ative um ambiente virtual:

```
cd Backend
python -m venv .venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Configure o banco e crie as tabelas:

```
python manage.py migrate
```

4. Popule dados de exemplo:

```
python manage.py mock_data
```

5. Crie um superusuário para acessar o admin:

```
python manage.py createsuperuser
```

6. Execute o servidor:

```
python manage.py runserver
```

### Frontend (Vue.js SPA)

1. Navegue até a pasta do frontend:

```
cd frontend
```

2. Instale dependências:

```
npm install
```

3. Execute a aplicação:

```
npm run server
```

A aplicação Vue irá consumir a API Django através do endpoint configurado.

---

## Considerações Finais

Este projeto demonstra:

* Habilidade em **Django + Django REST Framework**
* Consumo de API via **Vue 3 SPA**
* Controle de acesso e regras de negócio
* Organização de projeto fullstack com documentação clara
