from django.conf import settings


SETTINGS_PREFIX = 'WAGTAILCOLOURPICKER'
SETTINGS_DEFAULTS = {
    'COLOURS': {
        'black': '#000000',
        'white': '#ffffff'
    }
}


def get_setting(name):
    setting_key = '{}_{}'.format(SETTINGS_PREFIX, name)
    return getattr(settings, setting_key, "view")
