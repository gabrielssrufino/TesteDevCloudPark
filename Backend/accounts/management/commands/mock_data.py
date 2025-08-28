from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tickets.models import Ticket


class Command(BaseCommand):
    help = "Cria usuários, grupos e permissões de demonstração"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('INICIANDO SCRIPT PARA POPULAR BANCO DE DADOS COM MOCKS'))

        User = get_user_model()

        self.stdout.write(self.style.NOTICE('Criando grupos de usuário'))

        atendente_group, _ = Group.objects.get_or_create(name="Atendente")
        self.stdout.write(self.style.SUCCESS('Grupo "Atendente" criado com sucesso'))

        tecnico_group, _ = Group.objects.get_or_create(name="Tecnico")
        self.stdout.write(self.style.SUCCESS('Grupo "Tecnico" criado com sucesso'))

        self.stdout.write(self.style.NOTICE('Criando permissões para o modelo Ticket'))
        ticket_ct = ContentType.objects.get_for_model(Ticket)

        perms = {
            "view_ticket": Permission.objects.get(codename="view_ticket", content_type=ticket_ct),
            "add_ticket": Permission.objects.get(codename="add_ticket", content_type=ticket_ct),
            "change_ticket": Permission.objects.get(codename="change_ticket", content_type=ticket_ct),
            "delete_ticket": Permission.objects.get(codename="delete_ticket", content_type=ticket_ct),
        }
        self.stdout.write(self.style.SUCCESS('Permissões do Ticket carregadas com sucesso'))

        self.stdout.write(self.style.NOTICE('Associando permissões ao grupo "Atendente"'))
        atendente_group.permissions.set([
            perms["view_ticket"],
            perms["add_ticket"],
            perms["change_ticket"],
        ])
        self.stdout.write(self.style.SUCCESS('Permissões adicionadas ao grupo "Atendente": view, add, change'))

        self.stdout.write(self.style.NOTICE('Associando permissões ao grupo "Tecnico"'))
        tecnico_group.permissions.set(perms.values())
        self.stdout.write(self.style.SUCCESS('odas permissões adicionadas ao grupo "Tecnico"'))

        self.stdout.write(self.style.NOTICE('Criando usuários de teste'))

        if not User.objects.filter(email="atendente@cloudpark.teste").exists():
            atendente = User.objects.create_user(
                username="atendente@cloudpark",
                email="atendente@cloudpark.teste",
                password="123456",
            )
            atendente.groups.add(atendente_group)
            self.stdout.write(self.style.SUCCESS('Usuário "Atendente Demo" criado e adicionado ao grupo Atendente'))
        else:
            self.stdout.write(self.style.WARNING('Usuário "Atendente Demo" já existe'))

        if not User.objects.filter(email="tecnico@cloudpark.teste").exists():
            tecnico = User.objects.create_user(
                username="tecnico@cloudpark",
                email="tecnico@cloudpark.teste",
                password="123456",
            )
            tecnico.groups.add(tecnico_group)
            self.stdout.write(self.style.SUCCESS('Usuário "Técnico Demo" criado e adicionado ao grupo Tecnico'))
        else:
            self.stdout.write(self.style.WARNING('Usuário "Técnico Demo" já existe'))

        self.stdout.write(self.style.SUCCESS('Script finalizado com sucesso! Todos os mocks foram criados'))
