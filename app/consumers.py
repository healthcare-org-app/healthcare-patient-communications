"""Kafka consumers for patient-communications-service.

One handler per subscribed topic. Real handlers write to this service's own
database and/or publish follow-up events; stub handlers just log + audit.
"""
from __future__ import annotations

import logging

from psycopg.types.json import Json

from healthcare_common.audit import emit_audit

log = logging.getLogger("patient-communications-service.consumers")

TABLE = "patient_communications"


def register(svc) -> None:
    bus = svc.bus
    db = svc.db
    clients = svc.clients

    @bus.on("patient.created")
    def _on_patient_created(envelope: dict) -> None:
        data = envelope.get("data") or {}
        try:
                    pid = data.get("id")
                    if not pid: return
                    # Onboarding message.
                    bus.publish("notification.requested", key=str(pid),
                                value={"patient_id": pid, "subject": "Welcome!",
                                       "source": "patient-communications-service"})
        except Exception as e:
            log.exception("patient-communications-service/patient.created handler failed: %s", e)
        emit_audit(bus, action="consume.patient.created", actor="system:patient-communications-service",
                   target=None, details={"envelope_id": envelope.get("id")})

