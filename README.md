# 📦 Database Migration & Application Run Guide

## 🚀 Run Database Migration

### ➕ Create a Migration

```bash
poetry run alembic revision --autogenerate -m "your_migration_name"
```

### 📥 Apply the Migration

```bash
poetry run alembic upgrade head
```

## ▶️ Run the Application

### 1.

```bash
poetry install
```

### 2.

```bash
poetry run start
```
