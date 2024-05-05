from random import randint, choice


def email():
    templates = [

        f'{randint(1,9999)}qwerty{randint(1,9999)}poplok{randint(1,9999)}',
        f'asd{randint(1,9999)}vdiu{randint(1,9999)}gv{randint(1,9999)}uhn',
        f'kmjnhgfds{randint(1,9999)}eefcx{randint(1,9999)}9841fd{randint(1,9999)}1b',
        f'{randint(1,9999)}rftfg{randint(1,9999)}xcvm{randint(1,9999)}7pwgs',
        f'g{randint(1,9999)}y{randint(1,9999)}u{randint(1,9999)}i{randint(1,9999)}werdf',
        f'{randint(1,9999)}etrdg{randint(1,9999)}Dxvjoj{randint(1,9999)}b{randint(1,9999)}98',
        f'poo{randint(1,9999)}hqazh{randint(1,9999)}cxbvc845vfdvfbbdfs{randint(1,9999)}',
        f'l{randint(1,9999)}h{randint(1,9999)}r{randint(1,9999)}y{randint(1,9999)}i{randint(1,9999)}f{randint(1,9999)}d{randint(1,9999)}45dfser',
        f'portdfcv{randint(1,9999)}CTRP{randint(1,9999)}458745{randint(1,9999)}d',
        f'wsexrctfybgu{randint(1,9999)}fyguhmio{randint(1,9999)}zwsxedcrfvgbynhu{randint(1,9999)}drftghuji87',

    ]


    return f'{choice(templates)}@gmail.com'