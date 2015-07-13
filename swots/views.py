from django.shortcuts import render, render_to_response, redirect, resolve_url
from django.http import HttpResponse
import simplejson as json

from .models import Diagram


def index(request):
    return render(request, 'swots/index.html')


def get_data(request):
    responses = Diagram.objects.order_by('-pub_date')
    responses = responses or [Diagram()]
    response_onj = []
    for response in responses:
        response_onj.append(dict(
            id=response.id or 0,
            title=response.title or 'New SWOT',
            strengths=response.strengths or [],
            weaknesses=response.weaknesses or [],
            opportunities=response.opportunities or [],
            threats=response.threats or []
        ))
    return HttpResponse(json.dumps(response_onj))


def modify(request, swot_id=None):

    if request.method.upper() == 'POST':
        print('CREATING')
        create_swot(json.loads(request.body))

    if request.method.upper() == 'DELETE' and swot_id:
        print('DELETING', swot_id)
        delete_swot(swot_id)

    if request.method.upper() in ['PUT', 'PATCH'] and swot_id:
        print('UPDATING', swot_id)
        modify_swot(json.loads(request.body), swot_id)

    return HttpResponse('success')


def create_swot(new_swot):
    print(new_swot)
    diagram = Diagram(**new_swot)
    diagram.save()


def modify_swot(swot_data, swot_id):
    print(swot_data)
    diagram = Diagram.objects.get(pk=swot_id)
    print(diagram)
    for field, value in swot_data.items():
        print(field, value)
        if hasattr(diagram, field):
            setattr(diagram, field, value)
    diagram.save()


def delete_swot(swot_id):
    diagram = Diagram.objects.get(pk=swot_id)
    diagram.delete()