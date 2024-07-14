# hacking.her-44: Futura Dev

O projeto é divido em três partes:

- Backend
- Web
- DB

Antes de mais nada, clone o repositório e navegue até sua pasta:

```bash
git clone https://github.com/mariana-santos/hacking.her-44 && cd hacking.her-44 
```

## Banco de dados

Certifique-se de ter o banco de dados <strong>MySQL</strong> na sua máquina. 
Feito isso, inicie o um banco com o usuário "root" e sem senha.

Rode os scripts de criação e inserção de dados na pasta "db"

## Back-end
Com tudo feito no banco de dados, navegue até a pasta da api

```bash
  cd api
```

E então rode o servidor local

```bash
  python -m uvicorn main:app --reload
```

## Front-end

Na pasta do projeto, navegue até a pasta "web"

```bash
cd web
```

Instale as dependências
```bash
npm install
```

Inicie o projeto localmente
```bash
npm run dev
```
