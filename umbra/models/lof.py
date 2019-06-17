'''
Take dataset X and run it through the lof algorithm
'''

# Import third party libs
from pyod.models.lof import LOF

__virtualname__ = 'lof'


def __init__(hub):
    hub.models.lof.COMPS = {}


def make_mlo(hub, data, train):
    '''
    Create the Machine Learning Object used for this sequence
    '''
    return LOF(contamination=0.01)


async def run(hub, config, pipe, data, train):
    '''
    Run the lof algorithm on the given dataset
    '''
    if pipe not in hub.models.lof.COMPS:
        hub.models.lof.COMPS[pipe] = {'mlo': hub.models.lof.make_mlo(data, train)}
    mlo = hub.models.lof.COMPS[pipe]['mlo']
    if train:
        print(f'Training {len(train)} datasets')
        mlo.fit(train)
    if data:
        print(f'Predicting {len(data)} datasets')
        ret = mlo.predict(data)
        scores = mlo.decision_function(data)
        return ret
    return []
