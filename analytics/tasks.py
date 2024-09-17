from celery import shared_task
from .hubspot import delete_hubspot_lead

@shared_task
def delete_hubspot_lead_task(lead_id):
    response = delete_hubspot_lead(lead_id)
    if response.status_code == 204:
        return {'status': 'success', 'message': 'Lead deleted successfully'}
    else:
        return {'status': 'error', 'message': 'Failed to delete lead', 'details': response.json()}