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


def generate_training_form():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    p.translate(0, height)
    p.setFont('Arial', 12) 
    p.setTitle('TBS Training Application and Authorization Form')
    p.drawString(5*inch, 0.5*inch, "Protected B")

    # p.drawString(750, 750, "PROTECTED B")
    # p.drawString(75, 750, "TBS Training Application and Authorization Form")
    p.line(50, 700, 550, 700)

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
            # Save the data to the database
            # generate the pdf
            #filename = generate_pdf2(request)
            filename = generate_training_form() 
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
