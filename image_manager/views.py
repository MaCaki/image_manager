from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Welcome to the Proctor Institute Trachoma Grading Center.'
    )