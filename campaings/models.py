from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
# from cpffield import cpffield
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.urls import reverse_lazy


# from constrainedfilefield.fields import ConstrainedFileField
# DOCUMENT_UPLOAD_ALLOWED_FORMATS = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']




class Inscription(models.Model):
    name = models.CharField(max_length=80, verbose_name=("Nome"), help_text=("NOME COMPLETO (Nome Social para pessoas transgênero):	"))
    ### DATA
    # slug = models.SlugField(("Slug"), max_length=255, unique=True, help_text=("Slug do seu post (para URLs)"))
    created_at = models.DateTimeField(verbose_name="Data_criação", auto_now_add=True)

    birthday = models.DateTimeField(verbose_name="nascimento", null=True)
    cpf = models.PositiveSmallIntegerField(verbose_name="CPF", unique=True,)
    rg = models.PositiveSmallIntegerField(verbose_name="RG",null=False,blank=False)
    # AGE_CHOICES = [
    #     ("15", "anos ou menos"),
    #     ("16", "16"),
    #     ("17", "17"),
    #     ("18", "18"),
    #     ("19", "19"),
    #     ("20", "20"),
    #     ("21", "21"),
    #     ("22", "22"),
    #     ("23", "23"),
    #     ("24", "24"),
    #     ("25", "25 anos ou mais"),
    # ]
    age = models.CharField(max_length=50, default=" ", verbose_name=("idade"),
                             help_text=("Clique para selecionar"))

    # GENDER_CHOICES = [
    #     ("MC", "Mulher cis"),
    #     ("MT", "Mulher trans"),
    #     ("HC", "Homem cis"),
    #     ("HT", "Homem trans"),
    #     ("NB", "Não binário"),
    #     ("OUT", "Outra"),
    # ]
    gender = models.CharField(max_length=50, default=" ", verbose_name=("genero"),
                             help_text=("Clique para selecionar"))
    gender_other = models.CharField(max_length=80, verbose_name=("genero_outro"), default=" ", help_text=("em casa de outro:"), blank=True, null=True)
    # ETHNICITY_CHOICES = [
    #     ("AMA", "Amarelo (oriental)"),
    #     ("BRA", "Branca"),
    #     ("IND", "Indígena (oriundos de comunidades indígenas, aldeadas ou urbanas)"),
    #     ("PAR", "Parda (negra de pele clara)"),
    #     ("PRE", "Preta (negra de pele escura)"),
    #     ("OUT", "Outra"),
    # ]
    ethnicity = models.CharField(max_length=50, default=" ", verbose_name=("etinia"),
                             help_text=("Clique para selecionar"), blank=True, null=True)
    ethnicity_other = models.CharField(max_length=80, default=" ", verbose_name=("etinia"), help_text=("Em caso de outra etinia favor informa-la"), blank=True)
    zipcode = models.CharField(max_length=20, default=" ", null=True, blank=True, help_text="CEP do usuário")
    address = models.CharField(max_length=80, default=" ", verbose_name=("Endereço"), help_text=("Endereço"))
    address_line_1 = models.CharField(max_length=80, default=" ", verbose_name=("Complemento"), help_text=("Complemento"))
    neighberhood = models.CharField(max_length=80, default=" ", verbose_name=("Bairro"), help_text=("Bairro"))
    # CITY_CHOICES = [
    #     ("BEL", "Belford Roxo"),
    #     ("CDM", "Cachoeiras de Macacu"),
    #     ("DUC", "Duque de Caxias"),
    #     ("GUA", "Guapimirim"),
    #     ("ITB", "Itaboraí"),
    #     ("ITG", "Itaguaí"),
    #     ("JAP", "Japeri"),
    #     ("MAG", "Magé"),
    #     ("MAR", "Maricá"),
    #     ("MES", "Mesquita"),
    #     ("NIL", "Nilópolis"),
    #     ("NIT", "Niterói"),
    #     ("NOI", "Nova Iguaçu"),
    #     ("PAR", "Paracambi"),
    #     ("PET", "Petrópolis"),
    #     ("QUE", "Queimados"),
    #     ("RIB", "Rio Bonito"),
    #     ("RJ", ""),
    #     ("SAG", "São Gonçalo"),
    #     ("SAJ", "São João de Meriti"),
    #     ("SER", "Seropédica"),
    #     ("TAN", "Tanguá"),
    #     ("OUT", "Outra"),
    # ]
    city = models.CharField(max_length=50,  default="Rio de Janeiro", verbose_name=("city"),
                             help_text=("Clique para selecionar"))
    city_other = models.CharField(max_length=80, default=" ", verbose_name=("Outra_cidade"), help_text=("Em caso de outra cidade favor informa-la"), blank=True)

    phone = PhoneNumberField(verbose_name="Telefone")
    whatsapp = PhoneNumberField(verbose_name="Whatsapp")
    email = models.EmailField(verbose_name="Email")

    # SCHOOL_LEVEL_CHOICES = [
    #     ("EFIPU", "Ensino Fundamental incompleto em escola pública"),
    #     ("EFIPR", "Ensino Fundamental incompleto em escola particular"),
    #     ("EFCPU", "Ensino Fundamental completo em escola pública"),
    #     ("EFCPR", "Ensino Fundamental completo em escola particular"),
    #     ("EMIPU", "Ensino Médio incompleto em escola pública"),
    #     ("EMIPR", "Ensino Médio incompleto em escola particular"),
    #     ("EMCPU", "Ensino Médio completo em escola pública"),
    #     ("EMCPR", "Ensino Médio completo em escola particular"),
    #     ("ESIPU", "Ensino superior incompleto em instituição pública"),
    #     ("ESIPR", "Ensino superior incompleto em instituição particular"),
    #     ("ESCPU", "Ensino superior completo em instituição pública"),
    #     ("ESCPR", "Ensino superior completo em instituição particular"),
    # ]
    scholl_level = models.CharField(max_length=50, default=" ", verbose_name=("escolaridade"),
                             help_text=("NÍVEL DE ESCOLARIDADE:"))

    school = models.CharField(max_length=80, default=" ", verbose_name=("Escola"), help_text=("INSTITUIÇÃO DE ENSINO:"))
    grade = models.CharField(max_length=80, default=" ", verbose_name=("Série"), help_text=("SE ESTIVER ESTUDANDO NESTE ANO, INFORME SÉRIE / PERÍODO:"))

    # STUDING_CHOICES = [
    #     ("MAN", "manhã"),
    #     ("TAR", "tarde"),
    #     ("NOI", "noite"),
    #     ("INT", "integral"),

    # ]
    studing = models.CharField(max_length=50, default=" ", verbose_name=("período"),
                             help_text=("SE ESTIVER ESTUDANDO NESTE ANO, INFORME SÉRIE / PERÍODO:"),null=False,blank=False)

    course = models.CharField(max_length=80, default=" ", verbose_name=("Curso"), help_text=("CURSO (CASO ESTEJA NA ESCOLA TÉCNICA OU NA FACULDADE):"), blank=True)
    parent = models.CharField(max_length=80, default=" ", verbose_name=("Responsalvel"), help_text=("Nome completo do responsável "), blank=True)
    parent_phone = PhoneNumberField(max_length=50, default=" ", verbose_name="Telefone", blank=True)
    intern = models.CharField(max_length=50, default=" ", verbose_name=("Estágio"), null=False, blank=False)
    intern_time = models.CharField(max_length=80, default=" ", verbose_name=("horarios"), help_text=("CEM QUAIS HORÁRIOS VOCÊ TRABALHA OU FAZ ESTÁGIO? "), blank=True)
    looking_work = models.CharField(max_length=50, default=" ", verbose_name=("trabalho"), null=False, blank=False)

    income = models.CharField(max_length=50, default=" ", verbose_name=("renda"),
                             help_text=("RENDA FAMILIAR MENSAL"),null=False,blank=False)

    family = models.CharField(max_length=50, default="2", verbose_name=("familia"),
                             help_text=("Clique para selecionar"))
    deficincy = models.CharField(max_length=50, default=" ", verbose_name=("deficiente"), null=False, blank=False)
    deficincy_type = models.CharField(max_length=80, default=" ", verbose_name=("deficiencia"), help_text=("VOCÊ POSSUI ALGUM TIPO DE DEFICIÊNCIA? SE SIM, PODERIA NOS DIZER QUAL?"), blank=True)
    special_need = models.CharField(max_length=50, default=" ", verbose_name=("cuidado_especial"), null=False, blank=False)
    special_interview = models.CharField(max_length=80, default=" ", verbose_name=("cuidado_entrevista"), help_text=("SE SIM, PODERIA NOS DIZER QUAL?"), blank=True)

    # KNOWLOGE_CHOICES = [
    #     ("JR", "Jornais/revistas "),
    #     ("SI", "Sites"),
    #     ("FA", "Facebook"),
    #     ("IN", "Instagram"),
    #     ("YT", "YouTube"),
    #     ("TK", "Tik Tok "),
    #     ("TT", "Twitter"),
    #     ("ES", "Escola"),
    #     ("MAI", "E-mail"),
    #     ("WP", "WhatsApp"),
    #     ("OT", "Outros"),

    # ]
    knowloge = models.CharField(max_length=80, default="outros", verbose_name=("conhecia"),
                             help_text=("Clique para selecionar"))
    knowloge_other = models.CharField(max_length=80, default=" ", verbose_name=("conhecimento"), help_text="COMO VOCÊ FICOU SABENDO DAS INSCRIÇÕES PARA O PROCESSO SELETIVO DESTE ANO? ", blank=True)


    # PRIOR_INSCRIPTION_CHOICES = [
    #     ("2012", "2012 "),
    #     ("2013", "2013 "),
    #     ("2014", "2014 "),
    #     ("2015", "2015 "),
    #     ("2016", "2016 "),
    #     ("2017", "2017 "),
    #     ("2018", "2018 "),
    #     ("2019", "2019 "),
    #     ("2020", "2020 "),
    #     ("2021", "2021 "),
    #     ("2022", "2022 "),
    #     ("2023", "2023 "),
    #     ("2024", "2024 "),
    # ]
    prior_inscription = models.CharField(max_length=80,  default=" ", verbose_name=("inscricao_anterior"),
                             help_text=("Clique para selecionar"), null=True, blank=True)

    prior_course = models.CharField(max_length=50, default=" ", verbose_name="curso_anterior", null=True, blank=True)
    prior_course_year = models.CharField(max_length=50, default=" ", verbose_name="curso_anterior", null=True, blank=True)
    dedication = models.CharField(max_length=50, default=" ", verbose_name=("dedicação"), null=True, blank=True)
    # multiplechoices
    # TABLET_CHOICES = [
    #     ("OK", "Estou tranquilo(a)! Já faço uso da tablet e estou confortável com isso."),
    #     ("EX", "Estou animado (a) para aprender mais! Sei utilizar um pouco da tablet mas ainda não domino completamente o uso."),
    #     ("NBW", "Nunca usei mas quero aprender!"),
    #     ("NO", "Nunca usei e não quero aprender a usar."),
    # ]
    tablet = models.CharField(max_length=100,  default="OK", verbose_name=("tablet"),
                             help_text=("Clique para selecionar"))
    likes_to_draw = models.CharField(max_length=50, default=" ", verbose_name=("desenha"), null=False, blank=False)
    # FREQUENCY_CHOICES = [
    #     ("DAY", "Diariamente"),
    #     ("WEK", "Semanalmente"),
    #     ("MON", "Pelo menos uma vez por mês"),
    #     ("RAR", "Raramente desenho"),
    # ]
    frequency = models.CharField(max_length=50, default="MON", verbose_name=("frequencia"),
                             help_text=("Clique para selecionar"))

    group_rating =  models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name=("grupo"), help_text=("Numa escala de 0 à 10, o quanto você gosta de trabalhar em grupo?"))
    critics = models.CharField(max_length=80, verbose_name=("criticas"), help_text=("COMO VOCÊ LIDA COM CRÍTICAS EM RELAÇÃO AO SEU TRABALHO?"))
    # multiple choices
    previous_work = models.CharField(max_length=80, default=" ", verbose_name=("experiencia"), help_text=("HÁ OUTRA COISA QUE VOCÊ JÁ FEZ RELACIONADA À ANIMAÇÃO / AUDIOVISUAL QUE GOSTARIA DE DESTACAR?"))
    message = models.CharField(max_length=80, default=" ", verbose_name=("recado"), help_text=("USE AS LINHAS ABAIXO PARA DAR SEU RECADO: POR QUE VOCÊ SE INTERESSOU EM PARTICIPAR DO ESTÚDIO ESCOLA?"))
    portifolio = models.CharField(max_length=80, default=" ", verbose_name=("portifolio"), help_text=("VOCÊ POSSUI UM LOCAL ONDE DIVULGA SEU TRABALHO ARTÍSTICO? EM CASO AFIRMATIVO COMPARTILHE O LINK COM A GENTE!"))
    file = models.FileField(upload_to='file_uploads/', null=True, blank=True)





# intro = models.TextField(max_length=140, blank=True, null=True, verbose_name=_("Introdução"))
#     content = RichTextUploadingField(max_length=25000, verbose_name=_("Texto"), config_name='awesome_ckeditor', extra_plugins = ['codesnippet'])
#     THEME_CHOICES = [
#         ("OP", "Artigo de opinião"),
#         ("ART", "Matéria"), sf
#         ("CUR", "Curiosidades"),
#         ("TUT", "Tutorial"),
#         ("TIP", "Dicas"),
#         ("CON", "Conceitos básicos"),
#         ("RES", "Recursos úteis"),
#         ("ENT", "Entrevistas"),
#         ("NEW", "Novidades")
#     ]
#     theme = models.CharField(max_length=50, choices=THEME_CHOICES, default="OP", verbose_name=_("Tema do post"),
#                              help_text=_("Clique para selecionar"))
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name="Última modificação", auto_now=True)



    def __str__(self):
        return self.name
