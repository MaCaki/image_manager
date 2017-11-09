from django.views import generic
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from .forms import ImageFieldForm
from .models import Patient, Study


class StudyIndexView(generic.ListView):
    """The landing page for the app is a list of studies to grade for."""
    model = Study
    template_name = 'core/study_index.html'


class StudyDetailView(generic.DetailView):
    model = Study
    template_name = 'core/study_detail.html'


class StudyCreateView(generic.edit.CreateView):
    model = Study
    fields = ['name', 'region', 'description']

    # TODO: check if study name already exists.


class StudyDeleteView(generic.edit.DeleteView):
    model = Study
    success_url = reverse_lazy('core:study-index')


class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = 'core/patient_detail.html'


class PatientCreateView(generic.edit.CreateView):
    model = Patient
    fields = ['uid']

    def get_absolute_url(self):
        """Go back to the study detail page."""
        return reverse('core:study-detail', kwargs={'pk': self.pk})

    def get_form(self):
        form = super(PatientCreateView, self).get_form(self.form_class)
        # artical_id - is a name of foreign key defined the Comment model.
        form.instance.study_id = self.kwargs.get('pk', None)
        return form

    def get_context_data(self, **kwargs):
        """We need to also get the study object and pass it to the template."""
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        # the pk passed to this view is that of the attached study.
        context['study'] = Study.objects.get(pk=self.kwargs.get('pk', None))
        return context

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('file_field')
    #     if form.is_valid():
    #         for f in files:
    #             pass
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class ImageFieldView(generic.edit.FormView):
    # Image editor post.
    # https://conservancy.umn.edu/bitstream/handle/11299/107353/oh375mh.pdf?sequence=1&isAllowed=y

    # https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

    form_class = ImageFieldForm
    template_name = 'upload.html'  # Replace with your template.

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
