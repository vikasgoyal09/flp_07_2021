from django.contrib import admin
from . import models
from django import forms
from django.utils import timezone
now = timezone.now()

# Register your models here.


class GameBoardAdminForm(forms.ModelForm, admin.ModelAdmin):

    class Meta:
        model = models.GameBoard
        fields = "__all__"

    def clean_start_time(self):
        date = self.cleaned_data['start_time']
        if date < now:
            raise forms.ValidationError("start date cannot be in the past!")
        return date

    def clean_end_time(self):
        date = self.cleaned_data['end_time']
        if date < now + timezone.timedelta(minutes=30):
            raise forms.ValidationError(
                "time must be more than 30 minutes from start")
        return date

    def clean_max_players(self):
        max_player = self.cleaned_data['max_players']
        if max_player < 2:
            raise forms.ValidationError("max players must be 2 or more")
        return max_player

    def clean_bank_amount(self):
        bank_amount = self.cleaned_data["bank_amount"]
        if bank_amount < 0:
            raise forms.ValidationError("bank amount cannot be negative")
        return bank_amount

    


@admin.register(models.GameBoard)
class GameBoardAdmin(admin.ModelAdmin):
    #readonly_fields = ('no_of_players',)
    form = GameBoardAdminForm


class GamePlayerAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'user_id', 'scored_credit')
    readonly_fields = ('game_id', 'user_id', 'scored_credit')


admin.site.register(models.GamePlayer, GamePlayerAdmin)
