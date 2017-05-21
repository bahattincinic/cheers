import json

from django.template import Library

from criterion.models import Criterion


register = Library()


def global_weight(criterion, report):
    """
    Formula:
    Global Weight = Criterion W value / Criterion Count

    For example:
    W Value = 1
    Criterion Count = 5
    Global Weight = 1 / 5 = 0.2
    """
    criterion_count = criterion.parent.criterion_set.count()
    data = report.criterion_compare[str(criterion.parent.id)]
    criterion_index = 0

    columns = filter(lambda x: x != 'criterion_0',
                     data['main_table'][0])
    # get column index from matris
    for index, column in enumerate(columns):
        if 'criterion_%s' % criterion.id == column:
            criterion_index = index
            break

    w_value = data['w'][criterion_index]
    return json.dumps(round(w_value / criterion_count, 4))


@register.simple_tag
def criterion_w(criterion, report, index):
    """
    Get W value for given index.
    """
    data = report.supplier_compare[str(criterion.id)]
    return data['w'][index - 1]


@register.simple_tag
def calculate_supplier_score(report, index):
    """
    Calculate supplier score for given report and index.
    """
    total = 0
    for cr_id, data in report.supplier_compare.items():
        criterion = Criterion.objects.get(id=cr_id)
        w = float(data['w'][index - 1])
        weight = w * float(global_weight(criterion, report))
        total += weight
    return total


register.filter('global_weight', global_weight)
