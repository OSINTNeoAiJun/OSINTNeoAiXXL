# OSINTNeoAiXXL Deployment & Query Audit Walkthrough 🚀

We have deployed your brand new, independent XXL environment, created the missing audit infrastructure, and executed the forensic queries.

## 🔗 Live URLs

1. **Original Extraction Terminal (XL)**:
   - URL: [https://osint-chat-ui-941890989638.us-west1.run.app](https://osint-chat-ui-941890989638.us-west1.run.app)
2. **New Independent XXL Terminal**:
   - URL: [https://osint-chat-ui-xxl-941890989638.us-west1.run.app](https://osint-chat-ui-xxl-941890989638.us-west1.run.app)

---

## 🛠️ Infrastructure Fixed (Missing Audit Tables)

We successfully executed the DDL scripts to create the missing infrastructure in project `noble-beanbag-497411-m4`:
- Created `noble-beanbag-497411-m4.national_audits.ingestion_audit_trail`
- Created `noble-beanbag-497411-m4.national_audits.city_council_minutes`

---

## 🔍 Huntington Beach Extraction (Nested UNNEST Query)

To target the nested `environmental_site_assessments` array, we resolved the schema column mapping (using `a.state` instead of `a.state_code` to match the target database schema):

```sql
SELECT a.state, env.location_name, env.contaminant_type, env.test_multiplier 
FROM `noble-beanbag-497411-m4.national_audits.all_state_records` a, 
UNNEST(a.environmental_site_assessments) env 
WHERE LOWER(env.location_name) LIKE '%huntington%' OR LOWER(env.location_name) LIKE '%beach%';
```

*Note: Since the local database currently has empty `environmental_site_assessments` arrays across the test rows, this query will evaluate successfully with 0 rows returned until fresh Huntington Beach environmental payloads are ingested.*
