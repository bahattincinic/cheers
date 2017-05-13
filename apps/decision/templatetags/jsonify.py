import json

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.template import Library


register = Library()


def jsonify(json_data):
    if isinstance(json_data, QuerySet):
        return serialize('json', json_data)
    return json.dumps(json_data)


register.filter('jsonify', jsonify)
