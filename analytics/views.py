from rest_framework import viewsets
from django.http import JsonResponse
from .models import Lead, Interaction
from .serializers import LeadSerializer, InteractionSerializer
from .hubspot import fetch_hubspot_leads

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

def get_hubspot_leads(request):
    leads = fetch_hubspot_leads()
    if leads is not None:
        return JsonResponse(leads, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch leads from HubSpot'}, status=500)