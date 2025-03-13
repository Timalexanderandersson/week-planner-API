from django.http import JsonResponse 


#message for api
def views_api(request):
    return JsonResponse({"message": "this is task api"})