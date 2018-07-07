# from django.urls import reverse
# from django.views import generic
# from django.views.generic.edit import FormMixin
#
#
# class ListCreateView(FormMixin, generic.ListView):
#     model = None
#     form_class = None
#
#     #
#
#     def get_success_url(self):
#         return reverse('author-detail', kwargs={'pk': self.object.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         # Here, we would record the user's interest using the message
#         # passed in form.cleaned_data['message']
#         return super().form_valid(form)
