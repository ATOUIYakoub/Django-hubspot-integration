import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

HUBSPOT_ACCESS_TOKEN = os.getenv('HUBSPOT_ACCESS_TOKEN')

def format_datetime_fields(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            elif isinstance(value, dict):
                format_datetime_fields(value)
            elif isinstance(value, list):
                for item in value:
                    format_datetime_fields(item)
    return data

def fetch_hubspot_leads():
    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def post_hubspot_lead(lead_data):
    url = 'https://api.hubapi.com/crm/v3/objects/contacts'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {HUBSPOT_ACCESS_TOKEN}"
    }
    lead_data = format_datetime_fields(lead_data)
    response = requests.post(url, json={'properties': lead_data}, headers=headers)
    if response.status_code != 201:
        print(f"Error: {response.json()}")
    return response

def update_hubspot_lead(lead_id, lead_data):
    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{lead_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {HUBSPOT_ACCESS_TOKEN}"
    }
    lead_data = format_datetime_fields(lead_data)
    response = requests.patch(url, json={'properties': lead_data}, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.json()}")
    return response

def delete_hubspot_lead(lead_id):
    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{lead_id}'
    headers = {
        'Authorization': f"Bearer {HUBSPOT_ACCESS_TOKEN}"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code != 204:
        print(f"Error: {response.json()}")
    return response