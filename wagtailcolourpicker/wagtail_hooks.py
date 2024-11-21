from django.urls import reverse, path, include
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.wagtail_hooks import hooks

from wagtailcolourpicker.conf import get_setting
from wagtailcolourpicker.utils.colour import register_all_colour_features


@hooks.register('register_admin_urls')
def register_admin_urls():
    from wagtailcolourpicker import urls
    return [
        path('wagtailcolourpicker/', include((urls, 'wagtailcolourpicker'))),
    ]


@hooks.register('insert_editor_js')
def insert_editor_js():
    js_includes = format_html(
        "<script>window.chooserUrls.colourChooser = '{0}';</script>",
        reverse('wagtailcolourpicker:chooser')
    )
    return js_includes


@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    # register all colour features
    register_all_colour_features(features)

    # register the color picker
    feature_name = 'textcolour'
    type_ = feature_name.upper()
    icon = get_setting("ICON")
    control = {
        'type': type_,
        'icon':icon,
        'description': _('Text Colour'),
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=[
                'colourpicker/js/chooser.js',
                'colourpicker/js/colourpicker.js',
            ],
            css={
                'all': ['colourpicker/css/colourpicker.css'],
            }
        )
    )

    features.default_features.append(feature_name)
