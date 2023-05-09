import random
from django import template
from reviews.models import Review

register = template.Library()


@register.inclusion_tag('common/review.html')
def random_review():
    count = Review.objects.filter(featured=True).count()
    if count > 0:
        while True:
            i = random.randint(0, count-1)
            review = Review.objects.all()[i]
            if review.featured == True:
                return {
                    'review': review
                }
    else:
        return {
            'review': {
                'user': 'Fake Random user.',
                'review':
                'Fake review Very good site. NO FEATURED REVIEWS YET!, to feature any review go to admin page.',
                'created': 'Fake date Yesterday.'
            }
        }
