from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members, Users
import random
from django.core.mail import send_mail
from django.contrib import messages

#global OTPNUM
#OTPNUM = 0


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
  
  
  #Send Email for OTP Verification.
  OTPNUM = random.randrange(10000,99999)
  send_mail('Your OTP for Verification', 'Your OTP is {}'.format(OTPNUM),'aniketjadhav.aj.4282536@gmail.com',[personalemail],fail_silently=False)
  request.session['otpnum'] = OTPNUM
  print(OTPNUM)
  member.save() #Save Data to DB

  messages.info(request, 'Your account has been registered successfully!')
  return HttpResponseRedirect('/members/verifyemailreq/')
  #template = loader.get_template('regsucc.html')
  #return HttpResponse(template.render())
  #return HttpResponse('Registration Successfull !!')
  #return HttpResponseRedirect(reverse('index'))


def verifyemailreq(request):
  template = loader.get_template('verifyemail.html')
  return HttpResponse(template.render({}, request))

def verifyemail(request):
  OTPNUM = request.session.get('otpnum')
  OTP = request.POST['OTP']
  print(OTPNUM,OTP)
  if int(OTP) == int(OTPNUM):
    Member = Users(verified = 1)
    Member.save()
    return HttpResponse('Account Verified!!!')
  else:
    messages.error(request, 'OTP Invalid Retry !!!')
    return HttpResponseRedirect('/members/verifyemailreq/')

  """if(mymember == None):
    return HttpResponse('Email Does not exist!! Please Enter correct Email')"""
  
  #template = loader.get_template('verifyemail.html')
  #return HttpResponse(template.render())
