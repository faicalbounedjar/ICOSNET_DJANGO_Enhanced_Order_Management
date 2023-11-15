from django.http import JsonResponse

def handle404(request,exception):
    message = ('path not found')
    response = JsonResponse(data={'error':message})
    response.status_code = 404
    return response

def handle500(request):
    message = ('internal server error')
    response = JsonResponse(data={'error':message})
    response.status_code = 500
    return response