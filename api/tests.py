from django.test import TestCase
from .models import Exp, Skills, Projects

# Create your tests here.


class TestTitulo(TestCase):
    """ testing for models"""

    def setUp(self):  # Construye el objeto a verificar
        self.exp = Exp.objects.create(
            title="Desarrollador fullstack",
            team="Python en equipo",
            description="Aplicación web Tipo Marketplace, registro de usuarios, post y compras de usuarios y vendedores desarrollada con Django y Tailwind",
            gitHub="https://github.com/Python-en-equipo/MarketPlace",
            init_date="2018-02-20",
        )
        self.skills = Skills.objects.create(
            name="Django",
            image="nsequecosa.svg",
            description="descripcion",
            order=1
        )
        # self.projects = Projects.objects.create(
        #     name = "Clon de twitter",
        #     date = "2018-02-20",
        #     description = "un clon de twitter construido con tailwind y django",

        #     gitHub =  "url.com",
        #     live =  "url.com",
        #     image =  "url.com",

        #     skills = Projects.objects.get()
        #     )

    def test_Exp_model(self):
        m1 = self.exp
        m2 = self.skills
        self.assertTrue(isinstance(m1, Exp), isinstance(m2, Skills))
