from random import choice, seed


def random_kid():
    return choice(['girl', 'boy'])


def conditional_probability():
    """ B: Both children are girls
        L: At least one child is a girl
        G: Older child is a girl
    """
    both_girls = 0
    older_girl = 0
    either_girl = 0

    seed(0)
    for _ in range(10000):
        older = random_kid()
        younger = random_kid()

        if older is 'girl':
            older_girl += 1

        if older is 'girl' and younger is 'girl':
            both_girls += 1

        if older is 'girl' or younger is 'girl':
            either_girl += 1

    print('P(B|L) = ' + '{:.3f}'.format(both_girls / either_girl))
    print('P(B|G) = ' + '{:.3f}'.format(both_girls / older_girl))


conditional_probability()
