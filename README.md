# 🧾 API de Clientes e Pedidos

Um sistema simples de gestão de clientes e pedidos desenvolvido com **Django REST Framework**. Essa API permite cadastrar clientes, registrar pedidos vinculados a cada cliente e realizar autenticação via JWT.

Ideal para pequenas empresas que desejam automatizar processos comerciais de forma leve e eficiente.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (banco de dados padrão)
- **JWT** (JSON Web Tokens para autenticação)
- **DRF Serializers**

---

## 📦 Funcionalidades

- [x] CRUD de Clientes
- [x] CRUD de Pedidos  
- [x] Autenticação com JWT
- [x] Interface de navegação DRF
- [x] Organização com Serializers

---

## 🗂️ Estrutura do Projeto

```
customer_and_order_api/
├── app/              # Configurações do projeto
├── authentication/   # Módulo de autenticação
├── customers/        # Módulo de clientes
├── orders/           # Módulo de pedidos
├── manage.py
└── requirements.txt
```

---

## 🔐 Autenticação

A API utiliza autenticação JWT através do pacote `djangorestframework-simplejwt`.

### 📥 Obter Token de Acesso

```http
POST /api/v1/authentication/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### 🔄 Atualizar Token de Acesso

```http
POST /api/v1/authentication/token/refresh/
Content-Type: application/json

{
  "refresh": "token_refresh_aqui"
}
```

### 🔐 Cabeçalho para Autenticação

```http
Authorization: Bearer seu_token_de_acesso
```

---

## 📋 Endpoints da API

### Clientes

| Método | Endpoint              | Descrição                |
|--------|-----------------------|--------------------------|
| GET    | `/api/v1/customers/`  | Lista todos os clientes  |
| GET    | `/api/v1/customer/1/` | Detalha um cliente       |
| POST   | `/api/v1/customers/`  | Cria novo cliente        |
| PATCH  | `/api/v1/customer/1/` | Atualiza cliente         |
| PUT    | `/api/v1/customer/1/` | Atualiza cliente         |
| DELETE | `/api/v1/customer/1/` | Remove cliente           |

### Pedidos

| Método | Endpoint            | Descrição                |
|--------|---------------------|--------------------------|
| GET    | `/api/v1/orders/`   | Lista todos os pedidos   |
| GET    | `/api/v1/order/1/`  | Detalha um pedido        |
| POST   | `/api/v1/orders/`   | Cria novo pedido         |
| PATCH  | `/api/v1/order/1/`  | Atualiza pedido          |
| PUT    | `/api/v1/order/1/`  | Atualiza pedido          |
| DELETE | `/api/v1/order/1/`  | Remove pedido            |

---

## 🚀 Como Rodar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/leonardofgc/customer_and_order_api.git
cd customer_and_order_api
```

### 2. Crie o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Rode o servidor
```bash
python manage.py runserver
```

A API estará disponível em: `http://127.0.0.1:8000/`

---

## 📝 Exemplo de Uso

### Criando um Cliente
```http
POST /api/v1/customers/
Authorization: Bearer seu_token_aqui
Content-Type: application/json

{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "11999999999"
}
```

### Criando um Pedido
```http
POST /api/v1/orders/
Authorization: Bearer seu_token_aqui
Content-Type: application/json

{
  "customer": 1,
  "description": "Pedido de produtos eletrônicos",
  "value": 1500.00
}
```

---

## 📌 Autor

**Leonardo Guimarães**  
Backend Developer | PHP • Python • SQLite • APIs RESTful

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.