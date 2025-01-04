from django.contrib import admin
from django.urls import reverse

from app import models


admin.site.site_header = "Frederick Business Admin"


def link_to_admin_instance(model):
    def instance_link(obj):
        url = reverse(
            "admin:%s_%s_changelist" % (model._meta.app_label, model._meta.model_name),
            args=[obj.id],
        )
        return f'<a href="{url}">{obj}</a>'

    return instance_link


class ListAllFieldsMixin:
    def get_list_display(self, request):
        fields = []
        for field in self.model._meta.get_fields():
            if field.many_to_many:
                continue
            elif field.one_to_many:
                continue
            # elif field.many_to_one:
            #     fields.append(link_to_admin_instance(field.related_model))
            else:
                fields.append(field.name)
        return fields


@admin.register(models.Individual)
class IndividualAdmin(admin.ModelAdmin):
    pass
