#!/usr/bin/env python3
"""Register schemas and demonstrate compatibility checks with Schema Registry"""
import json
import requests
from pathlib import Path

SCHEMA_REGISTRY = "http://localhost:8081"
SUBJECT = "users-value"

def read_schema(path):
    return Path(path).read_text()


def register_schema(schema_str):
    url = f"{SCHEMA_REGISTRY}/subjects/{SUBJECT}/versions"
    payload = {"schema": schema_str}
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()


def set_compatibility(mode="BACKWARD"):
    url = f"{SCHEMA_REGISTRY}/config/{SUBJECT}"
    payload = {"compatibility": mode}
    r = requests.put(url, json=payload)
    r.raise_for_status()
    return r.json()


if __name__ == '__main__':
    print("Setting compatibility to BACKWARD for subject:", SUBJECT)
    print(set_compatibility())

    print("Registering v1 schema...")
    s1 = read_schema("schemas/user_v1.avsc")
    print(register_schema(s1))

    print("Registering v2 schema (compatible evolution)...")
    s2 = read_schema("schemas/user_v2.avsc")
    try:
        print(register_schema(s2))
    except requests.HTTPError as e:
        print("Failed to register v2:", e.response.text)
        raise

    print("Done.")
