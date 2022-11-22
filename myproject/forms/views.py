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
  
    text_file = open("latexfiles/withdraw.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentName" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentRollno", rollno)
    #filedata = filedata.replace("currentyear", curyear)
    filedata = filedata.replace("studentProgramme", "\\textbf{" +degree+"}",1)
    filedata = filedata.replace("studentDepartment", dept)
    filedata = filedata.replace("studentJoiningDate", doj)
    filedata = filedata.replace("studentQualification", prevdeg)
    filedata = filedata.replace("studentCategory", category)
    filedata = filedata.replace("studentAdvisor1", facads1)
    filedata = filedata.replace("studentAdvisor2", facads2)
    filedata = filedata.replace("studentCPI", cpi)
    filedata = filedata.replace("studentReason", reason)

  
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
    exam = request.POST['exam']
    gyear = request.POST['gyear']
    email = request.POST['email']
    contact = request.POST['contact']
  
    text_file = open("latexfiles/undertaking.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentName" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentRollno", rollno)
    filedata = filedata.replace("studentExam", exam+" "+gyear)
    filedata = filedata.replace("studentPrpgramme", degree)
    filedata = filedata.replace("studentDepartment", dept)
    filedata = filedata.replace("studentRollNo @iitb.ac.in", email)
    filedata = filedata.replace("studentContact", contact)

  
    text_file = open("latexfiles/newundertaking.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newundertaking.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newundertaking.pdf", 'rb'), content_type='application/pdf')


def reexam(request):

    if os.path.isfile("newreexam.aux"):
        os.remove("newreexam.aux")
    if os.path.isfile("newreexam.log"):
        os.remove("newreexam.log")
    if os.path.isfile("newreexam.pdf"):
        os.remove("newreexam.pdf")

    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    rollno = request.POST['rollno']
    dept = request.POST['dept']
    #degree = request.POST['degree']
    category = request.POST['category']
    hostelroom = request.POST['hostelroom']
    email = request.POST['email']
    receipt = request.POST['receipt']
    
    cnum1 = request.POST['cnum1']
    cname1 = request.POST['cname1']
    cslot1 = request.POST['cslot1']
    cgrade1 = request.POST['cgrade1']
    cinstr1 = request.POST['cinstr1']

    cnum2 = request.POST['cnum2']
    cname2 = request.POST['cname2']
    cslot2 = request.POST['cslot2']
    cgrade2 = request.POST['cgrade2']
    cinstr2 = request.POST['cinstr2']

    cnum3 = request.POST['cnum3']
    cname3 = request.POST['cname3']
    cslot3 = request.POST['cslot3']
    cgrade3 = request.POST['cgrade3']
    cinstr3 = request.POST['cinstr3']

    cnum4 = request.POST['cnum4']
    cname4 = request.POST['cname4']
    cslot4 = request.POST['cslot4']
    cgrade4 = request.POST['cgrade4']
    cinstr4 = request.POST['cinstr4']
  
    text_file = open("latexfiles/reexam.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentName" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentRollno", rollno)
    filedata = filedata.replace("studentCategory", category)
    filedata = filedata.replace("studentDepartment", dept)
    filedata = filedata.replace("studentHostelRoom", hostelroom)
    filedata = filedata.replace("studentRollno@iitb.ac.in", email)
    filedata = filedata.replace("receiptnum", receipt)

    filedata = filedata.replace("cnum1", cnum1)
    filedata = filedata.replace("cname1", cname1)
    filedata = filedata.replace("cslot1", cslot1)
    filedata = filedata.replace("cgrade1", cgrade1)
    filedata = filedata.replace("cinstr1", cinstr1)

    filedata = filedata.replace("cnum2", cnum2)
    filedata = filedata.replace("cname2", cname2)
    filedata = filedata.replace("cslot2", cslot2)
    filedata = filedata.replace("cgrade2", cgrade2)
    filedata = filedata.replace("cinstr2", cinstr2)

    filedata = filedata.replace("cnum3", cnum3)
    filedata = filedata.replace("cname3", cname3)
    filedata = filedata.replace("cslot3", cslot3)
    filedata = filedata.replace("cgrade3", cgrade3)
    filedata = filedata.replace("cinstr3", cinstr3)

    filedata = filedata.replace("cnum4", cnum4)
    filedata = filedata.replace("cname4", cname4)
    filedata = filedata.replace("cslot4", cslot4)
    filedata = filedata.replace("cgrade4", cgrade4)
    filedata = filedata.replace("cinstr4", cinstr4)

  
    text_file = open("latexfiles/newreexam.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newreexam.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newreexam.pdf", 'rb'), content_type='application/pdf')