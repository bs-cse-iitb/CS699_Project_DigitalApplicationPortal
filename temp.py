
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
    degree = request.POST['degree']
    gyear = request.POST['gyear']
    email = request.POST['email']
    contact = request.POST['contact']
  
    text_file = open("latexfiles/reexam.txt", "r")
    filedata = text_file.read()
    text_file.close()

    filedata = filedata.replace("studentfullname" , firstname +" "+ middlename +" "+ lastname)
    filedata = filedata.replace("studentrollno", rollno)
    filedata = filedata.replace("currentyear", curyear)
    filedata = filedata.replace(degree, "\\textbf{" +degree+"}",1)
    filedata = filedata.replace("studentdepartment", dept)
    filedata = filedata.replace("studentpurpose", purpose)

  
    text_file = open("latexfiles/newreexam.tex", "w")
    text_file.write(filedata)
    text_file.close()
  

    tex_filename = 'latexfiles/newreexam.tex'
    #tex_filename =  os.path.abspath(tex_filename)
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
  
    return FileResponse(open("newreexam.pdf", 'rb'), content_type='application/pdf')