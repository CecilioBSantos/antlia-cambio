import requests
from datetime import date, timedelta

BCB_PTAX_ENDPOINT = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{d}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
)

def is_business_day(d: date) -> bool:
    return d.weekday() < 5

def previous_business_day(d: date) -> date:
    delta = timedelta(days=1)
    nd = d - delta
    while not is_business_day(nd):
        nd -= delta
    return nd

def fetch_bcb_quote_for_date(d: date):
    d_str = d.strftime('%m-%d-%Y')
    url = BCB_PTAX_ENDPOINT.format(d=d_str)
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    j = resp.json()
    values = j.get('value', [])
    if not values:
        return None
    item = values[0]
    return {
        'cotacaoCompra': float(item.get('cotacaoCompra')),
        'cotacaoVenda': float(item.get('cotacaoVenda')),
        'dataHoraCotacao': item.get('dataHoraCotacao')
    }
