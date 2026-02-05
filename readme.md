# TryMe — Virtual Try‑On Platform

TryMe is a **modular, API‑first virtual try‑on platform** designed to power Shopify stores, browser extensions, mobile apps, and future third‑party integrations.

The goal is simple:

> **One try‑on engine. Many surfaces. No platform lock‑in.**

---

## 🧠 High‑Level Architecture

At the center of the system is the **API Core (AI Orchestration Layer)**. Every client — Shopify, Chrome extension, mobile app — talks to this service.

```
Clients (UI)
│
├─ Shopify App
├─ Chrome Extension
├─ Mobile App
└─ Future 3rd‑party apps
        │
        ▼
API Core (Fastify + TypeScript)
│
├─ Identity / Avatar Module
├─ Try‑On Pipeline
├─ AI Integration (Gemini / Nano Banana)
└─ Billing & Quotas (future)
```

---

## 📁 Repository Structure

```
TryMe/
├─ backend/
│  ├─ apps/
│  │  ├─ api-core/          # AI orchestration backend
│  │  ├─ shopify-app/       # Shopify app (UI + billing)
│  │  ├─ chrome-extension/  # Browser try‑on
│  │  └─ mobile-app/        # Mobile client
│  │
│  ├─ packages/             # Shared logic (prompts, types, SDKs)
│  ├─ tsconfig.json
│  └─ package.json
│
└─ .gitignore
```

### Key principles

* **`apps/`** → deployable products
* **`packages/`** → shared, reusable logic
* **API Core is standalone** — not Shopify‑dependent

---

## 🚀 API Core

The API Core is built with:

* **Node.js (ESM)**
* **TypeScript (strict)**
* **Fastify**

### Current status

* ✅ ESM + TypeScript bootstrap complete
* ✅ Modular routing structure
* 🚧 `/tryon` API under active development

---

## 🔌 Core Endpoint (WIP)

Planned primary endpoint:

```
POST /tryon
```

**Input (planned)**

```json
{
  "avatarId": "uuid",
  "garmentImageUrl": "https://...",
  "style": "studio | lifestyle | runway"
}
```

**Output (planned)**

```json
{
  "imageUrl": "https://...",
  "creditsUsed": 1
}
```

This endpoint will be reused by **all clients**.

---

## 🤖 AI Stack

* **Image segmentation**: Gemini 2.5 Flash
* **Image synthesis**: Nano Banana (Gemini Image)
* **Future video try‑on**: Veo (drop‑in replacement)

The architecture is intentionally designed so that **image → video** is an internal swap, not a rewrite.

---

## 🔐 Privacy‑First Avatars (Planned)

User avatars will be stored as:

* Encrypted image embeddings
* Optional raw image deletion
* Vector‑based retrieval (Pinecone / similar)

This minimizes sensitive data exposure while enabling high‑quality try‑ons.

---

## 🛠 Local Development

### Requirements

* Node.js 20+
* npm

### Run API Core

```bash
cd backend
npm install
npm run dev
```

Server will start at:

```
http://localhost:3000
```

---

## 🧭 Roadmap

* [ ] Zod schemas for `/tryon`
* [ ] Nano Banana integration
* [ ] Avatar storage + embeddings
* [ ] Shopify App Proxy integration
* [ ] Chrome Extension MVP
* [ ] Public API access

---

## 📌 Philosophy

* API‑first
* Platform‑agnostic
* Modular by default
* Privacy‑aware
* Built to scale beyond Shopify

---

## 📄 License

MIT (TBD)
