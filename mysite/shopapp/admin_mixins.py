from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpResponse, HttpRequest
import csv

class ExportAsCSVMixin:
    def export_as_csv(self, request, queryset):
        meta: Options = self.model._meta
        feild_name = [fields.name for fields in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'
        csv_writer = csv.writer(response)
        csv_writer.writerow(feild_name)
        for obj in queryset:
            csv_writer.writerow([getattr(obj,field) for field in feild_name])
        return response
    export_as_csv.short_description = 'Export selected objects to CSV'