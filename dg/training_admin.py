from django.contrib.admin.sites import AdminSite

from trainings.admin import TrainingAdmin
from trainings.models import Donor, Module, Trainer, Trainee, Training


class TrainingsAdmin(AdminSite):

    def has_permission(self, request):
        return request.user.is_active

training_admin = TrainingsAdmin(name="admin_training")

training_admin.register(Training, TrainingAdmin)
training_admin.register(Donor)
training_admin.register(Module)
training_admin.register(Trainer)
training_admin.register(Trainee)
