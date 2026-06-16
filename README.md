# OSINTNeoAiXL: Database Extraction Terminal 🕵️‍♂️

OSINTNeoAiXL is a production-grade, self-contained open-source Open Source Intelligence (OSINT) web portal designed to extract and audit municipal, environmental, and corporate contract anomalies across the United States.

## 🔗 Live Application
The live instance of this application is hosted publicly on Google Cloud Run:
👉 **[https://osint-chat-ui-xxl-941890989638.us-west1.run.app](https://osint-chat-ui-xxl-941890989638.us-west1.run.app)**

---

## 🛠️ Tech Stack & Architecture
- **Web UI**: Streamlit (Python)
- **Database**: Google BigQuery
- **Deployment**: Google Cloud Run (Dockerized Container)
- **Container Registry**: Artifact Registry

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/OSINTNeoAiJun/OSINTNeoAiXXL.git
cd OSINTNeoAiXXL
```

### 2. Configure Environment Variables
Export your Google Cloud credentials and project ID before running:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
export GCP_PROJECT_ID="your-gcp-project-id"
```

### 3. Install Dependencies & Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ How to Deploy to Google Cloud Run

To build and deploy the container directly to Cloud Run:
```bash
gcloud run deploy osint-chat-ui-xxl \
  --source . \
  --region us-west1 \
  --allow-unauthenticated \
  --project your-gcp-project-id
```

---

## 🔒 Security & Secrets Management
- The application retrieves database project mappings dynamically.
- Do not commit hardcoded API keys or Service Account JSON files to the repository.
- Use Google Cloud **Secret Manager** or **IAM Role Bindings** (such as assigning the `BigQuery Data Viewer` role to your Cloud Run Service Account principal) for authentication in production.

---

## ⚖️ Disclaimer
This is an OSINT research and audit visualization tool. Users are solely responsible for ensuring compliance with local laws, terms of service, and public data access regulations.
