from django.db import models


class Estados(models.TextChoices):
    ACRE_AC = "AC"
    ALAGOAS_AL = "AL"
    AMAPA_AP = "AP"
    AMAZONAS_AM = "AM"
    BAHIA_BA = "BA"
    CEARA_CE = "CE"
    DISTRITO_FEDERAL_DF = "DF"
    ESPIRITO_SANTO_ES = "ES"
    GOIAS_GO = "GO"
    MARANHAO_MA = "MA"
    MATO_GROSSO_MT = "MT"
    MATO_GROSSO_DO_SUL_MS = "MS"
    MINAS_GERAIS_MG = "MG"
    PARA_PA = "PA"
    PARAIBA_PB = "PB"
    PARANA_PR = "PR"
    PERNAMBUCO_PE = "PE"
    PIAUI_PI = "PI"
    RIO_DE_JANEIRO_RJ = "RJ"
    RIO_GRANDE_DO_NORTE_RN = "RN"
    RIO_GRANDE_DO_SUL_RS = "RS"
    RONDONIA_RO = "RO"
    RORAIMA_RR = "RR"
    SANTA_CATARINA_SC = "SC"
    SAO_PAULO_SP = "SP"
    SERGIPE_SE = "SE"
    TOCANTINS_TO = "TO"


class Endereco(models.Model):
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=2,
        choices=Estados.choices
    )
    cep = models.IntegerField()
    complemento = models.CharField(max_length=50)
