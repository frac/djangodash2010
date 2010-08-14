from django.template.loader import render_to_string
from django.utils.html import escape
from django.http import HttpResponse
import django.forms as forms


from django.shortcuts import render_to_response
from django.template import RequestContext

class SelectWithPop(forms.Select):
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        extraadd = render_to_string("extra_add.html", {'field': name})
        return html+extraadd

class MultipleSelectWithPop(forms.SelectMultiple):
    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        extraadd = render_to_string("extra_add.html", {'field': name})
        return html+extraadd

def handle_pop_add(request, addForm, field):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError, error:
                newObject = None
            if newObject:
                return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % \
                    (escape(newObject._get_pk_val()), escape(newObject)))

    else:
        form = addForm()

    pageContext = {'form': form, 'field': field}
    return render_to_response("popup_add.html", pageContext,RequestContext(request))
