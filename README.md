# Tiny Web Service behind Nginx Reverse Proxy

This repository contains a minimal web service running behind an Nginx reverse proxy.
It supports a **mandatory Docker Compose setup** and a **bonus Kubernetes (Kind + Ingress) setup**.

---

## 1. Prerequisites

### Mandatory
- Docker (Docker Desktop)
- Docker Compose
- Make

### Bonus (Kubernetes)
- kind
- kubectl
- helm (optional)

---

## 2. How to Run (Docker Compose)

### 2.1 Environment configuration

Copy the example env file and adjust values if needed:

```bash
cp .env.example .env
