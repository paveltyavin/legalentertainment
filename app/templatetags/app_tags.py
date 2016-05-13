from django import template
from django.template.base import Node
from django.utils.translation import get_language

register = template.Library()


@register.simple_tag
def text(text_ru, text_en):
    language = get_language()
    if language == 'ru':
        return text_ru
    if language == 'en':
        return text_en
    return ''


class TextBlockNode(Node):
    def __init__(self, nodelist, language):
        self.nodelist = nodelist
        self.language = language

    def render(self, context):
        if self.language == get_language():
            output = self.nodelist.render(context)
            return output
        else:
            return ''


@register.tag("textblock")
def do_text_block(parser, token):
    bits = token.split_contents()
    language = str(parser.compile_filter(bits[1]).var)
    nodelist = parser.parse(('endtextblock',))
    parser.delete_first_token()
    return TextBlockNode(nodelist, language)
