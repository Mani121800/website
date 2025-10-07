# templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_plan_status(feature, plan):
    """
    Returns True if the feature is available for the given plan.
    Assumes that 'feature' is an object and each plan has a boolean attribute
    like `basic`, `silver`, `gold`, or `platinum`.
    """
    if plan == 'basic':
        return feature.basic
    elif plan == 'silver':
        return feature.silver
    elif plan == 'gold':
        return feature.gold
    elif plan == 'platinum':
        return feature.platinum
    return False
