from django.http import JsonResponse 

def views_api(request):
    return JsonResponse({"message": "this is task api"})