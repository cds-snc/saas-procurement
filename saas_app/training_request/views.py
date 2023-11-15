from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import TrainingForm, CourseForm, UserForm
from .models import TrainingRequest
import django.contrib.messages as messages
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
from reportlab.lib.units import cm, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor


def generate_pdf2(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
    p=canvas.Canvas(response)

    p.drawString(100, 100, "Hello World")
    p.showPage()
    p.save()
    return response


def generate_training_form(form_data):
    # Register the Ariel font
    # pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    # pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial-Bold.ttf'))
    # pdfmetrics.registerFont(TTFont('Arial-Italic', 'Arial-Italic.ttf'))
    # pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'Arial-BoldItalic.ttf'))
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    print("Width: ", width)
    print("Height: ", height)
    p.setFont('Helvetica', 10)
    p.setTitle('TBS Training Application and Authorization Form')

    p.setFillColor(HexColor('#1F51FF'))
    p.drawString(6.5*inch, 10.5*inch,"PROTECTED B / PROTÉGÉ B")
    p.setFillColor(HexColor('#000000'))
    p.setFont('Helvetica-Bold', 12)
    p.drawString(2.1*inch, 10*inch,"TBS Training Application and Authorization Form /")
    p.drawString(1.6*inch, 9.8*inch,"Formulaire de demande et d’autorisation de formation du SCT")
    p.setFont('Helvetica-Bold', 10)
    p.line(0.5*inch, 9.5*inch, 8.0*inch, 9.5*inch)

    # Draw a gray rectangle
    p.setFillColor(HexColor('#E5E4E2'))
    p.rect(0.5*inch, 9.0*inch, 7.5*inch, 0.65*inch, fill=1)

    p.setFillColor(HexColor('#000000'))
    p.drawString(0.7*inch, 9.3*inch,"Please complete fields or select an option from the drop down menu. / Veuillez remplir les champs ou ")
    p.drawString(0.7*inch, 9.1*inch,"sélectionner une option dans le menu déroulant.")
    p.line(0.5*inch, 9.0*inch, 8.0*inch, 9.0*inch)
    
    # Requestor Information
    p.drawString(0.8*inch, 8.7*inch,"Name / Nom")
    p.setFont('Helvetica', 10)
    p.drawString(2*inch, 8.7*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 8.45*inch, "Position title / Titre du poste") 
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 8.45*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 8.2*inch, "E-Mail / Courrier électronique")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 8.2*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.95*inch, "Telephone No. / No de téléphone")
    p.setFont('Helvetica', 10)
    p.drawString(3.3*inch, 7.95*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.7*inch, "Sector / Secteur ")
    p.setFont('Helvetica', 10)
    p.drawString(2.0*inch, 7.7*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.45*inch, "Personal Record Identifier (PRI) / Code d’identification de dossier personnel (CIDP)")
    p.drawString(0.8*inch, 7.2*inch, "Group and Level / Groupe et niveau")
    p.setFont('Helvetica', 10)
    p.drawString(3.4*inch, 7.2*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 6.95*inch, "Employment Status / Statut d'emploi")
    p.setFont('Helvetica', 10)
    p.drawString(3.4*inch, 6.95*inch, form_data['title'])
    p.line(0.5*inch, 6.7*inch, 8.0*inch, 6.7*inch)

    # Course Information
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 6.45*inch, "Course Title / Titre du cours")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 6.45*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 6.2*inch, "Training Description / Description de la formation") 
    p.setFont('Helvetica', 10)
    if (len(form_data['description']) > 50):
        p.drawString(4.2*inch, 6.2*inch, form_data['description'][:70])
        p.drawString(0.8*inch, 6.05*inch, form_data['description'][70:])
    else:
        p.drawString(4.2*inch, 6.2*inch, form_data['description'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.85*inch, "Provider / Fournisseur")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 5.85*inch, form_data['provider'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.6*inch, "Language of course / Langue du cours")
    p.setFont('Helvetica', 10)
    p.drawString(3.5*inch, 5.6*inch, form_data['language'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.35*inch, "Start date / Date de début")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 5.35*inch, form_data['title'])
    #p.drawString(3.2*inch, 4.6*inch, form_data['start_date'].strftime("%d/%m/%Y"))
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.1*inch, "Duration / Durée")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 5.1*inch, form_data['duration'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.85*inch, "Location / Lieu")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.85*inch, form_data['location'])
    p.line(0.5*inch, 4.7*inch, 8.0*inch, 4.7*inch)
    
    # Cost Information
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.45*inch, "Costs* / Couts*")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.45*inch, str(form_data['cost']))
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.2*inch, "Fund centre / Centre financier")
    p.setFont('Helvetica', 10)
    # p.linkURL('http://google.com', (3.2*inch, 3.0*inch, 6.0*inch, 3.0*inch), relative=1)
    p.drawString(3.2*inch, 4.2*inch, form_data['title'])
    #p.drawString(3.2*inch, 3.0*inch, form_data['fund_centre'])
    p.setFont('Helvetica-Bold', 10)
    p.setFillColor(HexColor('#1F51FF'))
    p.drawString(0.8*inch, 3.95*inch, "Travel")
    p.linkURL('https://infosite.tbs-sct.gc.ca/services/fm-gf/asmp/tra-voy_e.aspx', (0.8*inch, 3.95*inch, 1.6*inch, 8*inch), relative=1)
    p.setFillColor(HexColor('#000000'))
    p.drawString(1.27*inch, 3.95*inch, "or living costs / Couts de voyage ou de subsistance")
    # p.linkURL('http://google.com', (inch, 2.7*inch, 5.0*inch, 0.5*inch), relative=1)
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.95*inch, form_data['travel_living_costs'])
    p.line(0.5*inch, 3.7*inch, 8.0*inch, 3.7*inch)
    
    # Supervisors signature
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 3.45*inch, "Performance delegated supervisor’s name / Nom du superviseur délégué du rendement")
    p.setFont('Helvetica', 10)
    p.drawString(0.8*inch, 3.25*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 3.0*inch, "Supervisor’s signature / Signature du superviseur")
    p.setFont('Helvetica', 10)
    p.line(4.1*inch, 2.95*inch, 8.0*inch, 2.95*inch)
    p.line(0.5*inch, 2.85*inch, 8.0*inch, 2.85*inch)

    # Fund center manager signature
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 2.6*inch, "Fund centre manager (Certified that funds are available pursuant to ")
    p.setFillColor(HexColor('#1F51FF'))
    p.drawString(5.3*inch, 2.6*inch, "Section 32(1) FAA") 
    p.linkURL('https://laws-lois.justice.gc.ca/eng/acts/F-11/index.html', (5.3*inch, 2.6*inch, 10*inch, 5*inch), relative=1)
    p.setFillColor(HexColor('#000000'))
    p.drawString(6.5*inch, 2.6*inch, "/ Gestionnaire du")
    p.drawString(0.8*inch, 2.4*inch, "centre financier (Attestation de la disponibilité des fonds aux termes de l’article 32(1) LGPF)")
    p.drawString(0.8*inch, 2.15*inch, "Name / Nom")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 2.15*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(4.8*inch, 2.15*inch, "Date")
    p.drawString(0.8*inch, 1.9*inch, "Signature Section 32(1) FAA / Signature article 32(1) LGPF")
    p.line(4.8*inch, 1.85*inch, 8.0*inch, 1.85*inch)
    p.line(0.5*inch, 1.75*inch, 8.0*inch, 1.75*inch)
    
    # Bottom instructions 
    # Set the brackground color to be gray#
    p.setFillColor(HexColor('#E5E4E2'))
    p.rect(0.5*inch, 0.3*inch, 7.5*inch, 1.45*inch, fill=1)
    
    p.setFillColor(HexColor('#000000'))
    p.setFont('Helvetica-Bold', 8)
    p.drawString(0.8*inch, 1.6*inch, "Return completed form to your sector HR and Finance Coordinator or to your training authorizer. / Retourner le formulaire dument")
    p.drawString(0.8*inch, 1.45*inch, "rempli à votre coordonnateur des ressources humaines et des finances de votre secteur ou à votre responsable de la formation.")
    p.line(0.5*inch, 1.3*inch, 8.0*inch, 1.3*inch)
    p.setFont('Helvetica-Oblique', 8)
    p.drawString(0.8*inch, 1.05*inch, "*As per the TBS Departmental Human Resources Delegation Instrument, any fees that total or could accrue to $10,000 or more must be ")
    p.drawString(0.8*inch, 0.9*inch, "reviewed and approved by the Secretary prior to registration. Contact Learning and Community Development Services to arrange this approval. ")
    p.drawString(0.8*inch, 0.75*inch, "*Selon l’Instrument ministériel de délégation en matière de ressources humaines du SCT, les frais totalisant ou pouvant atteindre 10 000 $ ou ")
    p.drawString(0.8*inch, 0.6*inch, "plus doivent être examinés et approuvés par le secrétaire avant l’inscription. Contactez les services d’apprentissage et de perfectionnement des")
    p.drawString(0.8*inch, 0.45*inch, "communautés pour organiser cette approbation." )  
    
    # Draw borders
    p.line(0.5*inch, 0.30*inch, 8.0*inch, 0.30*inch)
    p.line(0.5*inch, 9.5*inch, 0.5*inch, 0.30*inch)
    p.line(8.0*inch, 9.5*inch, 8.0*inch, 0.30*inch)


    p.showPage()
    p.save()
    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


    
def generate_pdf():
    # Create the pdf buffer
    
    print("In generate_pdf")
    buffer = io.BytesIO()
    # Create the PDF object
    
    p = canvas.Canvas(buffer)
    # Draw the data onto the PDF
    p.drawString(100, 100, "Hello World")
    
    # Close the PDF object 
    p.showPage()
    p.save()
    
    # Set the content-disposition header to force the browser to download the file
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

# Process the training request form
def process_requests(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        course_form = CourseForm(request.POST)
        form = TrainingForm(request.POST)
        if form.is_valid() and course_form.is_valid() and user_form.is_valid():
            # Combine the data from the two forms
            form_data = {**form.cleaned_data, **course_form.cleaned_data, **user_form.cleaned_data}
            print("All data: ", form_data)
            # Save the data to the database
            # generate the pdf
            #filename = generate_pdf2(request)
            filename = generate_training_form(form_data) 
            user_object = user_form.save(commit=False)
            user_object.save()
            course_object = course_form.save(commit=False)
            course_object.save()
            training_object = form.save(commit=False)
            training_object.pdf_form = filename.filename 
            training_object.submitted_by = request.user
            # Save the course object to the training object
            training_object.course = course_object
            training_object.status = _("Request submitted")
            training_object.save()
            messages.success(
                request, _("Your training form was submitted successfully!")
            )
            # filename = generate_pdf2(request)
            # filename = generate_pdf()
            return filename
            print("Filename: ", filename)
            # redirect to a new URL:
            return render(request, "training/training_thanks.html", {"filename": "hello.pdf"})
    else:
        # Clear the forms so that we can display them
        form = TrainingForm()
        course_form = CourseForm()
        user_form = UserForm()

    return render(
        request,
        "training/training_request.html",
        {"form": form, "course_form": course_form, "user_form": user_form},
    )


# function to return the list of submitted training requests for the logged in user
def view_all_requests(request):
    if request.method == "GET":
        # search for all the training requests submitted by the logged in user
        submitted_training_requests = TrainingRequest.objects.filter(
            submitted_by=request.user, date_manager_reviewed__isnull=True
        )
        prev_submitted_training_requests = TrainingRequest.objects.filter(
            submitted_by=request.user, date_manager_reviewed__isnull=False
        ).order_by("-date_manager_reviewed")
        # render the requests in a table
        return render(
            request,
            "training/view_all_requests.html",
            {
                "submitted_requests": submitted_training_requests,
                "prev_submitted_requests": prev_submitted_training_requests,
            },
        )


# function to view a single training request
def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        training_request = TrainingRequest.objects.get(pk=pk)
        course_form = CourseForm(instance=training_request.course)
        form = TrainingForm(instance=training_request)
        return render(
            request,
            "training/view_request.html",
            {"form": form, "course_form": course_form},
        )
