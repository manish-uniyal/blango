from django import template
from django.utils.html import format_html, html_safe

from django.utils.html import escape
from django.utils.safestring import mark_safe
register= template.Library()
from django.contrib.auth import get_user_model
user_model = get_user_model()

#@register.filter
#def author_details(author, current_user):
@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request= context['request']
    post=context['post']

    author=post.author
    current_user=request.user
    
    content=post.content
    slug=post.slug

    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""
    if author == current_user:
        return format_html( " <strong> Me </strong> ")   

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix= format_html('<a href="mailto:{} ">', author.email)
        suffix=   format_html("</a>") 
    else:
        suffix=""
        prefix=""    

    return format_html('{}{}{}{}"slug="{}',prefix, name, suffix,content, slug )

@register.simple_tag
def rows():
    return format_html('<div class="rows">')

@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def col(extra_classes=""):
    return  format_html('<div class="col">',extra_classes)


@register.simple_tag
def endrow():
    return  format_html("</div>")
@register.simple_tag
def endcol():
    return  format_html("</div>")