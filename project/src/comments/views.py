from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm
from photos.models import Photo

class PostComment(CreateView):
    model = Comment
    template_name = reverse('photos:photo')
    fields = ('text', )

    def dispatch(self, request, pk = None, *args, **kwargs):
        self.post = get_object_or_404(Photo, id=pk)
        return super(PostComment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostComment, self).get_context_data(**kwargs)
        context['post'] = self.post
        context['form'] = CommentForm()
        return context

'''    def form_valid(self, form):
        if self.user.is_anonymus:
            raise form.ValidationError('You are not registred')
            redirect('mainpage:login')
        return super(PostComment, self).form_valid(form)
'''