import os
import json
from google.cloud import bigquery
from google import genai

gcp_project_id = os.environ.get("GOOGLE_PROJECT_ID", "project-743aab84-f9a5-4ec7-954")
client = bigquery.Client(project=gcp_project_id)

query = f"""
    SELECT state_code, non_profiteers_index 
    FROM `{gcp_project_id}.national_audits.all_state_records`
"""

results = client.query(query).result()
all_data = []

for row in results:
    for item in row.non_profiteers_index:
        all_data.append({
            "state_code": row.state_code,
            "organization_name": item.get("organization_name", ""),
            "cms_billing_code": item.get("cms_billing_code", ""),
            "unaccounted_fund_delta": item.get("unaccounted_fund_delta", 0.0)
        })

print("Fetched records:", len(all_data))

prompt = f"""
You are OSINTNeoAiXXL, an advanced forensic audit AI.
Analyze the following database records of anomalous organizations and unaccounted funds.
For each record or group of records, identify the likely crimes, applicable statutes (e.g. 18 U.S.C. § 1343 - Wire Fraud, False Claims Act), explicitly named individuals if any, and evidence links (use placeholder links if actual links are missing, e.g. [Evidence File A](evidence.pdf)).
Provide a FULL FORENSIC AUDIT REPORT in Markdown format.

Records:
{json.dumps(all_data, indent=2)}

Ensure the output is strictly Markdown format.
"""

ai_client = genai.Client(vertexai=True, project=gcp_project_id, location="us-central1")
response = ai_client.models.generate_content(
    model="gemini-1.5-pro",
    contents=prompt
)

with open("audit_report.md", "w") as f:
    f.write(response.text)

print("Saved audit_report.md")
