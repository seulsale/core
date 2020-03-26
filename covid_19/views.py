from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
import pandas as pd
import numpy as np


@api_view(['GET'])
def covid_data(request):
    try:
        confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
        deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
        recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

        confirmed_data = pd.read_csv(confirmed_url, error_bad_lines=False)
        deaths_data = pd.read_csv(deaths_url, error_bad_lines=False)
        recovered_data = pd.read_csv(recovered_url, error_bad_lines=False)

        countries = confirmed_data['Country/Region'].to_numpy()
        hold_data = []
        saved_countries = []

        for country in countries:
            if country not in saved_countries:
                saved_countries.append(country)
                hold_data.append({
                    'name': country,
                    'confirmed': confirmed_data.loc[
                        confirmed_data['Country/Region'] == country, confirmed_data.keys()[-1]].sum(),
                    'deaths': deaths_data.loc[deaths_data['Country/Region'] == country, deaths_data.keys()[-1]].sum(),
                    'recovered': recovered_data.loc[
                        recovered_data['Country/Region'] == country, recovered_data.keys()[-1]].sum(),
                })
        return Response(hold_data, HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            'message': str(e)
        }, HTTP_500_INTERNAL_SERVER_ERROR)
