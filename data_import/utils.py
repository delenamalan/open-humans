from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from .models import BaseDataFile


def app_name_to_data_file_model(app_name):
    """
    Return DataFile model corresponding to a source name.

    DataFile modules subclassed from data_import.BaseDataFile will have paths
    determined by their app name (see data_import.models.get_upload_path). This
    allows us to determine the originating app and model, given the file's
    storage path.
    """
    for app_config in apps.get_app_configs():
        app_config_name = app_config.name.split('.')[-1]

        # Continue unless the file path matches the app's name.
        if app_config_name != app_name:
            continue

        for model in app_config.get_models():
            if issubclass(model, BaseDataFile):
                return model


def app_name_to_content_type(app_name):
    """
    Search all DataFile objects for match, return (ContentType, object_id)

    This uses file_path_to_data_file_model to determine the appropriate model,
    then finds the matching object for that model.
    """
    model = app_name_to_data_file_model(app_name)
    model_type = ContentType.objects.get_for_model(model)

    return (model, model_type)
