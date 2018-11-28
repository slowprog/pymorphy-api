from django.http import JsonResponse
from api.inflect import PhraseInflector, GRAM_CHOICES
import pymorphy2

def inflect(request):
    phrase = request.GET.get('phrase')
    forms  = request.GET.getlist('forms')
    
    if not phrase:
        return JsonResponse({
            'success' : False,
            'data'    : 'The phrase parameter is not specified.',
        })

    if not forms or forms == ['']:
        return JsonResponse({
            'success' : False,
            'data'    : 'The forms parameter is not specified. Use cases and / or noun-number (https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html#russian-cases).',
        })

    inflector = PhraseInflector(pymorphy2.MorphAnalyzer())
    result    = {}

    for form in forms:
        item = set(form.split(',')) & set(GRAM_CHOICES)
        result[form] = inflector.inflect(phrase, item)

    return JsonResponse({
        'success' : True,
        'data'    : result,
    })
