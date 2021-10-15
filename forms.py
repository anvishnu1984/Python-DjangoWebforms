from django.forms.models import inlineformset_factory
from .models import Environment, TagVersions

EnvironmentTagVersionsFormset = inlineformset_factory(Environment, TagVersions, fields=('tagnumber',))
