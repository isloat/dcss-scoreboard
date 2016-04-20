"""Defines useful constants."""

PLAYABLE_RACES = {'Ce', 'DD', 'DE', 'Dg', 'Dr', 'Ds', 'Fe', 'Fo', 'Gh', 'Gr',
                  'HE', 'HO', 'Ha', 'Hu', 'Ko', 'Mf', 'Mi', 'Mu', 'Na', 'Op',
                  'Og', 'Sp', 'Te', 'Tr', 'VS', 'Vp'}
PLAYABLE_ROLES = {'AE', 'AK', 'AM', 'Ar', 'As', 'Be', 'CK', 'Cj', 'EE', 'En',
                  'FE', 'Fi', 'Gl', 'Hu', 'IE', 'Mo', 'Ne', 'Sk', 'Su', 'Tm',
                  'VM', 'Wn', 'Wr', 'Wz'}
PLAYABLE_GODS = {'Ashenzari', 'Atheist', 'Beogh', 'Cheibriados', 'Dithmenos',
                 'Elyvilon', 'Fedhas', 'Gozag', 'Jiyva', 'Kikubaaqudgha',
                 'Lugonu', 'Makhleb', 'Nemelex Xobeh', 'Okawaru', 'Pakellas',
                 'Qazlal', 'Ru', 'Sif Muna', 'the Shining One', 'Trog',
                 'Vehumet', 'Xom', 'Yredelemnul', 'Zin'}
GOD_NAME_FIXUPS = {
    'The Shining One': 'the Shining One',
    'Dithmengos': "Dithmenos"
}
RACE_TO_GREAT_RACE = {'Ce': 'greatcentaur',
                      'DD': 'greatdeepdwarf',
                      'DE': 'greatdeepelf',
                      'Dg': 'greatdemigod',
                      'Ds': 'greatdemonspawn',
                      'Dr': 'greatdraconian',
                      'Fe': 'greatfelid',
                      'Fo': 'greatformicid',
                      'Gh': 'greatghoul',
                      'Gr': 'greatgargoyle',
                      'HE': 'greathighelf',
                      'HO': 'greathillorc',
                      'Ha': 'greathalfling',
                      'Hu': 'greathuman',
                      'Ko': 'greatkobold',
                      'Mf': 'greatmerfolk',
                      'Mi': 'greatminotaur',
                      'Mu': 'greatmummy',
                      'Na': 'greatnaga',
                      'Op': 'greatoctopode',
                      'Og': 'greatogre',
                      'Sp': 'greatspriggan',
                      'Te': 'greattengu',
                      'Tr': 'greattroll',
                      'VS': 'greatvinestalker',
                      'Vp': 'greatvampire'}
ROLE_TO_GREAT_ROLE = {'AE': 'greatairelementalist',
                      'AK': 'greatabyssalknight',
                      'AM': 'greatarcanemarksman',
                      'Ar': 'greatartificer',
                      'As': 'greatassassin',
                      'Be': 'greatberserker',
                      'CK': 'greatchaosknight',
                      'Cj': 'greatconjurer',
                      'DK': 'greatdeathknight',
                      'EE': 'greatearthelementalist',
                      'En': 'greatenchanter',
                      'FE': 'greatfireelementalist',
                      'Fi': 'greatfighter',
                      'Gl': 'greatgladiator',
                      'He': 'greathealer',
                      'Hu': 'greathunter',
                      'IE': 'greaticeelementalist',
                      'Mo': 'greatmonk',
                      'Ne': 'greatnecromancer',
                      'Sk': 'greatskald',
                      'Su': 'greatsummoner',
                      'Tm': 'greattransmuter',
                      'VM': 'greatvenommage',
                      'Wn': 'greatwanderer',
                      'Wr': 'greatwarper',
                      'Wz': 'greatwizard'}
MANUAL_ACHIEVEMENTS = {
    'comborobin': {
        'greatestplayer': True
    },
    'Stabwound': {
        '0.4_winner': True
    },
    '78291': {
        '0.5_winner': True
    },
    'elliptic': {
        '0.7_winner': True,
        '0.10_winner': True
    },
    'mikee': {
        '0.8_winner': True
    },
    'theglow': {
        '0.9_winner': True,
        '0.11_winner': True
    },
    'jeanjacques': {
        '0.12_winner': True
    },
    'bmfx': {
        '0.13_winner': True
    },
    'Tolias': {
        '0.14_winner': True,
        '0.15_winner': True
    },
    'DrKe': {
        '0.16_winner': True
    },
    'cosmonaut': {
        '0.17_winner': True
    }
}
MULTIPROCESSING_PROCESSES = 1
RECENT_GAMES_LENGTH = 10
MIN_DUR_RECORD_LENGTH = 5
MIN_TURN_RECORD_LENGTH = 5
MAX_SCORE_RECORD_LENGTH = 10