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

def rendergenerateotp(request):
  request.session['forgpass'] = 1
  template = loader.get_template('generateotp.html')
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
    messages.error(request,"Incorrect IITB Email, please try Again !!!")
    template = loader.get_template('reg.html')
    return HttpResponse(template.render({}, request))

  #checking if pass1 and repass is equal
  if(pass1 != repass):
    messages.error(request,"Password Should be Equal !!!")
    template = loader.get_template('reg.html')
    return HttpResponse(template.render({}, request))

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
  send_mail('Your OTP for Verification', 'Your OTP is {}'.format(OTPNUM),'aniketjadhav.aj.4282536@gmail.com',[iitbemail],fail_silently=False)
  request.session['otpnum'] = OTPNUM
  request.session['email'] = iitbemail
  #print(OTPNUM)
  member.save() #Save Data to DB

  messages.info(request, 'Your account has been registered successfully!')
  return HttpResponseRedirect('/members/verifyemailreq/')
  #template = loader.get_template('regsucc.html')
  #return HttpResponse(template.render())
  #return HttpResponse('Registration Successfull !!')
  #return HttpResponseRedirect(reverse('index'))


def generateotp(request):
  iitbemail = request.POST['iitbemail']
  if Users.objects.filter(iitbemail=iitbemail).count() != 1:
    #print("1")
    messages.error(request,"No Email Id Found, Please try Again")
    template = loader.get_template('generateotp.html')
    return HttpResponse(template.render({}, request))
  else:
    #print("2")
    forgotpass = request.session.get('forgpass')
    if forgotpass:
      request.session['email'] = iitbemail
    OTPNUM = random.randrange(10000,99999)
    send_mail('Your OTP for Verification', 'Your OTP is {}'.format(OTPNUM),'aniketjadhav.aj.4282536@gmail.com',['aniket1jadhav.3@gmail.com'],fail_silently=False)
    request.session['otpnum'] = OTPNUM
    messages.success(request,"OTP Sent Successfully")
    template = loader.get_template('verifyemail.html')
    return HttpResponse(template.render({}, request))

def verifyemailreq(request):
  template = loader.get_template('verifyemail.html')
  return HttpResponse(template.render({}, request))

def verifyemail(request):
  OTPNUM = request.session.get('otpnum')
  forgotpass = request.session.get('forgpass')
  OTP = request.POST['OTP']
  #print(OTPNUM,OTP)
  if int(OTP) == int(OTPNUM):
    if forgotpass:
      template = loader.get_template('forgotpassword.html')
      return HttpResponse(template.render({}, request))
    else:
      member = Users.objects.get(iitbemail = request.session.get('email'))
      member.verified = 1
      member.save()
      messages.success(request, 'Account Verified !!!')
      return HttpResponseRedirect('/members/login/')
  else:
    messages.error(request, 'OTP Invalid Retry !!!')
    return HttpResponseRedirect('/members/verifyemailreq/')

  """if(mymember == None):
    return HttpResponse('Email Does not exist!! Please Enter correct Email')"""
  
  #template = loader.get_template('verifyemail.html')
  #return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render({}, request))


def loginverify(request):
  email = request.POST['iitbemail']
  password = request.POST['password']
  #print("hello null", mymember)
  if Users.objects.filter(iitbemail=email).count() != 1:
    messages.error(request,"Wrong Username & password Combination")
    return HttpResponseRedirect('/members/login/')
  else:
    mymember = Users.objects.get(iitbemail=email)
    if mymember.password == password:
      messages.success(request, "Login Successfull !!")
      request.session['login'] = 1
      return HttpResponse("Login Successfull !!")
    else:  
      messages.error(request, "Wrong Username & password Combination")
      return HttpResponseRedirect('/members/login/')


def forgotpass(request):
  pass1 = request.POST['pass']
  repass = request.POST['repass']
  if(pass1 != repass):
    messages.error(request,"Password Should be Equal !!!")
    template = loader.get_template('forgotpassword.html')
    return HttpResponse(template.render({}, request))
  else:
    member = Users.objects.get(iitbemail = request.session.get('email'))
    member.password = pass1
    member.save()
    messages.success(request,"Password Changed Successfully")
    return HttpResponseRedirect('/members/login/')