# Arquitetura da Central Escolar

## Visão Geral

A Central Escolar é uma aplicação web desenvolvida para gerenciamento de demandas e eventos escolares.

A solução utiliza uma arquitetura cliente-servidor composta por:

* Frontend
* Backend
* Banco de Dados
* Infraestrutura Docker

---

# Arquitetura Geral

Frontend

↓

API FastAPI

↓

Serviços

↓

Banco SQLite

---

# Camada Frontend

Tecnologias:

* HTML5
* CSS3
* JavaScript

Responsabilidades:

* Exibir demandas cadastradas
* Exibir resumo das demandas
* Exibir eventos recebidos
* Permitir cadastro de novas demandas
* Permitir exclusão de demandas
* Consumir a API REST

Arquivo principal:

```text
frontend/index.html
```

Script principal:

```text
frontend/app.js
```

---

# Camada Backend

Tecnologia:

* FastAPI

Responsabilidades:

* Disponibilizar endpoints REST
* Processar requisições do frontend
* Validar dados recebidos
* Gerenciar demandas
* Gerenciar eventos
* Gerar resumos estatísticos

Arquivo principal:

```text
backend/app/main.py
```

---

# Camada de Serviços

Arquivo:

```text
backend/app/services.py
```

Responsabilidades:

* Normalização de status
* Construção de resumos
* Conversão de eventos em demandas

Função principal da Etapa 3:

```python
convert_event_to_demand()
```

Essa função recebe um evento e cria automaticamente os dados necessários para registrar uma nova demanda.

---

# Camada de Persistência

Arquivo:

```text
backend/app/database.py
```

Tecnologia:

* SQLite

Responsabilidades:

* Criar tabelas
* Inserir registros
* Atualizar registros
* Remover registros
* Consultar registros

---

# Modelo de Dados

## Tabela demands

Representa as demandas cadastradas.

Campos:

* id
* title
* category
* description
* status
* owner
* created_at

---

## Tabela events

Representa os eventos recebidos.

Campos:

* id
* source
* type
* value
* created_at

---

# Fluxo de Cadastro de Demanda

Usuário

↓

Frontend

↓

POST /demands

↓

Backend

↓

SQLite

↓

Resposta para o Frontend

---

# Fluxo de Evento

Evento

↓

POST /event

↓

Tabela events

↓

convert_event_to_demand()

↓

Nova demanda

↓

Tabela demands

↓

Atualização do frontend

---

# Endpoints Disponíveis

## Health Check

```text
GET /health
```

---

## Demandas

```text
GET /demands
POST /demands
PUT /demands/{id}
DELETE /demands/{id}
```

---

## Resumo

```text
GET /summary
```

---

## Eventos

```text
GET /events
POST /event
```

---

# Infraestrutura

Tecnologias utilizadas:

* Docker
* Docker Compose

Objetivos:

* Padronizar o ambiente de execução
* Facilitar implantação
* Garantir reprodutibilidade do projeto

Comando principal:

```bash
docker compose up --build
```

---

# Integração entre Componentes

Frontend

↓

API FastAPI

↓

Services

↓

Database

↓

SQLite

---

# Papel da Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio para:

* pesquisa técnica
* esclarecimento de dúvidas
* apoio na implementação
* revisão da documentação

A análise, validação e adaptação final da solução foram realizadas pelo aluno.

---

# Conclusão

A arquitetura adotada permite uma separação clara entre apresentação, regras de negócio e persistência de dados.

Essa organização facilita manutenção, evolução do sistema e implementação de novas funcionalidades, atendendo aos requisitos da Etapa 3 do Projeto de Extensão.