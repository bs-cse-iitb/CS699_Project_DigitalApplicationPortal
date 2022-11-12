from django.http import HttpResponse
from django.template import loader
from .models import Members, Users
import random
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)

def registration(request):
  template = loader.get_template('reg.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  firstname = request.POST['firstname']
  middlename = request.POST['middlename']
  lastname = request.POST['lastname']
  rollno = request.POST['rollno']
  dept = request.POST['dept']
  phone = request.POST['phone']
  personalemail = request.POST['personalemail']
  iitbemail = request.POST['iitbemail']
  pass1 = request.POST['pass']
  repass = request.POST['repass']


  list1 =  str(iitbemail).split('@')
  if list1[1] != "iitb.ac.in":
    return HttpResponse('Incorrect IITB Email, please try Again !!!')


  #checking if pass1 and repass is equal
  if(pass1 != repass):
    return HttpResponse('Password not matching, please try Again !!!')

  member = Users(firstname = firstname,
                   middlename = middlename,
                   lastname = lastname,
                   rollno = rollno,
                   dept = dept,
                   mobno = phone,
                   peremail =  personalemail,
                   iitbemail =  iitbemail,
                   password =  pass1,
                   verified = 0)
  member.save()
  
  #Send Email for OTP Verification.
  global OTPNUM
  OTPNUM = random.randrange(10000,99999)
  send_mail('Your OTP for Verification', 'Your OTP is {}'.format(OTPNUM),'aniketjadhav.aj.4282536@gmail.com',[personalemail],fail_silently=False)

  template = loader.get_template('regsucc.html')
  return HttpResponse(template.render())
  #return HttpResponse('Registration Successfull !!')
  #return HttpResponseRedirect(reverse('index'))

def verifyemail(request):
  global OTPNUM
  OTP = request.POST['OTP']
  
  if OTP == OTPNUM:
    messages.success(request,'Email Verified')

  """if(mymember == None):
    return HttpResponse('Email Does not exist!! Please Enter correct Email')"""
  
  #template = loader.get_template('verifyemail.html')
  #return HttpResponse(template.render())
