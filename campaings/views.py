from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Inscription


def CreateInscriprion(request):
    if request.method == "POST":
        new_name = request.POST.get('first_name')
        new_birthday = request.POST.get('nascimento')
        new_cpf = request.POST.get('cpf')
        new_rg = request.POST.get('rg')
        new_age = request.POST.get('idade')
        new_gender = request.POST.get('genero')
        new_gender_other = request.POST.get('generooutros')
        new_ethnicity = request.POST.get('raca')
        new_ethnicity_other = request.POST.get('racaoutros')
        new_zipcode = request.POST.get('cep')
        new_address = request.POST.get('endereco')
        new_address_line_1 = request.POST.get('complemento')
        new_neighberhood = request.POST.get('bairro')
        new_city = request.POST.get('cidade')
        new_city_other = request.POST.get('outracidade')
        new_phone = request.POST.get('telefone')
        new_whatsapp = request.POST.get('whatsapp')
        new_email = request.POST.get('email')
        new_scholl_level = request.POST.get('escolaridade')
        new_school = request.POST.get('instituicao')
        new_grade = request.POST.get('serie')
        new_studing = request.POST.get('turno')
        new_course = request.POST.get('curso')
        new_parent = request.POST.get('nomeresponsavel')
        new_parent_phone = request.POST.get('telefoneresponsavel')
        new_intern = request.POST.get('estagio')
        new_intern_time = request.POST.get('horarioestagio')
        new_looking_work = request.POST.get('buscaestagio')
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
        new_likes_to_draw = request.POST.get('gostadesenhar')
        new_frequency = request.POST.get('freqdesenho')
        new_group_rating = request.POST.get('trabalharemgrupo')
        new_critics = request.POST.get('criticastrabalgo')
        new_previous_work = request.POST.get('destacaranimacao')
        new_message = request.POST.get('porqueinteresse')
        new_portifolio = request.POST.get('linkportifolio')
        new_file = request.POST.get('desenho')
        Inscription.objects.create(name = new_name,
                                    birthday = new_birthday,
                                    cpf = new_cpf,
                                    rg = new_rg,
                                    age = new_age,
                                    gender = new_gender,
                                    ethnicity = new_ethnicity,
                                    ethnicity_other = new_ethnicity_other,
                                    address = new_address,
                                    address_line_1 = new_address_line_1,
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
                                    school = new_school,
                                    grade = new_grade,
                                    studing = new_studing,
                                    course = new_course,
                                    intern = new_intern,
                                    intern_time = new_intern_time,
                                    looking_work = new_looking_work,
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
                                    dedication = new_dedication,
                                    tablet = new_tablet,
                                    likes_to_draw = new_likes_to_draw,
                                    frequency = new_frequency,
                                    group_rating = new_group_rating,
                                    critics = new_critics,
                                    previous_work = new_previous_work,
                                    message = new_message,
                                    portifolio = new_portifolio,
                                    file = new_file,)
    context= {}
    return render(request, "home.html", context)



def ListInscriprion(request):
    inscriptions = Inscription.objects.all
    # context= {'incripitions': incripitions}
    # incripitions = Inscription.objects.all()

    return render(request, 'list.html', {'inscriptions': inscriptions})
