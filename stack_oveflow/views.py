from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .serializers import QuestionSerializer
from .models import Questions
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def questions_list(req):

    if req.method == "GET":
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif req.method == "POST":
        data = JSONParser().parse(req)
        serializer = QuestionSerializer(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def questions_info(req, pk):

    try :
        question = Questions.objects.get(pk=pk)
    except Questions.DoesNoExist:
        return HttpResponse(status=404)

    if req.method == "GET":
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)

