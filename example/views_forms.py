from django.urls import reverse
from django.views.generic.edit import UpdateView
from example.models import GiftList
from example.forms import GiftListForm


class PostEditView(UpdateView):
    model = GiftList
    form_class = GiftListForm
    success_url = '/gift_list'
    template_name = 'example/add.html'

    @property
    def success_url(self):
        return reverse('list_gfl')


