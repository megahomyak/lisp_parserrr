import lark


class Transformer(lark.Transformer):

    # noinspection PyMethodMayBeStatic
    def list(self, elements):
        list_ = []
        for element in elements:
            list_.append(element)
        return list_

    def obj(self, obj):
        try:
            return obj[0].value
        except AttributeError:
            return obj[0]


parser = lark.Lark(r"""
obj: list | WORD
list: "(" [obj ]* ")"
start: (obj )*

%import common.WORD
%import common.WS
%ignore WS
""", transformer=Transformer(), parser="lalr")

if __name__ == '__main__':
    print(parser.parse("(a b c (d e f))\n(fdf idsjfijsd)").children)
