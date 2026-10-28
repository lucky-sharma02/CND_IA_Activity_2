# Containerization & Kubernetes Deployment Challenge

**Author:** Lucky Sharma  
**Course:** Cloud Native DevOps / Cloud Computing  

A cloud-native demonstration deploying a lightweight, optimized Python web application to a Kubernetes cluster with multi-replica load balancing, resource governance, and health probes.

---

## Architecture & Implementation Overview

- **Base Image:** `python:3.11-slim` for a minimal vulnerability attack surface and fast build times.
- **Security:** Strict principle of least privilege using an unprivileged non-root user (`appuser`).
- **Orchestration:** Managed via Kubernetes `Deployment` maintaining 3 replicas for high availability.
- **Reliability:** Liveness and Readiness probes configured against the `/healthz` endpoint.
- **Resource Management:** Explicit CPU and Memory requests and limits applied to prevent node contention.
- **Service Networking:** Managed via `Service` targeting pod labels, enabling seamless internal cluster communication and external exposure via `NodePort`.

---

## Project Structure

```text
.
├── .dockerignore
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
└── k8s/
    ├── deployment.yaml
    └── service.yaml
