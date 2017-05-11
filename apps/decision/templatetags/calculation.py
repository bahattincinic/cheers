from django import template

register = template.Library()


@register.simple_tag
def get_supplier_criterion_score(scores, supplier, criterion):
    return scores.get('%s_%s' % (criterion, supplier), 0)
