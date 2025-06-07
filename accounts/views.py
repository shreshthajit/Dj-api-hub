from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

   # Form-based views (unchanged)
def register(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               login(request, user)
               messages.success(request, f'Welcome, {user.username}! Your account has been created.')
               return redirect('home')
           else:
               messages.error(request, 'Please correct the errors below.')
       else:
           form = CustomUserCreationForm()
       return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
       if request.method == 'POST':
           form = CustomAuthenticationForm(request, data=request.POST)
           if form.is_valid():
               user = form.get_user()
               login(request, user)
               messages.success(request, f'Logged in as {user.username}.')
               return redirect('home')
           else:
               messages.error(request, 'Invalid username or password.')
       else:
           form = CustomAuthenticationForm()
       return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
       logout(request)
       messages.success(request, 'You have been logged out.')
       return redirect('login')

@login_required
def home(request):
       return render(request, 'home.html', {'user': request.user})

def check_login(request):
       return render(request, 'accounts/check_login.html', {'is_authenticated': request.user.is_authenticated})

   # API views
class RegisterAPI(APIView):
       def post(self, request):
           serializer = RegisterSerializer(data=request.data)
           if serializer.is_valid():
               user = serializer.save()
               refresh = RefreshToken.for_user(user)
               return Response({
                   'user': UserSerializer(user).data,
                   'refresh': str(refresh),
                   'access': str(refresh.access_token),
               }, status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
       def post(self, request):
           username = request.data.get('username')
           password = request.data.get('password')
           user = authenticate(request, username=username, password=password)
           if user:
               refresh = RefreshToken.for_user(user)
               return Response({
                   'user': UserSerializer(user).data,
                   'refresh': str(refresh),
                   'access': str(refresh.access_token),
               }, status=status.HTTP_200_OK)
           return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPI(APIView):
       permission_classes = [IsAuthenticated]

       def post(self, request):
           try:
               refresh_token = request.data.get('refresh')
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
           except Exception as e:
               return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserAPI(APIView):
       permission_classes = [IsAuthenticated]

       def get(self, request):
           serializer = UserSerializer(request.user)
           return Response(serializer.data)