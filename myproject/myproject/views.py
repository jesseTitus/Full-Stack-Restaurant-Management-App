from django.http import HttpResponse

def handler404(request ,exception):
    return HttpResponse("<h1>404 : page not found!</h1>  <br><br><button onclick="" href='';""> Back")