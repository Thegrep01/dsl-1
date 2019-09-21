class Tree:
    def __init__(self, symbol, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right


G = ['a', 'b', 'c']
tokens = ['|', '.', '(', ')', '*', 'end']


def prep_string(str):
    res = str.split()
    res.append('end')
    return res


def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.symbol)
    print_tree(root.right)


def get_token(token_list, expected):
    if token_list[0] == expected and expected in tokens:
        del token_list[0]
        return True
    else:
        return False


def get_symbol(token_list):
    if get_token(token_list, '('):
        x = get_line(token_list)  # get the subexpression
        get_token(token_list, ')')  # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if x not in G:
            raise Exception('Wrong Expression: symbol ' + x + ' is not in G')
        token_list[0:1] = []
        return Tree(x, None, None)


def get_dot(token_list):
    a = get_symbol(token_list)
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


# tree = Tree('|', Tree('a'), Tree('.', Tree('b'), Tree('*', Tree('c'))))
# print_tree(tree)

token_list = prep_string('a | ( ( b . c ) . a )')
tree = get_line(token_list)
print_tree(tree)