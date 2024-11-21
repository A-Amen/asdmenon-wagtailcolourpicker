from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtailcolourpicker.conf import get_setting
from wagtailcolourpicker.models import Color

def get_colour_choices():
    colors = Color.objects.all()
    return tuple((color.color_name, color.color) for color in colors)


# def get_feature_name(name):
#     feature = 'colour_%s' % name
#     return feature


# def get_feature_name_upper(name):
#     return get_feature_name(name).upper()

def get_colour_code(name):
    try:
        return Color.objects.get(color_name=name).color
    except Color.DoesNotExist:
        print(f"Color {name} does not exist ")
    return ""

def get_feature_name_list():
    return [color.color_name for color in Color.objects.all()]


def register_color_feature(name, colour, features):
    feature_name = name.upper()
    type_ = name
    tag = 'span'
    detection = '%s[style="color: %s;"]' % (tag, colour)

    control = {
        'type': name,
        'description': colour,
        'style': {'color': colour}
    }
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {detection: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'style': {
                            'color': colour
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_colour_features(features):
    for color in Color.objects.all():
        register_color_feature(color.color_name, color.color, features)


# def get_list_colour_features_name():
#     """
#     Add list names into your
#     models.py RichTextField(features=[get_list_features_name()]
#     """
#     list_features_name = list()

#     for name, colour in get_setting('COLOURS').items():
#         name_feature = get_feature_name(name)
#         list_features_name.append(name_feature)
#     return list_features_name
