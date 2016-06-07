from countries.models import Country
import pandas as pd
from django.utils.termcolors import colorize


def load_countries():
    df = pd.read_csv('https://raw.githubusercontent.com/Valuehorizon/valuehorizon-countries/master/data/data-2016-06-01.csv')
    df = df.fillna("")
    for indexvalue in df.index:

        # Getting raw data from csv
        code2 = df.ix[indexvalue]["Alpha-2 code"]
        code3 = df.ix[indexvalue]["Alpha-3 code"]
        full_name = df.ix[indexvalue]["Full name"]
        if full_name == "":
            full_name = None
        num_code = df.ix[indexvalue]["Numeric code"]
        remark1 = df.ix[indexvalue]["Remark part 1"]
        remark2 = df.ix[indexvalue]["Remark part 2"]
        remark3 = df.ix[indexvalue]["Remark part 3"]
        remarks = df.ix[indexvalue]["Remarks"]
        com_name = df.ix[indexvalue]["Common name"]
        territory = df.ix[indexvalue]["Territory name"]

        # Getting ISO Status
        iso_dict = dict((v, k) for k, v in dict(Country.ISO_STATUS_CHOICES).iteritems())
        iso_raw = df.ix[indexvalue]["Status"]
        iso_stat = iso_dict[iso_raw]

        if df.ix[indexvalue]["Independent"] == "Yes":
            independent = True
        else:
            independent = False

        try:
            # Update data for existing country
            code_check = Country.objects.get(symbol_alpha2_code=code2)
            print "Country Code Already Exists for %s..." % str(com_name)
            code_check.name = full_name
            code_check.symbol_alpha3_code = code3
            code_check.is_independent = independent
            code_check.numeric_code = num_code
            code_check.remark_1 = remark1
            code_check.remark_2 = remark2
            code_check.remark_3 = remark3
            code_check.territory_name = territory
            code_check.iso_status = iso_stat
            code_check.common_name = com_name
            code_check.save()
        except Country.DoesNotExist:
            # Country does not exist..Add new country data
            print colorize("New Country Code Found...Save it!!", fg="red")
            print 'Creating Line'
            country_data = Country(name=full_name,
                                   symbol_alpha2_code=code2,
                                   symbol_alpha3_code=code3,
                                   is_independent=independent,
                                   numeric_code=num_code,
                                   remark_1=remark1,
                                   remark_2=remark2,
                                   remark_3=remark3,
                                   territory_name=territory,
                                   iso_status=iso_stat,
                                   common_name=com_name
                                   )
            print 'Done Creating Line'
            country_data.save()
            print colorize('Done Saving Line', fg="red")
