# patient-communications-service

patient-communications-service — domain: patients

- **Port:** 8109
- **Language:** Python 3.11 + Flask
- **Database:** `patients` (Postgres, table `patient_communications`)
- **Event bus:** Kafka

## API

| Method    | Path                       |
|-----------|----------------------------|
| GET       | `/api/patient_communications/`          |
| POST      | `/api/patient_communications/`          |
| GET       | `/api/patient_communications/<id>`      |
| PUT/PATCH | `/api/patient_communications/<id>`      |
| DELETE    | `/api/patient_communications/<id>`      |
| GET       | `/health`                  |
| GET       | `/ready`                   |

## Events

**Publishes:** (none)
**Subscribes:** patient.created

## HTTP peer dependencies

- `patients-service`
- `notifications-service`
- `audit-log-service`

## Local dev

```bash
pip install -e ../../libs/py-healthcare-common
pip install -r requirements.txt
cp .env.example .env
(cd ../../infra && docker compose up -d postgres kafka kafka-init)
python -m app.main
```

## Tests

```bash
pytest
```
