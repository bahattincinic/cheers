from django.http import JsonResponse


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return super(AjaxableResponseMixin, self).form_invalid(form)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        if self.request.is_ajax():
            form.save()
            return JsonResponse(form.data)
        return super(AjaxableResponseMixin, self).form_valid(form)
