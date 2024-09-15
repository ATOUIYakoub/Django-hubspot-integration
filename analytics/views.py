import os
import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LeadSerializer
from .hubspot import fetch_hubspot_leads, post_hubspot_lead, update_hubspot_lead, delete_hubspot_lead
from drf_spectacular.utils import extend_schema

@extend_schema(
    responses={200: LeadSerializer(many=True)},
    description="Fetch leads from HubSpot"
)
@api_view(['GET'])
def get_hubspot_leads(request):
    leads = fetch_hubspot_leads()
    if leads is not None:
        return JsonResponse({'results': leads['results']}, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch leads from HubSpot'}, status=500)

@extend_schema(
    request=LeadSerializer,
    responses={201: LeadSerializer},
    description="Post a new lead to HubSpot"
)
@api_view(['POST'])
def post_hubspot_lead_view(request):
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        lead_data = serializer.validated_data['properties']
        response = post_hubspot_lead(lead_data)
        if response.status_code == 201:
            return Response({'results': [serializer.data]}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to post lead to HubSpot', 'details': response.json()}, status=response.status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=LeadSerializer,
    responses={200: LeadSerializer},
    description="Update an existing lead in HubSpot"
)
@api_view(['PUT'])
def update_hubspot_lead_view(request, pk):
    serializer = LeadSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        lead_data = serializer.validated_data.get('properties', {})
        response = update_hubspot_lead(pk, lead_data)
        if response.status_code == 200:
            return Response({'results': [lead_data]}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to update lead in HubSpot', 'details': response.json()}, status=response.status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    responses={204: None},
    description="Delete a lead from HubSpot"
)
@api_view(['DELETE'])
def delete_hubspot_lead_view(request, pk):
    response = delete_hubspot_lead(pk)
    if response.status_code == 204:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Failed to delete lead from HubSpot', 'details': response.json()}, status=response.status_code)