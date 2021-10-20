from django.shortcuts import render,redirect
from django.http import HttpResponse
#from ..sparks_paymentgateway.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
from sparks_paymentgateway.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.core.mail import send_mail
from django.conf import settings
from .models import RazorPay

# Create your views here.


client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
def home(request):
    amount: 1000
    currency: "INR"

    payment_order=client.order.create(dict(amount=100,currency='INR',payment_capture=1))
    payment_order_id=payment_order['id']
    context={
        'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id
    }

    return render(request,"index.html",context=context)
    return redirect('/mail')



def success(request):
    return render(request,"success.html")

def mail(request):
     subject="Your Payment Done"
     msg="Thank You for Donation"
     to="monalibawankar97@gmail.com"
     res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
     if (res==1):
         msg="mail send successfully"

     else:
         msg="mail could not send"

     return HttpResponse(msg)
