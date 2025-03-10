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



# from reportlab.lib.utils import simpleSplit
# L = simpleSplit(text,canv._fontname,canv._fontsize,maxWidth)

# for t in L:
# canv.drawString(x,y,t)
# y -= canv._leading

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
        new_knowloge = request.POST.get('conheceu[]')
        new_knowloge_other = request.POST.get('conheceuoutros')
        new_prior_inscription = request.POST.get('inscreveu')
        new_prior_course = request.POST.get('participou')
        new_prior_course_year = request.POST.get('qualedicao')
        new_dedication = request.POST.get('frequencia')
        new_tablet = request.POST.get('cutout')
        # new_likes_to_draw = request.POST.get('gostadesenhar')
        new_frequency = request.POST.get('freqdesenho')
        new_group_rating = request.POST.get('trabalharemgrupo')
        new_critics = request.POST.get('criticastrabalgo')
        new_previous_work = request.POST.get('destacaranimacao')
        new_message = request.POST.get('porqueinteresse')
        new_portifolio = request.POST.get('linkportifolio')
        new_file = request.FILES['desenho']
        Inscription.objects.create(
                                    name = new_name,
                                    birthday = new_birthday,
                                    cpf = new_cpf,
                                    # rg = new_rg,
                                    age = new_age,
                                    gender = new_gender,
                                    gender_other = new_gender_other,
                                    ethnicity = new_ethnicity,
                                    ethnicity_other = new_ethnicity_other,
                                    # address = new_address,
                                    # address_line_1 = new_address_line_1,
                                    neighberhood = new_neighberhood,
                                    city = new_city,
                                    city_other = new_city_other,
                                    phone = new_phone,
                                    whatsapp = new_whatsapp,
                                    email = new_email,
                                    zipcode = new_zipcode,
                                    parent = new_parent,
                                    parent_phone = new_parent_phone,
                                    scholl_level = new_scholl_level,
                                    # school = new_school,
                                    # grade = new_grade,
                                    # studing = new_studing,
                                    # course = new_course,
                                    intern = new_intern,
                                    intern_time = new_intern_time,
                                    # looking_work = new_looking_work,
                                    income = new_income,
                                    family = new_family,
                                    deficincy = new_deficincy,
                                    deficincy_type = new_deficincy_type,
                                    special_need = new_special_need,
                                    special_interview = new_special_interview,
                                    knowloge = new_knowloge,
                                    knowloge_other = new_knowloge_other,
                                    prior_inscription = new_prior_inscription,
                                    prior_course = new_prior_course,
                                    prior_course_year = new_prior_course_year,
                                    dedication = new_dedication,
                                    tablet = new_tablet,
                                    # likes_to_draw = new_likes_to_draw,
                                    frequency = new_frequency,
                                    group_rating = new_group_rating,
                                    critics = new_critics,
                                    previous_work = new_previous_work,
                                    message = new_message,
                                    portifolio = new_portifolio,
                                    file = new_file,)
        html = render_to_string('emails/inscriprionconfirmed.html',{
            'name': new_name,
            'email': new_email,
        })
        send_mail(
        "Inscrição realizada com sucesso",
        " ola",
        "from@example.com",
        ["to@example.com"],
        html_message=html,
        fail_silently=False,
        )
        return redirect(InscriptionSucess)

    context= {}
    return render(request, "home.html", context)



def InscriptionSucess(request):
    # specify the model to use
    return render(request, 'sucess.html')



@login_required(login_url='/admin/')
def ListInscriprion(request):
    # context= {'incripitions': incripitions}
    # incripitions = Inscription.objects.all()
    if request.user.is_authenticated:
        inscriptions = Inscription.objects.all
        return render(request, 'list.html', {'inscriptions': inscriptions})
    else:
         return redirect(CreateInscriprion)





# Generate CSV File inscription List
def inscription_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=inscription.xls'

    # Create a csv writer
    writer = csv.writer(response, quoting=csv.QUOTE_ALL)

    # Designate The Model
    inscriptions = Inscription.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Nome', 'idade', 'cpf', 'rg', 'genero', 'genero outro', 'etinia', 'etinia outra', 'email', 'CEP', 'endereço', 'complemento', 'bairro', 'Cidade', 'cidade outra', 'telefone', 'whatsapp', 'escolaridade', 'escola', 'série', 'período', 'curso', 'responsavel', 'telefone responsavel', 'estágio', 'horarios', 'trabalha', 'renda', 'familia renda', 'deficiencia', 'deficiencia qual', 'cuidado especial', 'cuidado entrevista', 'como conheceu', 'como conheceu outros', 'ja se inscreveu', 'curso anterior', 'dedicacao', 'tablet', 'gosta de desenhar', 'frequencia', 'avaliacao grupo', 'criticas', 'experiencia anterior', 'mensagem', 'portifolio'])

    # Loop through and output
    for inscription in inscriptions:
        writer.writerow([
            inscription.name,
            inscription.age,
            inscription.cpf,
            # inscription.rg,
            inscription.gender,
            inscription.gender_other,
            inscription.ethnicity,
            inscription.ethnicity_other,
            inscription.email,
            inscription.zipcode,
            # inscription.address,
            # inscription.address_line_1,
            inscription.neighberhood,
            inscription.city,
            inscription.city_other,
            inscription.phone,
            inscription.whatsapp,
            inscription.scholl_level,
            # inscription.school,
            # inscription.grade,
            # inscription.studing,
            # inscription.course,
            inscription.parent,
            inscription.parent_phone,
            inscription.intern,
            inscription.intern_time,
            inscription.looking_work,
            inscription.income,
            inscription.family,
            inscription.deficincy,
            inscription.deficincy_type,
            inscription.special_need,
            inscription.special_interview,
            inscription.knowloge,
            inscription.knowloge_other,
            inscription.prior_inscription,
            inscription.prior_course,
            inscription.dedication,
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
	textob.setTextOrigin(1*cm, 1*cm)
	textob.setFont("Helvetica", 10)
	textob.maxLineLength=80
	# Designate The Model
	inscription = Inscription.objects.get(id=pk)
	# Create blank list
	lines = []
	lines.append("Nome:" + inscription.name)
	lines.append("CPF:" + str(inscription.cpf))
	# lines.append("RG:" + str(inscription.rg))
	lines.append("Idade:" + inscription.age)
	lines.append("Data de Nascimento: " + str(inscription.birthday))
	lines.append("Gênero: " + inscription.gender)
	lines.append("Gênero outro: " +inscription.gender_other)
	lines.append("Raça: " + inscription.ethnicity)
	lines.append("Etinia outra " +inscription.ethnicity_other)
	lines.append("CEP: " + inscription.zipcode)
	# lines.append("Endereço: " + inscription.address)
	# lines.append("Complemento: " + inscription.address_line_1)
	lines.append("Bairro: " + inscription.neighberhood)
	lines.append("Cidade: " + inscription.city)
	lines.append("Outra cidade " + inscription.city_other)
	lines.append("Telefone: " + str(inscription.phone))
	lines.append("Whatsapp: " + str(inscription.whatsapp))
	lines.append("E-mail: " + str(inscription.email))
	lines.append("Escolaridade: " + inscription.scholl_level)
	# lines.append("Instituição: " + inscription.school)
	# lines.append("Série: " + inscription.grade)
	# lines.append("Turno: " + inscription.studing)
	# lines.append("Curso: " + inscription.course)
	lines.append("Renda familiar: " + inscription.income)
	lines.append("Quantas pessoas usufruem desta renda? " + inscription.family)
	lines.append("Trabalha ou faz estágio: " + inscription.intern)
	lines.append("Horário Trabalho/Estágio: " + inscription.intern_time)
	# lines.append(" " + inscription.looking_work)
	lines.append("Possui alguma deficiência? " + inscription.deficincy)
	lines.append("Qual defiencia? " + inscription.deficincy_type)
	lines.append("Precisa de atendimento especial? " + inscription.special_need)
	lines.append("Qual atendimento especial? " + inscription.special_interview)
	lines.append("Já se inscreveu: " + inscription.prior_inscription)
	lines.append("Como conheceu: " + inscription.knowloge)
	lines.append("Conheceu outro lugar " + inscription.knowloge_other)
	lines.append("Já participou? " + inscription.prior_course)
	lines.append("Qual edição? " + str(inscription.prior_course_year))
	lines.append("Está disposto a se dedicar com essa frequência? " + inscription.dedication)
	lines.append("Qual a disponibilidade de horário? " )
	lines.append("Como você se sente em relação ao uso do cut-out? ")
	lines.append(inscription.tablet)
	# lines.append("Você gosta de desenhar? " + inscription.likes_to_draw)
	lines.append("Com que frequência você desenha? " + inscription.frequency)
	lines.append("Numa escala de - à 10, o quanto você gosta de trabalhar em grupo? " + str(inscription.group_rating))
	lines.append("Como você lida com críticas em relação ao seu trabalho? ")
	lines.append(inscription.critics)
	lines.append(" ")
	lines.append("Dos itens abaixo, marque aqueles que você já teve a oportunidade de realizar: ")
	lines.append(" ")
	lines.append("Há outra coisa que você já fez relacionada à animação? ")
	lines.append(inscription.previous_work)
	lines.append("  ")
	lines.append("Por que você se interessou em participar do Estúdio Escola? ")
	lines.append(inscription.message )
	lines.append(" ")
	lines.append("Possui um local onde divulga o seu trabalho artístico? ")
	lines.append(inscription.portifolio)
	lines.append(" ")
	# Loop
	for line in lines:
		wrapped_lines = wrap(line, 127)  # Wrap text to fit within 100 characters per line
		for wrapped_line in wrapped_lines:
			textob.textLine(wrapped_line)

    # Finish Up
	c.drawText(textob)
	c.showPage()
	print(str(inscription.file.url))
	# images = convert_from_path("/estudioescoladeanimacao" + str(inscription.file.url))

  # Construct the correct file path
	file_path = default_storage.path(inscription.file.name)
	print(file_path)

    # Check if the file exists
	# if not os.path.exists(file_path):
	# 	return HttpResponse("File not found.", status=404)

    # Convert PDF to images
	images = convert_from_path(file_path)
	for image in images:
		with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
			image.save(temp_image, format='JPEG')
			temp_image_path = temp_image.name
        # Get the dimensions of the image
		img_width, img_height = image.size
        # Adjust the transformation matrix to flip the image vertically
		c.saveState()
		c.translate(0, A4[1])
		c.scale(1, -1)
		c.drawImage(temp_image_path, 0, 0, width=A4[0], height=A4[1])
		c.restoreState()
		c.showPage()
		os.remove(temp_image_path)

	c.save()
	buf.seek(0)
    # Return something
	return FileResponse(buf, as_attachment=True, filename=inscription.name +'.pdf')



def Return200(request):

    return HttpResponse(status=200)
