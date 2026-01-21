# Test Task — Docker + Nginx Reverse Proxy

This repository contains a solution for a test task that demonstrates:
- a tiny web service running behind an nginx reverse proxy,
- Docker Compose–based local setup,
- rate limiting and request ID handling,
- health checks,
- and a bonus Kubernetes (Kind + Ingress) deployment.

---

## TL;DR

```bash
cp .env.example .env
make up
make test
