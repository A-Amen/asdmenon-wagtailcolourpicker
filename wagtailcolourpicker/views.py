from wagtail.admin.modal_workflow import render_modal_workflow
from wagtailcolourpicker.models import Color
from wagtailcolourpicker.forms import ColourForm
from wagtailcolourpicker.utils.colour import (
    get_feature_name_list,
    
)
from wagtail.admin.admin_url_finder import AdminURLFinder
from django.conf import settings
def chooser(request):
    if request.method == "POST":
        form = ColourForm(request.POST)

        if form.is_valid():
            feature_name = ""
            if form.cleaned_data.get("colour"):
                feature_name = form.cleaned_data.get("colour")

            all_features = get_feature_name_list()

            return render_modal_workflow(
                request,
                None,
                None,
                None,
                json_data={
                    "step": "colour_chosen",
                    "toggled_feature": feature_name,
                    "all_features": all_features,
                },
            )
    else:
        form = ColourForm()
    admin_url = Color.snippet_viewset.breadcrumbs_items[0]['url'] # weird way to get the admin base url.
    snippet_url = Color.snippet_viewset.url_prefix
    return render_modal_workflow(
        request,
        "colourpicker/chooser/chooser.html",
        None,
        {
            "form": form,
            "snippet_url": admin_url + snippet_url,
        },
        json_data={"step": "chooser"},
    )
