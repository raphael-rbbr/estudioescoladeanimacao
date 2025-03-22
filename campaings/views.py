from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import Inscription
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from django.views.generic.detail import DetailView
from pypdf import PdfWriter
from django.contrib.auth.decorators import login_required
from pdf2image import convert_from_path
from django.core.files.storage import default_storage
import os
import tempfile
from textwrap import wrap
from django.core.mail import send_mail
import fitz  # PyMuPDF
from openpyxl import Workbook
from django.utils.html import strip_tags


def CreateInscriprion(request):
    if request.method == "POST":
        new_name = request.POST.get('first_name')
        new_birthday = request.POST.get('nascimento')
        new_cpf = request.POST.get('cpf')
        # new_rg = request.POST.get('rg')
        new_age = request.POST.get('idade')
        new_gender = request.POST.get('genero')
        new_gender_other = request.POST.get('generooutros')
        new_ethnicity = request.POST.get('raca')
        new_ethnicity_other = request.POST.get('racaoutros')
        new_zipcode = request.POST.get('cep')
        # new_address = request.POST.get('endereco')
        # new_address_line_1 = request.POST.get('complemento')
        new_neighberhood = request.POST.get('bairro')
        new_city = request.POST.get('cidade')
        new_city_other = request.POST.get('outracidade')
        new_phone = request.POST.get('telefone')
        new_whatsapp = request.POST.get('whatsapp')
        new_email = request.POST.get('email')
        new_scholl_level = request.POST.get('escolaridade')
        # new_school = request.POST.get('instituicao')
        # new_grade = request.POST.get('serie')
        # if request.POST.get('turno') == None:
        #     new_studing = " "
        # else:
        #     new_studing = request.POST.get('turno')
        # new_course = request.POST.get('curso')
        new_parent = request.POST.get('nomeresponsavel')
        new_parent_phone = request.POST.get('telefoneresponsavel')
        new_intern = request.POST.get('estagio')
        new_intern_time = request.POST.get('horarioestagio')
        # new_looking_work = request.POST.get('buscaestagio')
        new_income = request.POST.get('renda')
        new_family = request.POST.get('pessoasrenda')
        new_deficincy = request.POST.get('deficiencia')
        new_deficincy_type = request.POST.get('qualdeficiencia')
        new_special_need = request.POST.get('atendimento')
        new_special_interview = request.POST.get('qualatendimento')
        new_knowloge = request.POST.get('conheceu_concatenated')
        new_knowloge_other = request.POST.get('conheceuoutros')
        new_prior_inscription = request.POST.get('inscreveu')
        new_prior_course = request.POST.get('participou')
        new_prior_course_year = request.POST.get('qualedicao')
        new_dedication = request.POST.get('frequencia')
        new_availability = request.POST.get('disponibilidadehorario_concatenated')
        new_tablet = request.POST.get('cutout')
        # new_likes_to_draw = request.POST.get('gostadesenhar')
        new_frequency = request.POST.get('freqdesenho')
        new_group_rating = request.POST.get('trabalharemgrupo')
        new_critics = request.POST.get('criticastrabalgo')
        new_previous_work = request.POST.get('destacaranimacao')
        new_message = request.POST.get('porqueinteresse')
        new_portifolio = request.POST.get('linkportifolio')
        new_file = request.FILES['desenho']








          # Print debug information
        # print(f"new_name: {new_name}")
        # print(f"new_birthday: {new_birthday}")
        # print(f"new_cpf: {new_cpf}")
        # print(f"new_age: {new_age}")
        # print(f"new_gender: {new_gender}")
        # print(f"new_gender_other: {new_gender_other}")
        # print(f"new_ethnicity: {new_ethnicity}")
        # print(f"new_ethnicity_other: {new_ethnicity_other}")
        # print(f"new_zipcode: {new_zipcode}")
        # print(f"new_neighberhood: {new_neighberhood}")
        # print(f"new_city: {new_city}")
        # print(f"new_city_other: {new_city_other}")
        # print(f"new_phone: {new_phone}")
        # print(f"new_whatsapp: {new_whatsapp}")
        # print(f"new_email: {new_email}")
        # print(f"new_scholl_level: {new_scholl_level}")
        # print(f"new_parent: {new_parent}")
        # print(f"new_parent_phone: {new_parent_phone}")
        # print(f"new_intern: {new_intern}")
        # print(f"new_intern_time: {new_intern_time}")
        # print(f"new_income: {new_income}")
        # print(f"new_family: {new_family}")
        # print(f"new_deficincy: {new_deficincy}")
        # print(f"new_deficincy_type: {new_deficincy_type}")
        # print(f"new_special_need: {new_special_need}")
        # print(f"new_special_interview: {new_special_interview}")
        # print(f"new_knowloge: {new_knowloge}")
        # print(f"new_knowloge_other: {new_knowloge_other}")
        # print(f"new_prior_inscription: {new_prior_inscription}")
        # print(f"new_prior_course: {new_prior_course}")
        # print(f"new_prior_course_year: {new_prior_course_year}")
        # print(f"new_dedication: {new_dedication}")
        # print(f"new_tablet: {new_tablet}")
        # print(f"new_frequency: {new_frequency}")
        # print(f"new_group_rating: {new_group_rating}")
        # print(f"new_critics: {new_critics}")
        # print(f"new_previous_work: {new_previous_work}")
        # print(f"new_message: {new_message}")
        # print(f"new_portifolio: {new_portifolio}")
        # print(f"new_portifolio: {test}")

        inscription = Inscription.objects.create(
            name=new_name,
            birthday=new_birthday,
            cpf=new_cpf,
            # rg=new_rg,
            age=new_age,
            gender=new_gender,
            gender_other=new_gender_other,
            ethnicity=new_ethnicity,
            ethnicity_other=new_ethnicity_other,
            # address=new_address,
            # address_line_1=new_address_line_1,
            neighberhood=new_neighberhood,
            city=new_city,
            city_other=new_city_other,
            phone=new_phone,
            whatsapp=new_whatsapp,
            email=new_email,
            zipcode=new_zipcode,
            parent=new_parent,
            parent_phone=new_parent_phone,
            scholl_level=new_scholl_level,
            # school=new_school,
            # grade=new_grade,
            # studing=new_studing,
            # course=new_course,
            intern=new_intern,
            intern_time=new_intern_time,
            # looking_work=new_looking_work,
            income=new_income,
            family=new_family,
            deficincy=new_deficincy,
            deficincy_type=new_deficincy_type,
            special_need=new_special_need,
            special_interview=new_special_interview,
            knowloge=new_knowloge,
            knowloge_other=new_knowloge_other,
            prior_inscription=new_prior_inscription,
            prior_course=new_prior_course,
            prior_course_year=new_prior_course_year,
            dedication=new_dedication,
            availability=new_availability,
            tablet=new_tablet,
            # likes_to_draw=new_likes_to_draw,
            frequency=new_frequency,
            group_rating=new_group_rating,
            critics=new_critics,
            previous_work=new_previous_work,
            message=new_message,
            portifolio=new_portifolio,
            file=new_file,
        )

        # Load and render the email template
        subject = 'Inscrição Confirmada'
        html_message = render_to_string('campaings/emails/inscriprionconfirmed.html', {'inscription': inscription})
        plain_message = strip_tags(html_message)
        from_email = 'estudioescoladeanimacao@gmail.com'
        to = new_email

        # Send the email
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        return redirect(InscriptionSucess)

    context = {}
    return render(request, "home.html", context)



def InscriptionSucess(request):
    # specify the model to use
    return render(request, 'sucess.html')



@login_required(login_url='/admin/')
def ListInscriprion(request):
    # context= {'incripitions': incripitions}
    # incripitions = Inscription.objects.all()
    if request.user.is_authenticated:
        inscriptions = Inscription.objects.all().order_by('-created_at')
        print(Inscription.objects.count())
        return render(request, 'list.html', {'inscriptions': inscriptions})
    else:
         return redirect(CreateInscriprion)





# Generate CSV File inscription List
def inscription_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=inscription.csv'

    # Create a csv writer
    writer = csv.writer(response, quoting=csv.QUOTE_ALL)

    # Designate The Model
    inscriptions = Inscription.objects.all().order_by('-created_at')

    # Add column headings to the csv file
    writer.writerow([
        '', 'Nome','cpf', 'Data de nascimento', 'idade',
                 'genero', 'genero outro', 'etinia','etinia outra', 'CEP','bairro', 'Cidade', 'cidade outra', 'telefone', 'whatsapp','email','responsavel', 'telefone responsavel','renda', 'familia renda', 'deficiencia', 'deficiencia qual', 'cuidado especial', 'cuidado entrevista','escolaridade',  'estágio', 'horarios', 'trabalha',
                    'como conheceu', 'como conheceu outros', 'ja se inscreveu', 'curso anterior',
                    'curso anterior ano', 'dedicacao', 'disponibilidade',
                    'tablet', 'desenha', 'avaliacao grupo', 'criticas', 'experiencia anterior', 'mensagem', 'portifolio'
        ])

    # Loop through and output
    for inscription in inscriptions:
        writer.writerow([
            inscription.id -109,
            inscription.name,
            inscription.cpf,
            str(inscription.birthday),
            inscription.age,
            inscription.gender,
            inscription.gender_other,
            inscription.ethnicity,
            inscription.ethnicity_other,
            inscription.zipcode,
            inscription.neighberhood,
            inscription.city,
            inscription.city_other,
            str(inscription.phone),
            str(inscription.whatsapp),
            inscription.email,
            inscription.parent,
            str(inscription.parent_phone),
            inscription.income,
            inscription.family,
            inscription.deficincy,
            inscription.deficincy_type,
            inscription.special_need,
            inscription.special_interview,


            # inscription.rg,
            # inscription.address,
            # inscription.address_line_1,
            # inscription.school,
            # inscription.grade,
            # inscription.studing,
            # inscription.course,
            inscription.scholl_level,
            inscription.intern,
            inscription.intern_time,
            inscription.looking_work,
            inscription.knowloge,
            inscription.knowloge_other,
            inscription.prior_inscription,
            inscription.prior_course,
            inscription.prior_course_year,
            inscription.dedication,
            inscription.availability,
            inscription.tablet,
            # inscription.likes_to_draw,
            inscription.frequency,
            inscription.group_rating,
            inscription.critics,
            inscription.previous_work,
            inscription.message,
            inscription.portifolio
        ])

    return response


from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def inscription_pdf(request, pk):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(1*cm, 1*cm)  # Adjust the text origin to leave space for the logo
    textob.setFont("Helvetica", 10)
    textob.setLeading(14)  # Set the leading to increase line spacing (default is 12)
    textob.maxLineLength = 80
    # Designate The Model
    inscription = Inscription.objects.get(id=pk)
    i = str(inscription.id - 109)

    # Create blank list
    lines = []
    if inscription.name:
        lines.append("Nome: " + inscription.name)
    if inscription.cpf:
        lines.append("CPF: " + str(inscription.cpf))
    if inscription.age:
        lines.append("Idade: " + inscription.age)
    if inscription.birthday:
        lines.append("Data de Nascimento: " + str(inscription.birthday))
    if inscription.gender:
        lines.append("Gênero: " + inscription.gender)
    if inscription.gender_other:
        lines.append("Gênero outro: " + inscription.gender_other)
    if inscription.ethnicity:
        lines.append("Raça: " + inscription.ethnicity)
    if inscription.ethnicity_other:
        lines.append("Etinia outra: " + inscription.ethnicity_other)
    if inscription.zipcode:
        lines.append("CEP: " + inscription.zipcode)
    if inscription.neighberhood:
        lines.append("Bairro: " + inscription.neighberhood)
    if inscription.city:
        lines.append("Cidade: " + inscription.city)
    if inscription.city_other:
        lines.append("Outra cidade: " + inscription.city_other)
    if inscription.phone:
        lines.append("Telefone: " + str(inscription.phone))
    if inscription.whatsapp:
        lines.append("Whatsapp: " + str(inscription.whatsapp))
    if inscription.email:
        lines.append("E-mail: " + str(inscription.email))
    if inscription.scholl_level:
        lines.append("Escolaridade: " + inscription.scholl_level)
    if inscription.income:
        lines.append("Renda familiar: " + inscription.income)
    if inscription.family:
        lines.append("Quantas pessoas usufruem desta renda? " + inscription.family)
    if inscription.intern:
        lines.append("Trabalha ou faz estágio: " + inscription.intern)
    if inscription.intern_time:
        lines.append("Horário Trabalho/Estágio: " + inscription.intern_time)
    if inscription.deficincy:
        lines.append("Possui alguma deficiência? " + inscription.deficincy)
    if inscription.deficincy_type:
        lines.append("Qual deficiencia? " + inscription.deficincy_type)
    if inscription.special_need:
        lines.append("Precisa de atendimento especial? " + inscription.special_need)
    if inscription.special_interview:
        lines.append("Qual atendimento especial? " + inscription.special_interview)
    if inscription.prior_inscription:
        lines.append("Já se inscreveu: " + inscription.prior_inscription)
    if inscription.knowloge:
        lines.append("Como conheceu: " + inscription.knowloge)
    if inscription.knowloge_other:
        lines.append("Conheceu outro lugar: " + inscription.knowloge_other)
    if inscription.prior_course:
        lines.append("Já participou? " + inscription.prior_course)
    if inscription.prior_course_year:
        lines.append("Qual edição? " + str(inscription.prior_course_year))
    if inscription.dedication:
        lines.append("Está disposto a se dedicar com essa frequência? " + inscription.dedication)
    if inscription.tablet:
        lines.append("Como você se sente em relação ao uso do cut-out? " + inscription.tablet)
    if inscription.frequency:
        lines.append("Com que frequência você desenha? " + inscription.frequency)
    if inscription.group_rating:
        lines.append("Numa escala de - à 10, o quanto você gosta de trabalhar em grupo? " + str(inscription.group_rating))
    if inscription.critics:
        lines.append("Como você lida com críticas em relação ao seu trabalho? " + inscription.critics)
    lines.append(" ")
    lines.append("Dos itens abaixo, marque aqueles que você já teve a oportunidade de realizar: ")
    lines.append(" ")
    if inscription.previous_work:
        lines.append("Há outra coisa que você já fez relacionada à animação? " + inscription.previous_work)
    lines.append("  ")
    if inscription.message:
        lines.append("Por que você se interessou em participar do Estúdio Escola? " + inscription.message)
    lines.append(" ")
    if inscription.portifolio:
        lines.append("Possui um local onde divulga o seu trabalho artístico? " + inscription.portifolio)
    lines.append(" ")
    # Loop
    # logo_path = '/home/raphael-2/code/raphael-rbbr/estudioescoladeanimacao/campaings/static/campaings/logo-eea.png'  # --> dev
    logo_path = '/estudioescoladeanimacao/campaings/static/campaings/logo-eea.png'  # --> prod
    c.saveState()
    c.translate(15*cm, 5*cm)  # Translate to the position where you want to place the logo
    c.scale(1, -1)  # Flip the image vertically
    c.drawImage(logo_path, 0, 0, width=7*cm, height=5*cm)  # Draw the image at the origin
    c.restoreState()

    for line in lines:
        wrapped_lines = wrap(line, 120)  # Wrap text to fit within 100 characters per line
        for wrapped_line in wrapped_lines:
            textob.textLine(wrapped_line)

    # Finish Up
    c.drawText(textob)
    c.showPage()

    # Construct the correct file path
    file_path = default_storage.path(inscription.file.name)

    # Check if the file exists
    # if not os.path.exists(file_path):
    #     return HttpResponse("File not found.", status=404)

    # Convert PDF to images using PyMuPDF with lower DPI to avoid DecompressionBombError
    pdf_document = fitz.open(file_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        # Rotate the page by 90 degrees if it is in landscape orientation
        if page.rect.width > page.rect.height:
            page.set_rotation(90)
        pix = page.get_pixmap(dpi=100)  # Set DPI to 150 for lower quality to avoid DecompressionBombError
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
            pix.save(temp_image.name)
            temp_image_path = temp_image.name
        # Get the dimensions of the image
        img_width, img_height = 595, 842
        # Adjust the transformation matrix to flip the image vertically
        c.saveState()
        c.translate(0, A4[1])
        c.scale(1, -1)
        c.drawImage(temp_image_path, 0, 0, width=img_width, height=img_height)
        c.restoreState()
        c.showPage()
        os.remove(temp_image_path)

    c.save()
    buf.seek(0)
    # Return the PDF as a response
    return FileResponse(buf, as_attachment=True, filename=i + '_' + inscription.name + '.pdf')



def inscription_excel(request):
    # Create a workbook and a worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Inscriptions"

    # Add column headings to the worksheet
    columns = ['', 'Nome','cpf', 'Data de nascimento', 'idade',
                 'genero', 'genero outro', 'etinia','etinia outra', 'CEP','bairro', 'Cidade', 'cidade outra', 'telefone', 'whatsapp','email','responsavel', 'telefone responsavel','renda', 'familia renda', 'deficiencia', 'deficiencia qual', 'cuidado especial', 'cuidado entrevista','escolaridade',  'estágio', 'horarios', 'trabalha',
                    'como conheceu', 'como conheceu outros', 'ja se inscreveu', 'curso anterior',
                    'curso anterior ano', 'dedicacao', 'disponibilidade',
                    'tablet', 'desenha', 'avaliacao grupo', 'criticas', 'experiencia anterior', 'mensagem', 'portifolio']
    ws.append(columns)

    # Designate The Model
    inscriptions = Inscription.objects.all().order_by('created_at')
    i = Inscription.objects.all().count()

    # Loop through and output
    for inscription in inscriptions:
        row = [
            inscription.id -109,
            inscription.name,
            inscription.cpf,
            str(inscription.birthday),
            inscription.age,
            inscription.gender,
            inscription.gender_other,
            inscription.ethnicity,
            inscription.ethnicity_other,
            inscription.zipcode,
            inscription.neighberhood,
            inscription.city,
            inscription.city_other,
            str(inscription.phone),
            str(inscription.whatsapp),
            inscription.email,
            inscription.parent,
            str(inscription.parent_phone),
            inscription.income,
            inscription.family,
            inscription.deficincy,
            inscription.deficincy_type,
            inscription.special_need,
            inscription.special_interview,


            # inscription.rg,
            # inscription.address,
            # inscription.address_line_1,
            # inscription.school,
            # inscription.grade,
            # inscription.studing,
            # inscription.course,
            inscription.scholl_level,
            inscription.intern,
            inscription.intern_time,
            inscription.looking_work,
            inscription.knowloge,
            inscription.knowloge_other,
            inscription.prior_inscription,
            inscription.prior_course,
            inscription.prior_course_year,
            inscription.dedication,
            inscription.availability,
            inscription.tablet,
            # inscription.likes_to_draw,
            inscription.frequency,
            inscription.group_rating,
            inscription.critics,
            inscription.previous_work,
            inscription.message,
            inscription.portifolio
        ]
        ws.append(row)

    # Save the workbook to a bytes buffer
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=inscription.xlsx'
    wb.save(response)

    return response


def Return200(request):

    return HttpResponse(status=200)
