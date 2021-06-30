from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from api.models import FeatureSet

# Register your models here.


@admin.register(FeatureSet)
class FeatureSetAdmin(ImportExportModelAdmin):
    """
    Feature set admin model
    """
    list_filter = ['sexo', 'ind_empleado',
                   'ind_nuevo'
                   ]
    list_display = ('id', 'sexo', 'ind_empleado',
                   'ind_nuevo')
    search_fields = ('id','sexo', 'ind_empleado',
                   'ind_nuevo')
    