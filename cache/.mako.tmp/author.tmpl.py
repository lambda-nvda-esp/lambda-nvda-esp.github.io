# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1502358494.6532183
_enable_loop = True
_template_filename = '/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/author.tmpl'
_template_uri = 'author.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="authorpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('            <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        __M_writer('        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(author)))
        __M_writer('\n        </div>\n    </header>\n')
        if posts:
            __M_writer('        <ul class="postlist">\n')
            for post in posts:
                __M_writer('                <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(author)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "author.tmpl", "line_map": {"64": 11, "130": 124, "23": 3, "78": 11, "79": 14, "80": 14, "81": 15, "82": 16, "83": 16, "84": 16, "85": 18, "86": 19, "87": 19, "88": 22, "89": 23, "90": 24, "91": 25, "92": 25, "29": 0, "94": 25, "95": 25, "96": 25, "97": 25, "98": 25, "99": 25, "100": 25, "101": 25, "102": 27, "103": 29, "122": 6, "109": 5, "93": 25, "47": 2, "48": 3, "53": 8, "120": 5, "121": 6, "58": 30, "123": 7, "124": 7}, "source_encoding": "utf-8", "filename": "/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/author.tmpl"}
__M_END_METADATA
"""
