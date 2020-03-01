from models import XRate, init_db

from config import logging, LOGGER_CONFIG

log = logging.getLogger('TestApi')
fh = logging.FileHandler(LOGGER_CONFIG['file'])
fh.setLevel(LOGGER_CONFIG['level'])
fh.setFormatter(LOGGER_CONFIG['formatter'])
log.addHandler(fh)
log.setLevel(LOGGER_CONFIG['level'])

def update_xrates(from_currency, to_currency):
    log.info(f'Started update for: {from_currency} => {to_currency}')
    xrate = XRate.select().where(XRate.from_currency == from_currency,
                                 XRate.to_currency == to_currency).first()
    log.debug(f'rate before: {xrate}')
    xrate.rate += 0.01
    xrate.save()

    log.debug(f'rate after: {xrate}')
    log.info(f'Finished update for: {from_currency} => {to_currency}')
