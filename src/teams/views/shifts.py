from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView
from django import forms
from django.contrib.postgres.forms.ranges import RangeWidget
from django.utils import timezone
from django.urls import reverse
from psycopg2.extras import DateTimeTZRange

from camps.mixins import CampViewMixin

from ..models import (
    Team,
    TeamShift,
)


class ShiftListView(LoginRequiredMixin, CampViewMixin, ListView):
    model = TeamShift
    template_name = "shifts/shift_list.html"
    context_object_name = "shifts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(team__slug=self.kwargs['team_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = Team.objects.get(
            camp=self.camp,
            slug=self.kwargs['team_slug']
        )
        return context


def time_choices():
    index = 0
    minute_choices = []
    SHIFT_MINIMUM_LENGTH = 15  # TODO: Maybe this should be configurable per team?
    while index * SHIFT_MINIMUM_LENGTH < 60:
        minutes = int(index * SHIFT_MINIMUM_LENGTH)
        minute_choices.append(minutes)
        index += 1

    time_choices = []
    for hour in range(0, 24):
        for minute in minute_choices:
            choice_label = "{hour:02d}:{minutes:02d}".format(hour=hour, minutes=minute)
            time_choices.append((choice_label, choice_label))

    return time_choices


class ShiftForm(forms.ModelForm):
    class Meta:
        model = TeamShift
        fields = [
            'from_date',
            'from_time',
            'to_date',
            'to_time',
            'people_required'
        ]

    from_date = forms.DateField(
        help_text="Format is YYYY-MM-DD - ie. 2018-08-15"
    )

    from_time = forms.ChoiceField(
        choices=time_choices
    )

    to_date = forms.DateField(
        help_text="Format is YYYY-MM-DD - ie. 2018-08-15"
    )

    to_time = forms.ChoiceField(
        choices=time_choices
    )

    def save(self, commit=True):
        from_string = "{} {}".format(
            self.cleaned_data['from_date'],
            self.cleaned_data['from_time']
        )
        to_string = "{} {}".format(
            self.cleaned_data['to_date'],
            self.cleaned_data['to_time']
        )
        datetime_format = '%Y-%m-%d %H:%M'
        self.instance.shift_range = DateTimeTZRange(
            timezone.datetime.strptime(from_string, datetime_format),
            timezone.datetime.strptime(to_string, datetime_format)
        )
        return super().save(commit=commit)


class ShiftCreateView(LoginRequiredMixin, CampViewMixin, CreateView):
    model = TeamShift
    template_name = "shifts/shift_form.html"
    form_class = ShiftForm

    def form_valid(self, form):
        shift = form.save(commit=False)
        shift.team = Team.objects.get(
            camp=self.camp,
            slug=self.kwargs['team_slug']
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'teams:shift_list',
            kwargs=self.kwargs
        )


class ShiftUpdateView(LoginRequiredMixin, CampViewMixin, UpdateView):
    model = TeamShift
    template_name = "shifts/shift_form.html"

