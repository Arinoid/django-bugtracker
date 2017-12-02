from django.shortcuts import redirect, render
from .forms import *


def ticket_index(request, project_id):
    project = Project.objects.get(pk=project_id)

    return render(request, 'tickets/list.html', {
        'project': project,
        'ticket_list': Ticket.objects.filter(project_id=project.pk)
    })


def project_index(request):
    return render(request, 'projects/list.html', {
        'project_list': Project.objects.filter()
    })


def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()

            return redirect('ticket-index', ticket.project_id)

    return render(request, 'tickets/update.html', {
        'project': Project.objects.get(pk=ticket.project_id),
        'object': ticket,
        'form': form,
    })


def ticket_create(request, project_id):
    form = TicketCreateForm()
    if request.method == 'POST':
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.status = Status.objects.get(title='opened')
            ticket.project_id = project_id
            ticket.save()

            return redirect('ticket-index', project_id)

    return render(request, 'tickets/create.html', {
        'project': Project.objects.get(pk=project_id),
        'form': form,
    })


    # class AjaxableResponseMixin(object):
    # """
    # Mixin to add AJAX support to a form.
    # Must be used with an object-based FormView (e.g. CreateView)
    # """
    # def form_invalid(self, form):
    # response = super(AjaxableResponseMixin, self).form_invalid(form)
    # if self.request.is_ajax():
    # return JsonResponse(form.errors, status=400)
    # else:
    # return response
    #
    # def form_valid(self, form):
    # # We make sure to call the parent's form_valid() method because
    # # it might do some processing (in the case of CreateView, it will
    # # call form.save() for example).
    # response = super(AjaxableResponseMixin, self).form_valid(form)
    # if self.request.is_ajax():
    # data = {
    # 'pk': self.object.pk,
    # }
    # return JsonResponse(data)
    # else:
    # return response