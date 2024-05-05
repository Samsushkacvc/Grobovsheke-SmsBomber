from random import randint, choice


def username():
    templates = [

        f'SEPOLasL{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}',
        f's{randint(1,9999)}jnkfd{randint(1,9999)}jnk{randint(1,9999)}df{randint(1,9999)}',
        f'Ifidf{randint(1,9999)}oie{randint(1,9999)}i{randint(1,9999)}f6{randint(1,9999)}YTvf',
        f'TRCDSysgb{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}{randint(1,9999)}s',
        f'Peev{randint(1,9999)}stY{randint(1,9999)}GSBV{randint(1,9999)}ssz445',

    ]


    return choice(templates)