from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
# Create your views here.
from account.models import AuthUser
from datetime import datetime


class Join(APIView):
    def get(self, request):
        return render(request, "account/join.html") # Join 들어오면 화면으로 여길 보여줘라!!

    def post(self, request):
        # TODO 회원가입
        id = request.data.get('id')
        email = request.data.get('email')
        relationship = request.data.get('relationship')
        name = request.data.get('name')
        password = request.data.get('password')
        #birth = request.data.get('birth')
        #phonenumber = request.data.get('phonenumber')
        #gender = request.data.get('gender')
        member_type = request.data.get('member_type')   # 1관리자 2보호자

        user_id = request.data.get('user_id')

        AuthUser.objects.create(id=id,
                                password=password,
                                relationship=relationship,
                                is_superuser=0,
                                recipient_id=user_id,
                                email=email,
                                username=name,
                                is_staff=member_type,
                                is_active=member_type,
                                date_joined=datetime.now())

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "account/login.html/")

    def post(self, request):
        # TODO 로그인
        id = request.data.get('id', None)
        password = request.data.get('password', None)

        user = AuthUser.objects.filter(id=id).first()

        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

        if user.password == password:
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['id'] = id
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


def logoutUser(request):
    logout(request)
    return redirect('login')