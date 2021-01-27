from django.shortcuts import render
from django.http import JsonResponse
# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
# library
from api.lib.face_compare import ImageProcessing


@api_view(['POST'])
def check_face(request):
    result = ImageProcessing.face_comparison(data=request.data)
    json_result = {"result": result[0]}
    return Response(json_result)
