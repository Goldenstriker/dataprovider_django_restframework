from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import response
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse

def index(request):
	#userlist = User.objects.all().select_related('userprofile')
	res = ""
	userlist = User.objects.all().select_related('userprofile')
	#res = u.userprofile.is_online
	for user in userlist:
		print(user.userprofile.is_online)
		#res = res + user.first_name
	return HttpResponse("First Web Response"+ res)

# Create your views here.


# Create your views here.
def home(request):
    return render(request, 'main/index.html')

from django.shortcuts import render
from django.http import response

# Create your views here.
def home(request):
    return render(request, 'main/index.html')



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class RegisterUserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def current_user(request):
    user = request.user
    return JsonResponse({'user':user.username })







