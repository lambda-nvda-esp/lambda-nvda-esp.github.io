# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495709808.0598128
_enable_loop = True
_template_filename = '/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/math_helper.tmpl'
_template_uri = 'math_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['math_scripts', 'math_styles_ifposts', 'math_scripts_ifpost', 'math_styles_ifpost', 'math_styles', 'math_scripts_ifposts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_katex:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js" integrity="sha256-ExtbCSBuYA7kq1Pz362ibde9nnsHYPt6JxuxYeZbU+c=" crossorigin="anonymous"></script>\n')
            if katex_auto_render:
                __M_writer('            <script>\n                renderMathInElement(document.body,\n                    {\n                        ')
                __M_writer(str(katex_auto_render))
                __M_writer('\n                    }\n                );\n            </script>\n')
            else:
                __M_writer('            <script>\n                renderMathInElement(document.body);\n            </script>\n')
        else:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML" integrity="sha256-yYfngbEKv4RENfGDvNUqJTqGFcKf31NJEe9OTnnMH3Y=" crossorigin="anonymous"></script>\n')
            if mathjax_config:
                __M_writer('        ')
                __M_writer(str(mathjax_config))
                __M_writer('\n')
            else:
                __M_writer('        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            __M_writer('    ')
            __M_writer(str(math_styles()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            __M_writer('    ')
            __M_writer(str(math_scripts()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            __M_writer('    ')
            __M_writer(str(math_styles()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_katex:
            __M_writer('        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            __M_writer('    ')
            __M_writer(str(math_scripts()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "math_helper.tmpl", "source_encoding": "ascii", "line_map": {"130": 42, "131": 43, "132": 44, "133": 44, "134": 44, "140": 134, "16": 0, "21": 28, "22": 34, "23": 40, "24": 46, "25": 52, "26": 58, "32": 1, "39": 1, "40": 2, "41": 3, "42": 5, "43": 6, "44": 9, "45": 9, "46": 13, "47": 14, "48": 18, "49": 19, "50": 20, "51": 21, "52": 21, "53": 21, "54": 22, "55": 23, "61": 54, "68": 54, "69": 55, "70": 56, "71": 56, "72": 56, "78": 36, "84": 36, "85": 37, "86": 38, "87": 38, "88": 38, "94": 48, "100": 48, "101": 49, "102": 50, "103": 50, "104": 50, "110": 30, "115": 30, "116": 31, "117": 32, "123": 42}, "filename": "/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/math_helper.tmpl"}
__M_END_METADATA
"""
