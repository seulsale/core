from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import pandas as pd


@api_view(['GET'])
def covid_data(request):
    confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

    confirmed_data = pd.read_csv(confirmed_url, error_bad_lines=False)
    deaths_data = pd.read_csv(deaths_url, error_bad_lines=False)
    recovered_data = pd.read_csv(recovered_url, error_bad_lines=False)

    print(confirmed_data)
    print(deaths_data)
    print(recovered_data)

    return Response({"message": "It works"}, HTTP_200_OK)
