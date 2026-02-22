from datetime import datetime

METER_YARD = (1.09361/1)
METER_FATHOM = (.546807/1)
METER_KM = (1/1000)
METER_LEAGUE = (1/4828.03)
METER_VERNE = ()

FATHOM_YARD = (2/1) #6 ft to fathom, 3 ft to yrd
FATHOM_METER = (1.829/1)
FATHOM_KM = (1/546.807)
FATHOM_LEAGUE = (1/3000)
FATHOM_VERNE = (1/52800000) #20000 leagues:D


LEAGUE_YARD = (5280/1)
LEAGUE_METER = (4828.03/1)
LEAGUE_FATHOM = (2640/1)
LEAGUE_KM = (4.82803/1)
LEAGUE_VERNE = (1/20000)

VERNE_YARD = (105599960/1)
VERNE_METER = (96560600/1)
VERNE_FATHOM = (52799980/1)
VERNE_KM = (96560.6/1)
VERNE_LEAGUE = (20000/1)


#methane freezes at ~ -182.5^C(-296^F)


def convert_fathoms(metric:float,metric_type:str):
    if metric_type not in ['meter','m','kilometer','km','yard','yd','verne','v','league','lea']:
        return 'Could not convert'
    elif isinstance(metric,float) or isinstance(metric,int):
        pass
    else:
        return 'Invalid metric type'
    fathom_m = None
    if metric_type == 'meter' or metric_type == 'm':
        fathom_m = round(metric*FATHOM_METER,6)
    elif metric_type == 'kilometer' or metric_type == 'km':
        fathom_m = round(metric*FATHOM_KM,6)
    elif metric_type == 'yard' or metric_type == 'yd':
        fathom_m = round(metric*FATHOM_YARD)
    elif metric_type == 'league' or metric_type == 'le':
        fathom_m = round(metric*FATHOM_LEAGUE,6)
    elif metric_type == 'verne' or metric_type == 'v':
        fathom_m = round(metric*FATHOM_VERNE,6)
    else:
        return 'Invalid metric type'
    
    return fathom_m

def convert_leagues(metric:float,metric_type:str):
    if metric_type not in ['meter','m','kilometer','km','yard','yd','fathom','fa','verne','v']:
        return 'Invalid metric type'
    elif isinstance(metric,float) or isinstance(metric,int):
        pass
    else:
        return 'Invalid metric type'
    league_m = None
    if metric_type == 'meter' or metric_type == 'm':
        league_m = round(metric*LEAGUE_METER,6)
    elif metric_type == 'kilometer' or metric_type == 'km':
        league_m = round(metric*LEAGUE_KM,6)
    elif metric_type == 'yard' or metric_type == 'yd':
        league_m = round(metric*LEAGUE_YARD)
    elif metric_type == 'fathom' or metric_type == 'fa':
        league_m = round(metric*LEAGUE_FATHOM,6)
    elif metric_type == 'verne' or metric_type == 'v':
        league_m = round(metric*LEAGUE_VERNE,6)
    else:
        return 'Invalid metric type'
    
    return league_m
    