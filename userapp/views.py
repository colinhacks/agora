def register(request, *args, **kwargs):
	return render(request, kwargs['template'],{'extension':'logout.html'})# Create your views here.
	