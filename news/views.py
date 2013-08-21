from .models import Article, Reporter
#from django.views import generic
#from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from polls.models import Poll, Choice


#class IndexView(generic.ListView):
#    template_name = 'news/index.html'
#    context_object_name = 'latest_article_list'

#    def get_queryset(self):
#        """Return the last five published polls."""
#        return Article.objects.all().order_by('-pub_date')


class IndexView(View):
	'''
	Subclased in order to create a view that encompassed different things from different views.
	Very useful when implementing the whole page that needs variety of content.
	'''
	articles_list = Article.objects.all().order_by('-pub_date')
	polls_list = Poll.objects.order_by('-pub_date')
	reporter_list = Reporter.objects.all()
	content = {'latest_article_list': articles_list, 'polls_list': polls_list, 'reporter_list': reporter_list }
	template_name = 'news/index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.content )


	#def post(self, request, *args, **kwargs):
	#	form = self.form_class(request.POST)
	#	if form.is_valid():
	#	# <process form cleaned data>
	#		return HttpResponseRedirect('/success/')
	#	return render(request, self.template_name, {'form': form})
