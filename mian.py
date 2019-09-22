class Tree:
    def __init__(self, symbol, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right


G = ['a', 'b', 'c']
tokens = ['|', '.', '(', ')', '*', 'end']


def prep_string(expression):
    res = []
    expression = expression.replace(' ', '')
    for i in expression:
        res.append(i)
    res.append('end')
    return res


def print_tree(root):
    a = "("
    if root.left is not None:
        a += print_tree(root.left)
    a += " " + root.symbol + " "
    if root.right is not None:
        a += print_tree(root.right)
    a += ')'
    return a


def get_token(token_list, expected):
    if token_list[0] == expected and expected in tokens:
        del token_list[0]
        return True
    else:
        return False


def get_symbol(token_list):
    if get_token(token_list, '('):
        x = get_line(token_list)
        get_token(token_list, ')')
        return x
    else:
        x = token_list[0]
        if x not in G:
            raise Exception('Wrong Expression: symbol ' + x + ' is not in G')
        token_list[0:1] = []
        return Tree(x, None, None)


def get_star(token_list):
    a = get_symbol(token_list)
    if get_token(token_list, '*'):
        return Tree('*', a)
    else:
        return a


def get_dot(token_list):
    a = get_star(token_list)
    if get_token(token_list, '.'):
        b = get_dot(token_list)  # this line changed
        return Tree('.', a, b)
    elif token_list[0] not in tokens and token_list[0] not in G:
        raise Exception('Wrong Expression: symbol ' + token_list[0])
    else:
        return a


def get_line(token_list):
    a = get_dot(token_list)
    if get_token(token_list, '|'):
        b = get_line(token_list)
        return Tree('|', a, b)
    else:
        return a


tree = Tree('|', Tree('a'), Tree('.', Tree('b'), Tree('*', Tree('c'))))
print(print_tree(tree))

token_list = prep_string('a|((b.c).a)*')
tree = get_line(token_list)
print(print_tree(tree))
