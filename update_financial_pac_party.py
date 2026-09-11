import fec

end_url = '/v1/totals/pac-party/'
base_parameters = {
    'per_page': 100,
    'cycle': 2026
}
dedupe_columns = None
csv_name = 'data_financial_pac_party.csv'

fec.fec_api_pull(end_url, base_parameters, dedupe_columns, csv_name)