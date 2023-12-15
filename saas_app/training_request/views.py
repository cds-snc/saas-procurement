from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import TrainingForm, CourseForm, UserForm
from .models import TrainingRequest, Users
import django.contrib.messages as messages
import io
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from django.core.files.base import ContentFile
import common.util.utils as utils


# Send an email to the requestor
def email_requestor(request, template_id):
    # get the requester's email address
    requestor_email = request.user.email
    # get the requestors's name
    requestor_name = request.user.first_name
    # get the url
    url = utils.get_current_site(request)

    # send an email to the requestor
    utils.send_email(
        requestor_email,
        template_id,
        {
            "name": requestor_name,
            "url": url,
        },
    )

def email(request, template_id, recipient):
    # get the requester's email address
    requestor_email = request.user.email
    # get the requestors's name
    requestor_name = request.user.first_name
    # get the url
    url = utils.get_current_site(request)

    # send the email based on the recipient
    if recipient == ("requestor" or "internal_ops"):
        # send an email to the requestor
        utils.send_email(
            requestor_email,
            template_id,
            {
                "name": requestor_name,
                "url": url,
            },
        )


# Generate the PDF training from using data from the Form
def generate_training_form(form_data):
    # create teh buffer, canvas and set up the title
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    print("Width: ", width)
    print("Height: ", height)
    p.setFont("Helvetica", 10)
    p.setTitle("CDS Training Application and Authorization Form")

    # set Protected B heading and title of the document.
    p.setFillColor(HexColor("#1F51FF"))
    p.drawString(6.5 * inch, 10.5 * inch, "PROTECTED B / PROTÉGÉ B")
    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 12)
    p.drawString(
        2.1 * inch, 10 * inch, "CDS Training Application and Authorization Form /"
    )
    p.drawString(
        1.6 * inch,
        9.8 * inch,
        "Formulaire de demande et d’autorisation de formation du SNC",
    )
    p.setFont("Helvetica-Bold", 10)
    p.line(0.5 * inch, 9.5 * inch, 8.0 * inch, 9.5 * inch)

    # Draw a gray rectangle
    p.setFillColor(HexColor("#E5E4E2"))
    p.rect(0.5 * inch, 9.0 * inch, 7.5 * inch, 0.65 * inch, fill=1)

    p.setFillColor(HexColor("#000000"))
    p.drawString(
        0.7 * inch,
        9.3 * inch,
        "Please complete fields or select an option from the drop down menu. / Veuillez remplir les champs ou ",
    )
    p.drawString(
        0.7 * inch, 9.1 * inch, "sélectionner une option dans le menu déroulant."
    )
    p.line(0.5 * inch, 9.0 * inch, 8.0 * inch, 9.0 * inch)

    # Requestor Information
    p.drawString(0.8 * inch, 8.7 * inch, "Name / Nom")
    p.setFont("Helvetica", 10)
    full_name = form_data["first_name"] + " " + form_data["last_name"]
    p.drawString(2 * inch, 8.7 * inch, full_name)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 8.45 * inch, "Position title / Titre du poste")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 8.45 * inch, form_data["title"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 8.2 * inch, "E-Mail / Courrier électronique")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 8.2 * inch, form_data["dept_email"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 7.95 * inch, "Telephone No. / No de téléphone")
    p.setFont("Helvetica", 10)
    p.drawString(3.3 * inch, 7.95 * inch, str(form_data["telephone"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 7.7 * inch, "Sector / Secteur ")
    p.setFont("Helvetica", 10)
    p.drawString(2.0 * inch, 7.7 * inch, form_data["sector"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch,
        7.45 * inch,
        "Personal Record Identifier (PRI) / Code d’identification de dossier personnel (CIDP)",
    )
    p.drawString(0.8 * inch, 7.2 * inch, "Group and Level / Groupe et niveau")
    p.setFont("Helvetica", 10)
    group_level = form_data["group"] + " " + form_data["level"]
    p.drawString(3.4 * inch, 7.2 * inch, group_level)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 6.95 * inch, "City/Ville")
    p.setFont("Helvetica", 10)
    p.drawString(3.0 * inch, 6.95 * inch, form_data["city"])
    p.line(0.5 * inch, 6.7 * inch, 8.0 * inch, 6.7 * inch)

    # Course Information
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 6.45 * inch, "Course Title / Titre du cours")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 6.45 * inch, form_data["course_title"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch, 6.2 * inch, "Training Description / Description de la formation"
    )
    p.setFont("Helvetica", 10)
    if len(form_data["description"]) > 50:
        p.drawString(4.2 * inch, 6.2 * inch, form_data["description"][:70])
        p.drawString(0.8 * inch, 6.05 * inch, form_data["description"][70:])
    else:
        p.drawString(4.2 * inch, 6.2 * inch, form_data["description"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 5.85 * inch, "Provider / Fournisseur")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 5.85 * inch, form_data["provider"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 5.6 * inch, "Language of course / Langue du cours")
    p.setFont("Helvetica", 10)
    p.drawString(3.5 * inch, 5.6 * inch, form_data["language"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 5.35 * inch, "Start date / Date de début")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 5.35 * inch, str(form_data["start_date"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 5.1 * inch, "Duration / Durée")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 5.1 * inch, form_data["duration"])
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch,
        4.85 * inch,
        "Location (Virtual/In-person?)/ Lieu (virtuel/en personne ?)",
    )
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 4.85 * inch, form_data["location"])
    p.line(0.5 * inch, 4.7 * inch, 8.0 * inch, 4.7 * inch)

    # Cost Information
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 4.45 * inch, "Costs* / Couts*")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 4.45 * inch, str(form_data["cost"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 4.2 * inch, "Fund centre / Centre financier")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 4.2 * inch, str(form_data["fund_center"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(0.8 * inch, 3.95 * inch, "Travel")
    p.setFillColor(HexColor("#000000"))
    p.drawString(
        1.27 * inch, 3.95 * inch, "or living costs / Couts de voyage ou de subsistance"
    )
    p.setFont("Helvetica", 10)
    p.drawString(4.9 * inch, 3.95 * inch, form_data["travel_living_costs"])
    p.line(0.5 * inch, 3.7 * inch, 8.0 * inch, 3.7 * inch)

    # Supervisors signature
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch,
        3.45 * inch,
        "Performance delegated supervisor’s name / Nom du superviseur délégué du rendement",
    )
    p.setFont("Helvetica", 10)
    p.drawString(0.8 * inch, 3.25 * inch, str(form_data["manager"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch, 3.0 * inch, "Supervisor’s signature / Signature du superviseur"
    )
    p.setFont("Helvetica", 10)
    p.line(4.1 * inch, 2.95 * inch, 8.0 * inch, 2.95 * inch)
    p.line(0.5 * inch, 2.85 * inch, 8.0 * inch, 2.85 * inch)

    # Fund center manager signature
    p.setFont("Helvetica-Bold", 10)
    p.drawString(
        0.8 * inch,
        2.6 * inch,
        "Fund centre manager (Certified that funds are available pursuant to ",
    )
    p.setFillColor(HexColor("#1F51FF"))
    p.drawString(5.3 * inch, 2.6 * inch, "Section 32(1) FAA")
    p.linkURL(
        "https://laws-lois.justice.gc.ca/eng/acts/F-11/index.html",
        (5.3 * inch, 2.6 * inch, 10 * inch, 5 * inch),
        relative=1,
    )
    p.setFillColor(HexColor("#000000"))
    p.drawString(6.5 * inch, 2.6 * inch, "/ Gestionnaire du")
    p.drawString(
        0.8 * inch,
        2.4 * inch,
        "centre financier (Attestation de la disponibilité des fonds aux termes de l’article 32(1) LGPF)",
    )
    p.drawString(0.8 * inch, 2.15 * inch, "Name / Nom")
    p.setFont("Helvetica", 10)
    p.drawString(3.2 * inch, 2.15 * inch, str(form_data["s32_approved_by"]))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(4.8 * inch, 2.15 * inch, "Date")
    p.drawString(
        0.8 * inch,
        1.9 * inch,
        "Signature Section 32(1) FAA / Signature article 32(1) LGPF",
    )
    p.line(4.8 * inch, 1.85 * inch, 8.0 * inch, 1.85 * inch)
    p.line(0.5 * inch, 1.75 * inch, 8.0 * inch, 1.75 * inch)

    # Bottom instructions
    # Set the brackground color to be gray#
    p.setFillColor(HexColor("#E5E4E2"))
    p.rect(0.5 * inch, 0.3 * inch, 7.5 * inch, 1.45 * inch, fill=1)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 8)
    p.drawString(
        0.8 * inch,
        1.6 * inch,
        "Return completed form to your sector HR and Finance Coordinator or to your training authorizer. / Retourner le formulaire dument",
    )
    p.drawString(
        0.8 * inch,
        1.45 * inch,
        "rempli à votre coordonnateur des ressources humaines et des finances de votre secteur ou à votre responsable de la formation.",
    )
    p.line(0.5 * inch, 1.3 * inch, 8.0 * inch, 1.3 * inch)
    p.setFont("Helvetica-Oblique", 8)
    p.drawString(
        0.8 * inch,
        1.05 * inch,
        "*As per the TBS Departmental Human Resources Delegation Instrument, any fees that total or could accrue to $10,000 or more must be ",
    )
    p.drawString(
        0.8 * inch,
        0.9 * inch,
        "reviewed and approved by the Secretary prior to registration. Contact Learning and Community Development Services to arrange this approval. ",
    )
    p.drawString(
        0.8 * inch,
        0.75 * inch,
        "*Selon l’Instrument ministériel de délégation en matière de ressources humaines du SCT, les frais totalisant ou pouvant atteindre 10 000 $ ou ",
    )
    p.drawString(
        0.8 * inch,
        0.6 * inch,
        "plus doivent être examinés et approuvés par le secrétaire avant l’inscription. Contactez les services d’apprentissage et de perfectionnement des",
    )
    p.drawString(
        0.8 * inch, 0.45 * inch, "communautés pour organiser cette approbation."
    )

    # Draw borders
    p.line(0.5 * inch, 0.30 * inch, 8.0 * inch, 0.30 * inch)
    p.line(0.5 * inch, 9.5 * inch, 0.5 * inch, 0.30 * inch)
    p.line(8.0 * inch, 9.5 * inch, 8.0 * inch, 0.30 * inch)

    # Save the PDF and return the buffer IO bytes
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer


# Process the training request form
def process_requests(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        course_form = CourseForm(request.POST)
        form = TrainingForm(request.POST)
        if form.is_valid() and course_form.is_valid() and user_form.is_valid():
            # Combine the data from the three forms - user, course and training form
            form_data = {
                **form.cleaned_data,
                **course_form.cleaned_data,
                **user_form.cleaned_data,
            }

            # generate the pdf
            pdf = generate_training_form(form_data)

            # get the user object
            user_object = Users.objects.get(user=request.user)
            # update all the fields for the user
            user_object.first_name = user_form.cleaned_data["first_name"]
            user_object.last_name = user_form.cleaned_data["last_name"]
            user_object.title = user_form.cleaned_data["title"]
            user_object.dept_email = user_form.cleaned_data["dept_email"]
            user_object.telephone = user_form.cleaned_data["telephone"]
            user_object.sector = user_form.cleaned_data["sector"]
            user_object.group = user_form.cleaned_data["group"]
            user_object.level = user_form.cleaned_data["level"]
            user_object.city = user_form.cleaned_data["city"]
            user_object.save()

            # update all the fields for the course
            course_object = course_form.save(commit=False)
            # course_object = course_form.cleaned_data["course_title"]
            course_object.save()

            # update all the fields for the training request
            training_object = form.save(commit=False)
            training_object.submitted_by = request.user
            # Save the course object to the training object
            training_object.course = course_object
            training_object.status = _("Request submitted")

            # Save the pdf file to the pdf_form field in the training object
            pdf_file = ContentFile(pdf.getvalue())

            # generate the name for the pdf file
            file_name = (
                "training_form_"
                + str(user_object.last_name)
                + "_"
                + str(course_object.course_title)
                + ".pdf"
            )
            training_object.pdf_form.save(file_name, pdf_file)

            # Save the training object
            training_object.save()

            # Email the requestor and also send an email to internal ops
            # email_requestor(request, os.getenv("TRAINING_FORM_REQUESTOR_TEMPLATE_ID"))
            email(request, os.getenv("TRAINING_REQUEST_REQUESTOR_TEMPLATE_ID"), "requestor")
            email(request, os.getenv("TRAINING_REQUEST_INTERNAL_OPS_TEMPLATE_ID"), "internal_ops")

            

            # Tell the user that the form was submitted successfully
            messages.success(
                request, _("Your training form was submitted successfully!")
            )
            # Redirect the user to the thanks page
            return render(
                request, "training/training_thanks.html", {"pk": training_object.pk}
            )
    else:
        # Clear the forms so that we can display them
        form = TrainingForm()
        course_form = CourseForm()
        user_form = UserForm()

    # show the form again
    return render(
        request,
        "training/training_request.html",
        {"form": form, "course_form": course_form, "user_form": user_form},
    )


# function to download the pdf file
def download(request):
    # get the file object
    file_obj = TrainingRequest.objects.get(pk=request.GET.get("pk"))
    # get the name of the file
    filename = file_obj.pdf_form.name
    # Create the FileResponse and return the file
    response = FileResponse(
        file_obj.pdf_form.open(), as_attachment=True, filename=filename
    )
    response["Content-Disposition"] = f"attachment; filename= {filename}"
    return response


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
        # get the user
        user = Users.objects.get(user=request.user)
        user_form = UserForm(instance=user)
        course_form = CourseForm(instance=training_request.course)
        form = TrainingForm(instance=training_request)
        return render(
            request,
            "training/view_request.html",
            {"form": form, "course_form": course_form, "user_form": user_form},
        )
