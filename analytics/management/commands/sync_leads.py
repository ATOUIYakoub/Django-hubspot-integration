from django.core.management.base import BaseCommand
from analytics.models import Lead
from analytics.hubspot import fetch_hubspot_leads

class Command(BaseCommand):
    help = 'Sync leads from HubSpot API'

    def handle(self, *args, **kwargs):
        leads_data = fetch_hubspot_leads()

        if leads_data:
            for lead_data in leads_data['results']:
                Lead.objects.update_or_create(
                    hubspot_id=lead_data['id'],
                    defaults={
                        'name': f"{lead_data['properties']['firstname']} {lead_data['properties']['lastname']}",
                        'email': lead_data['properties']['email'],
                        'phone': lead_data['properties'].get('phone'),
                        'company': lead_data['properties'].get('company'),
                        'lead_status': lead_data['properties'].get('lead_status'),
                        'created_at': lead_data['properties']['createdate'],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully synced leads'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch leads from HubSpot'))
