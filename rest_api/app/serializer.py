from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    model = BooksModel
    feilds = "__all__"