from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import EyelidForm, UploadImageForm
from .models import EyeLid, Patient, Study


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


class EyeLidUploadView(generic.edit.FormView):
    # Image editor post.
    # https://conservancy.umn.edu/bitstream/handle/11299/107353/oh375mh.pdf?sequence=1&isAllowed=y

    # https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

    form_class = UploadImageForm
    template_name = 'core/upload_eyelids.html'

    def get_success_url(self):
        """Go back to the study detail page."""
        patient_id = self.kwargs.get('pk', None)
        return reverse('core:patient-detail', kwargs={'pk': patient_id})

    def get_context_data(self, **kwargs):
        """We need to also get the Patient object."""
        patent_id = self.kwargs.get('pk', None)
        context = super(EyeLidUploadView, self).get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=patent_id)
        return context

    def post(self, request, *args, **kwargs):
        patent_id = self.kwargs.get('pk', None)
        patient = Patient.objects.get(pk=patent_id)
        form = self.get_form(self.form_class)
        image = request.FILES['image']

        if form.is_valid():
            print('Form is Valid')
            eyelid = EyeLid(image=image, patient=patient)
            eyelid.save()
            return self.form_valid(form)

        else:
            print('Form is invalid')
            return self.form_invalid(form)
