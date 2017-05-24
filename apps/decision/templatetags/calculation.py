from __future__ import division

import json

from django.template import Library


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
    criterion_count = criterion['parent']['count']
    data = report.criterion_compare[str(criterion['parent']['id'])]
    criterion_index = 0

    columns = filter(lambda x: x != 'criterion_0',
                     data['main_table'][0])
    # get column index from matris
    for index, column in enumerate(columns):
        if 'criterion_%s' % criterion['id'] == column:
            criterion_index = index
            break

    w_value = data['w'][criterion_index]
    return json.dumps(round(w_value / criterion_count, 4))


@register.simple_tag
def criterion_w(criterion, report, index):
    """
    Get W value for given index.
    """
    data = report.supplier_compare[str(criterion['id'])]
    return data['w'][index - 1]


@register.simple_tag
def calculate_supplier_score(report, index):
    """
    Calculate supplier score for given report and index.
    """
    total = 0
    for cr_id, data in report.supplier_compare.items():
        criterion = filter(lambda x: str(x['id']) == str(cr_id),
                           report.get_child_criterions())[0]
        w = float(data['w'][index - 1])
        weight = w * float(global_weight(criterion, report))
        total += weight
    return total


@register.simple_tag
def get_supplier_criterion_score(report, supplier, criterion):
    """
    Vikor Step 1 Calculation.
    """
    result = filter(
        lambda x: x['criterion_id'] == str(criterion['id']) and
        x['supplier_id'] == str(supplier['id']),
        report.criterion_supplier_score)

    if len(result) > 0:
        return result[0]['score']
    return 0


@register.simple_tag
def get_supplier_normalized_criterion_score(report, supplier, criterion):
    """
    Vikor Step 1 Calculation.
    """
    result = filter(
        lambda x: x['criterion_id'] == str(criterion['id']) and
        x['supplier_id'] == str(supplier['id']),
        report.criterion_supplier_score)

    if len(result) > 0:
        score = int(result[0]['score'])
        best = best_criterion_score(report, criterion)
        worst = worst_criterion_score(report, criterion)
        result = float((best - score) / (best - worst))
        return '%.3f' % result
    return 0


@register.simple_tag
def get_supplier_weighted_criterion_score(report, supplier, criterion):
    """
    Vikor Step 1 Calculation.
    """
    normalized = float(get_supplier_normalized_criterion_score(
        report, supplier, criterion))
    w = float(global_weight(criterion, report))
    result = normalized * w
    return '%.3f' % result


@register.simple_tag
def best_criterion_score(report, criterion):
    """
    Vikor Step 1 Calculation.
    """
    max_score = 0
    for item in report.criterion_supplier_score:
        if item['criterion_id'] == str(criterion['id']) and \
                int(item['score']) > max_score:
            max_score = int(item['score'])

    return max_score


@register.simple_tag
def get_si_value(report, supplier):
    """
    Vikor Step 1 Calculation.
    """
    total = 0
    for criterion in report.get_child_criterions():
        total += float(get_supplier_weighted_criterion_score(
            report, supplier, criterion))
    return '%.4f' % total


@register.simple_tag
def get_min_si_value(report):
    """
    Vikor Step 1 Calculation.
    """
    min_value = 0
    for supplier in report.suppliers:
        value = float(get_si_value(report, supplier))
        if min_value == 0 or value < min_value:
            min_value = value
    return '%.4f' % min_value


@register.simple_tag
def get_max_si_value(report):
    """
    Vikor Step 1 Calculation.
    """
    max_value = 0
    for supplier in report.suppliers:
        value = float(get_si_value(report, supplier))
        if value > max_value:
            max_value = value
    return '%.4f' % max_value


@register.simple_tag
def get_min_ri_value(report):
    """
    Vikor Step 1 Calculation.
    """
    min_value = 0
    for supplier in report.suppliers:
        value = float(get_ri_value(report, supplier))
        if min_value == 0 or value < min_value:
            min_value = value
    return '%.4f' % min_value


@register.simple_tag
def get_max_ri_value(report):
    """
    Vikor Step 1 Calculation.
    """
    max_value = 0
    for supplier in report.suppliers:
        value = float(get_ri_value(report, supplier))
        if value > max_value:
            max_value = value
    return '%.4f' % max_value


@register.simple_tag
def get_ri_value(report, supplier):
    """
    Vikor Step 1 Calculation.
    """
    max_value = 0
    for criterion in report.get_child_criterions():
        score = float(get_supplier_weighted_criterion_score(
            report, supplier, criterion))
        if score > max_value:
            max_value = score
    return '%.4f' % max_value


@register.simple_tag
def get_qi_value(report, supplier, weight, min_si, max_si, min_ri, max_ri):
    """
    Vikor Step 1 Calculation.
    """
    si = float(get_si_value(report, supplier))
    ri = float(get_ri_value(report, supplier))
    min_si = float(min_si)
    max_si = float(max_si)
    min_ri = float(min_ri)
    max_ri = float(max_ri)
    total = ((weight * (si - min_si)) / (max_si - min_si)) + \
            (((1 - weight) * (ri - min_ri)) / (max_ri - min_ri))
    return '%.4f' % total


@register.simple_tag
def get_rank(report, supplier, weight):
    return 0


@register.simple_tag
def worst_criterion_score(report, criterion):
    """
    Vikor Step 1 Calculation.
    """
    min_score = 0
    for item in report.criterion_supplier_score:
        if item['criterion_id'] == str(criterion['id']) and \
                (min_score == 0 or int(item['score']) < min_score):
            min_score = int(item['score'])

    return min_score


register.filter('global_weight', global_weight)
