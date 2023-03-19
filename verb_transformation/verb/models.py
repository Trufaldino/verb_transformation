from django.db import models
from django_fsm import FSMIntegerField, transition

class VerbTense(models.Model):
    PRESENT = 1
    PAST = 2
    FUTURE = 3
    TENSE_CHOICES = (
        (PRESENT, 'Present'),
        (PAST, 'Past'),
        (FUTURE, 'Future'),
    )
    
    tense = models.CharField(max_length=50, choices=TENSE_CHOICES)
    state = FSMIntegerField(default=PRESENT)
    verb = models.CharField(max_length=50)
    
    @transition(field=state, source=PRESENT, target=PAST)
    def make_past(self):
        return True
