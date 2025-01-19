from django.contrib.auth.models import User, Permission, Group
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=4)
        #создание группы
        group, created = Group.objects.get_or_create(name='profile_manager')

        permission_profile = Permission.objects.get(
            codename="view_profile",
        )

        permission_logentry = Permission.objects.get(
            codename="view_logentry",
        )
        #присоеденение расреш. к группе
        group.permissions.add(permission_profile)
        #
        #добавления пользователя к группе
        user.groups.add(group)
        #это добвление на прямую разреш пользователю
        user.user_permissions.add(permission_logentry)

        group.save()
        user.save()