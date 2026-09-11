import fec

end_url = '/v1/candidates/totals/'
base_parameters = {
    'per_page': 100,
    'election_year': 2026
}
dedupe_columns = 'candidate_id'
csv_name = 'candidate_totals'

fec.fec_api_pull(end_url, base_parameters, dedupe_columns, csv_name)