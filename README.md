# Aurora API

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-black)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](pyproject.toml)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**API com autenticacao, trilhas de auditoria e relatorios prontos para o time de ops**

Dominio: `fintech / ledger`. Problema de partida: times financeiros perdem horas reconciliando lancamentos manuais e sem auditoria.

## What recruiters should notice

- API versionada (`/api/v1`) com contrato OpenAPI gerado.
- Autenticacao JWT, CORS, healthcheck e persistencia SQLAlchemy.
- Testes de autenticacao + CRUD, CI no GitHub Actions, Docker Compose.
- Documentacao de arquitetura em `/docs` — nao e um CRUD jogado no README.

## Stack

FastAPI · Pydantic Settings · SQLAlchemy 2 · JWT · Pytest · Docker · GitHub Actions

## Quick start

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Login de demo: `demo` / `demo123`.

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"demo123"}'
```

Docs interativas: `http://127.0.0.1:8000/docs`

## Tests

```bash
pytest -q
```

## Docker

```bash
docker compose up --build
```

## Roadmap

- [ ] Postgres + Alembic
- [ ] RBAC por papel (ops / finance / admin)
- [ ] Webhook de auditoria
