
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
    doj = request.POST['doj']
    prevdeg = request.POST['prevdeg']
    category = request.POST['category']
    facads1 = request.POST['facads1']
    facads2 = request.POST['facads2']
    cpi = request.POST['cpi']
    reason = request.POST['reason']
    purpose = request.POST['purpose']
  
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