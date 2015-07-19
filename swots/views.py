from django.shortcuts import redirect
from django.http import HttpResponse
import simplejson as json
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Diagram


@ensure_csrf_cookie
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

@ensure_csrf_cookie
def modify(request, swot_id=None):
    if request.method.upper() == 'GET':
        print('GET')
        return redirect('/')

    if request.method.upper() == 'DELETE' and swot_id:
        print('DELETING', swot_id)
        delete_swot(swot_id)
        return HttpResponse(json.dumps(dict(status='success')))

    if request.method.upper() == 'POST':
        print('CREATING')
        swot_id = create_swot(json.loads(request.body))

    if request.method.upper() in ['PUT', 'PATCH'] and swot_id:
        print('UPDATING', swot_id)
        modify_swot(json.loads(request.body), swot_id)

    return HttpResponse(json.dumps(dict(id=swot_id, status='success')))


def create_swot(new_swot):
    print(new_swot)
    diagram = Diagram(**new_swot)
    diagram.save()
    return diagram.id


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