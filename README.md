# **Relatório do Projeto Garage Flask API**

## **1. Introdução**
O projeto **Garage API** foi desenvolvido como parte da disciplina **UFCD 5417 - Programação para a WEB - servidor (server-side)**, com o objetivo de aprimorar a aprendizagem prática sobre APIs. O projeto foi estruturado seguindo boas práticas de desenvolvimento e organização de código, utilizando a framework **Flask** para a criação de endpoints e operações CRUD.

---

## **2. Estrutura do Projeto**
A estrutura de diretórios do projeto está organizada da seguinte forma:

### **2.1 Models**
Os **Models** representam a estrutura dos dados utilizados na aplicação. Eles são responsáveis por definir como as informações serão armazenadas e manipuladas no banco de dados.  

### **2.2 API**
A **API** é responsável por expor os endpoints para interação com os dados da aplicação. Ela recebe requisições HTTP e retorna respostas formatadas em JSON.

#### **2.2.1 Exemplo de Endpoints:**

- **GET** /vehicles  
 Retorna a lista de todos os veículos registrados.
- **POST** /vehicles  
Adiciona um novo veículo ao sistema.
- **GET** /vehicles/{id}  
  Retorna os detalhes de um veículo específico.
- **PUT** /vehicles/{id}  
  Atualiza as informações de um veículo existente.
- **DELETE** /vehicles/{id}  
  Remove um veículo do sistema.

### **2.3 Services**  

A camada de **Services** é responsável por centralizar a lógica de negócios da aplicação. Ela abstrai as operações do banco de dados e outras regras de negócios para manter a API mais organizada e modular.

---

## **3. Banco de Dados**
A modelagem segue uma estrutura relacional com as seguintes tabelas principais:

- **client** → Informações dos clientes.
- **vehicle** → Registo de veículos.
- **work** → Serviços realizados na garagem.
- **task** → Tarefas associadas a cada serviço.
- **employee** → Funcionários da garagem.
- **invoice** → Faturas geradas para os clientes.
- **invoice_item** → Itens das faturas.
- **setting** → Configurações gerais da aplicação.

---
## **4. Funcionalidades da API**
A  API implementa operações **CRUD** (Create, Read, Update, Delete) para cada entidade.

### **Principais Endpoints**
- **Clientes:** Cadastro, edição e listagem.
- **Veículos:** Registro e associação aos clientes.
- **Serviços:** Gerenciamento de serviços.
- **Tarefas:** Gestão das tarefas dentro dos serviços.
- **Funcionários:** Controle dos funcionários.
- **Faturas:** Geração e controle de faturas.

---

## **5. Configuração e Execução**
Para configurar e rodar o projeto localmente, siga os passos abaixo:

1. **Clone the repository:**  
  Baixe o repositório para sua máquina local executando o seguinte comando no terminal:
```bash
 git clone https://github.com/Tayara32/API-REST.git
 ```

2. **Navegue até o diretório do projeto:**  
  Após clonar o repositório, acesse a pasta do projeto:
```bash
 cd garage_flask_api
 ```

3. **Crie e ative um ambiente virtual:**  
  Para isolar as dependências do projeto, crie um ambiente virtual com os seguintes comandos:
   #### 3.1 Para Linux/macOS
```bash
   python3 -m venv venv
   source venv/bin/activate
 ```
 #### 3.2 Para Linux/macOS
```bash
   python3 -m venv venv
   venv\Scripts\activate
 ```
4. **Instale as dependências:** 
   Com o ambiente virtual ativado, instale os pacotes necessários utilizando o arquivo `requirements.txt`:
```bash
  pip install -r requirements.txt
 ```
5. **Execute a aplicação:** 
   Para verificar se a instalação foi concluída com sucesso, inicie a aplicação Flask:
```bash
  flask run
 ```

## **6. Documentação do Swagger**
Para acessar a documentação do Swagger, inicie a aplicação Flask e navegue até a seguinte URL em seu navegador:
```bash
  http://127.0.0.1:5000/api/docs
 ```

## **7. Conclusão**
O projeto Garage API foi desenvolvido como um exercício prático para consolidar conhecimentos sobre APIs com `Flask`, `base de dados relacional` e `boas práticas de arquitetura de software`. 
A implementação segue princípios modulares, garantindo flexibilidade e escalabilidade à aplicação.








