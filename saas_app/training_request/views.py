from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import TrainingForm, CourseForm
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


def generate_table():
    # Sample data
    data = [
        ["Name", "Age", "City"],
        ["John Doe", 30, "New York"],
        ["Jane Doe", 25, "San Francisco"],
        ["Bob Smith", 35, "Chicago"],
    ]

    # Create a PDF document
    pdf_filename = "table_example.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create a table and set style
    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Build the PDF
    document.build([table])


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
    # p.translate(0, height)
    p.setFont('Helvetica', 10)
    # # p.setFont('Arial', 12) 
    p.setTitle('TBS Training Application and Authorization Form')
    p.drawString(6.5*inch, 10.5*inch,"Protected B")
    p.setFont('Helvetica-Bold', 12)
    p.drawString(2.1*inch, 10*inch,"TBS Training Application and Authorization Form /")
    p.drawString(1.6*inch, 9.8*inch,"Formulaire de demande et d’autorisation de formation du SCT")
    p.setFont('Helvetica-Bold', 10)
    p.line(0.5*inch, 9.5*inch, 8.0*inch, 9.5*inch)
    # set the background color to gray
    # p.setFillColorRGB(211, 211, 211)
    # p.rect(0.5*inch, 9.5*inch, 8.0*inch, 9.0*inch, fill=1)
    p.drawString(0.7*inch, 9.3*inch,"Please complete fields or select an option from the drop down menu. / Veuillez remplir les champs ou ")
    p.drawString(0.7*inch, 9.1*inch,"sélectionner une option dans le menu déroulant.")
    p.line(0.5*inch, 9.0*inch, 8.0*inch, 9.0*inch)
    
    # Requestor Information
    p.drawString(0.8*inch, 8.6*inch,"Name / Nom")
    p.setFont('Helvetica', 10)
    p.drawString(2*inch, 8.6*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 8.3*inch, "Position title / Titre du poste") 
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 8.3*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 8.0*inch, "E-Mail / Courrier électronique")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 8.0*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.7*inch, "Telephone No. / No de téléphone")
    p.setFont('Helvetica', 10)
    p.drawString(3.3*inch, 7.7*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.4*inch, "Sector / Secteur ")
    p.setFont('Helvetica', 10)
    p.drawString(2.0*inch, 7.4*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 7.1*inch, "Personal Record Identifier (PRI) / Code d’identification de dossier personnel (CIDP)")
    p.drawString(0.8*inch, 6.8*inch, "Group and Level / Groupe et niveau")
    p.setFont('Helvetica', 10)
    p.drawString(3.4*inch, 6.8*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 6.5*inch, "Employment Status / Statut d'emploi")
    p.setFont('Helvetica', 10)
    p.drawString(3.4*inch, 6.5*inch, form_data['title'])
    p.line(0.5*inch, 6.2*inch, 8.0*inch, 6.2*inch)

    # Course Information
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.8*inch, "Course Title / Titre du cours")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 5.8*inch, form_data['title'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.5*inch, "Training Description / Description de la formation") 
    p.setFont('Helvetica', 10)
    if (len(form_data['description']) > 50):
        p.drawString(4.2*inch, 5.5*inch, form_data['description'][:65])
        p.drawString(0.8*inch, 5.35*inch, form_data['description'][65:])
    else:
        p.drawString(4.2*inch, 5.5*inch, form_data['description'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 5.2*inch, "Provider / Fournisseur")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 5.2*inch, form_data['provider'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.9*inch, "Language of course / Langue du cours")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.9*inch, form_data['language'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.6*inch, "Start date / Date de début")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.6*inch, form_data['title'])
    #p.drawString(3.2*inch, 4.6*inch, form_data['start_date'].strftime("%d/%m/%Y"))
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.3*inch, "Duration / Durée")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.3*inch, form_data['duration'])
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 4.0*inch, "Location / Lieu")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 4.0*inch, form_data['location'])
    p.line(0.5*inch, 3.7*inch, 8.0*inch, 3.7*inch)
    
    # Cost Information
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 3.3*inch, "Costs* / Couts*")
    p.setFont('Helvetica', 10)
    p.drawString(3.2*inch, 3.3*inch, str(form_data['cost']))
    p.setFont('Helvetica-Bold', 10)
    p.drawString(0.8*inch, 3.0*inch, "Fund centre / Centre financier")
    p.setFont('Helvetica', 10)
    p.linkURL('http://google.com', (3.2*inch, 3.0*inch, 6.0*inch, 3.0*inch), relative=1)
    p.drawString(3.2*inch, 3.0*inch, form_data['fund_centre'])
    p.setFont('Helvetica-Bold', 10)
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
        course_form = CourseForm(request.POST)
        form = TrainingForm(request.POST)
        if form.is_valid() and course_form.is_valid():
            # Combine the data from the two forms
            form_data = {**form.cleaned_data, **course_form.cleaned_data}
            print("All data: ", form_data)
            # Save the data to the database
            # generate the pdf
            #filename = generate_pdf2(request)
            filename = generate_training_form(form_data) 
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

    return render(
        request,
        "training/training_request.html",
        {"form": form, "course_form": course_form},
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
