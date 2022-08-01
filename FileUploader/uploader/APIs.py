from rest_framework import status , generics
from rest_framework.views import APIView
from .serializers import CommonSerializer
from uploader.models import UploadedFile
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException

"""Default Permission : IsAuthenticatedOrReadOnly"""

class FileUplodaerAPI(APIView):
	def get(self , request):
		qs = UploadedFile.objects.all()
		serializer = CommonSerializer(qs , many=True)
		return Response(serializer.data)

class FileDeleteAPI(APIView):
	def get(self , request , pk):
		qs = get_object_or_404(UploadedFile , id=pk)
		serializer = CommonSerializer(qs , many=True)
		return Response(serializer.data)

	def delete(self , request , pk):
		qs = get_object_or_404(UploadedFile , id=pk)
		qs.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class NewFileAPI(generics.ListCreateAPIView):
	# def get(self , request):
	# 	qs = UploadedFile.objects.all()
	# 	serializer = CommonSerializer(qs , many=True)
	# 	return Response(serializer.data)

	# def post(self , request):
	# 	serializer = CommonSerializer(data=request.data)
	# 	serializer.is_valid(raise_exception=True)
	# 	"""this section not allowed to users change id and save somthing with that"""
	# 	if request.user.is_authenticated and serializer.data['user'] != request.user.id:
	# 		raise APIException("Error , You Can't Change Current User ID And Post Something")
	# 	else:
	# 		file = serilizer.data['file']
	# 		UploadedFile.objects.create(user=request.user.id , file=file , type='txt' , size = '100')
	# 	return Response(status=status.HTTP_200_OK)
	queryset = UploadedFile.objects.all()
	serializer_class = CommonSerializer