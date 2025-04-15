from django.shortcuts import render
from .serializers.accountsmanagement_serializers import PasswordNumberSerializer, TokenValidationsSerializer
from rest_framework import generics
# from rest_framework.views import APIView
from accounts.models import CustomUser
from django.db.models import Q
from rest_framework import status
from django.core.cache import cache
# from .sms_sender import SendSms, ContactMe
from rest_framework import response

import random
import string

otp_time_expired = 1200
# Create your views here.
class PasswordResetView(generics.GenericAPIView):

    def generate_otp(self,user):
        # Generate a random 5-digit OTP
        user= str(user)
        return user[0]+''.join(random.choices(string.digits, k=4)) + user[-1]
    
    serializer_class = PasswordNumberSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        email = serializer.data['email']
        user = CustomUser.objects.filter(Q(email=email) | Q(phone=email)).first()  #match email with DB
        if user:
            
            otp = self.generate_otp(user.id)

            email_type = "reset_password"   #Why oTP?

            subject = 'Skillshikshya Password Reset OTP'  #email subject
            if '@' in email:   #email valid
                email = user.email
                sendPasswordResetMail(email, otp,subject,email_type,user)
            # else:
            #     SendSms(contact=email,otp=otp,message=subject)
            
            cache_key = f"password_reset_otp_{user.id}"
            cache.set(cache_key, otp, timeout=otp_time_expired)

            return response.Response(
                {
                "message" : "OTP has been sent to your email address"
                },
                status = status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message":"User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

def sendPasswordResetMail(email, otp, subject, email_type, user):
    password_html_contents = ""      # Initialize to avoid UnboundLocalError

    if email_type == "reset_password":      # Ensures this matches what is passed
        context  = {
            'otp' : otp,
            'user' : user,
            'verification_url' : 'https://example.com/verify'
        }

        password_html_contents = render_to_string('reset_password_otp.html', context)

    email_from = settings.EMAIL_HOST_USER
    receipient_list = [email]
    plain_message = ''
    send_email(subject, plain_message, email_from, receipient_list, html_message=password_html_contents)

class VerifyUserPasswordToken(generics.GenericAPIView):
    serializer_class = TokenValidationsSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data, context={"kwargs":kwargs})
        serializer.is_valid(raise_exception=True)

        return response.Response(
            {
                "message":"Your Token is Validate",
                'data' : serializer.data,
            },
            status=status.HTTP_200_OK,
        )