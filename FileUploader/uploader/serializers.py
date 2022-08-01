from rest_framework import serializers
from uploader.models import UploadedFile

class CommonSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadedFile
		fields = '__all__'