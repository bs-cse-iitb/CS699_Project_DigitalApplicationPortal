from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.template import loader
from django.contrib import messages
import os
import subprocess


# Create your views here.

def formsselect(request):
  template = loader.get_template('forms.html')
  return HttpResponse(template.render({}, request))

def fillform(request):
    option = request.POST['Forms']
    print(option)
    if option == 'undertaking':
        template = loader.get_template('undertaking.html')
        return HttpResponse(template.render({}, request))
    elif option == 'Withdrawal':
        template = loader.get_template('withdrawal.html')
        return HttpResponse(template.render({}, request))
    elif option == 'bonafide':
        template = loader.get_template('bonafide.html')
        return HttpResponse(template.render({}, request))
    elif option == 'reexam':
        template = loader.get_template('reexam.html')
        return HttpResponse(template.render({}, request))
    elif option == 'common':
        template = loader.get_template('common.html')
        return HttpResponse(template.render({}, request))


def bonafide(request):

    if os.path.isfile("newbona.aux"):
        os.remove("newbona.aux")
    if os.path.isfile("newbona.log"):
        os.remove("newbona.log")
    if os.path.isfile("newbona.pdf"):
        os.remove("newbona.pdf")

    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    rollno = request.POST['rollno']
    dept = request.POST['dept']
    degree = request.POST['degree']
    curyear = request.POST['curyear']
    purpose = request.POST['purpose']
  
    text_file = open("latexfiles/bonafide.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentfullname" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentrollno", rollno)
    filedata = filedata.replace("currentyear", curyear)
    filedata = filedata.replace(degree, "\\textbf{" +degree+"}",1)
    filedata = filedata.replace("studentdepartment", dept)
    filedata = filedata.replace("studentpurpose", purpose)

  
    text_file = open("latexfiles/newbona.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newbona.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newbona.pdf", 'rb'), content_type='application/pdf')


def withdrawal(request):

    if os.path.isfile("newwithdraw.aux"):
        os.remove("newwithdraw.aux")
    if os.path.isfile("newwithdraw.log"):
        os.remove("newwithdraw.log")
    if os.path.isfile("newwithdraw.pdf"):
        os.remove("newwithdraw.pdf")

    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    rollno = request.POST['rollno']
    dept = request.POST['dept']
    degree = request.POST['degree']
    doj = request.POST['doj']
    prevdeg = request.POST['prevdeg']
    category = request.POST['category']
    facads1 = request.POST['facads1']
    facads2 = request.POST['facads2']
    cpi = request.POST['cpi']
    reason = request.POST['reason']
    purpose = request.POST['purpose']
  
    text_file = open("latexfiles/withdraw.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentfullname" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentrollno", rollno)
    filedata = filedata.replace("currentyear", curyear)
    filedata = filedata.replace(degree, "\\textbf{" +degree+"}",1)
    filedata = filedata.replace("studentdepartment", dept)
    filedata = filedata.replace("studentpurpose", purpose)

  
    text_file = open("latexfiles/newwithdraw.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newwithdraw.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newwithdraw.pdf", 'rb'), content_type='application/pdf')


def undertaking(request):

    if os.path.isfile("newundertaking.aux"):
        os.remove("newundertaking.aux")
    if os.path.isfile("newundertaking.log"):
        os.remove("newundertaking.log")
    if os.path.isfile("newundertaking.pdf"):
        os.remove("newundertaking.pdf")

    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    rollno = request.POST['rollno']
    dept = request.POST['dept']
    degree = request.POST['degree']
    gyear = request.POST['gyear']
    email = request.POST['email']
    contact = request.POST['contact']
  
    text_file = open("latexfiles/undertaking.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentfullname" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentrollno", rollno)
    filedata = filedata.replace("currentyear", curyear)
    filedata = filedata.replace(degree, "\\textbf{" +degree+"}",1)
    filedata = filedata.replace("studentdepartment", dept)
    filedata = filedata.replace("studentpurpose", purpose)

  
    text_file = open("latexfiles/newundertaking.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newundertaking.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newundertaking.pdf", 'rb'), content_type='application/pdf')