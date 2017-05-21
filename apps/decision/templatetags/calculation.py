import json

from django.template import Library


register = Library()


def global_weight(criterion, report):
    criterion_count = criterion.parent.criterion_set.count()
    data = report.criterion_compare[str(criterion.parent.id)]
    criterion_index = 0
    colums = filter(lambda x: x != 'criterion_0',
                    data['main_table'][0])
    for index, column in enumerate(colums):
        if 'criterion_%s' % criterion.id == column:
            criterion_index = index
            break

    w_value = data['w'][criterion_index]
    return json.dumps(round(w_value / criterion_count, 4))


register.filter('global_weight', global_weight)
