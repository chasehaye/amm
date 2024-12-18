# Generated by Django 5.0.6 on 2024-08-15 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleEnglish', models.CharField(unique=True)),
                ('titleJpRoman', models.CharField(unique=True)),
                ('titleJpKanj', models.CharField(unique=True)),
                ('description', models.CharField(unique=True)),
                ('genre', models.CharField(unique=True)),
                ('demographic', models.CharField(unique=True)),
                ('animeType', models.CharField(unique=True)),
                ('episodes', models.IntegerField()),
                ('episodeDuration', models.IntegerField()),
                ('premireSeason', models.CharField(choices=[('Spring 1970', 'Spring 1970'), ('Summer 1970', 'Summer 1970'), ('Fall 1970', 'Fall 1970'), ('Winter 1970', 'Winter 1970'), ('Spring 1971', 'Spring 1971'), ('Summer 1971', 'Summer 1971'), ('Fall 1971', 'Fall 1971'), ('Winter 1971', 'Winter 1971'), ('Spring 1972', 'Spring 1972'), ('Summer 1972', 'Summer 1972'), ('Fall 1972', 'Fall 1972'), ('Winter 1972', 'Winter 1972'), ('Spring 1973', 'Spring 1973'), ('Summer 1973', 'Summer 1973'), ('Fall 1973', 'Fall 1973'), ('Winter 1973', 'Winter 1973'), ('Spring 1974', 'Spring 1974'), ('Summer 1974', 'Summer 1974'), ('Fall 1974', 'Fall 1974'), ('Winter 1974', 'Winter 1974'), ('Spring 1975', 'Spring 1975'), ('Summer 1975', 'Summer 1975'), ('Fall 1975', 'Fall 1975'), ('Winter 1975', 'Winter 1975'), ('Spring 1976', 'Spring 1976'), ('Summer 1976', 'Summer 1976'), ('Fall 1976', 'Fall 1976'), ('Winter 1976', 'Winter 1976'), ('Spring 1977', 'Spring 1977'), ('Summer 1977', 'Summer 1977'), ('Fall 1977', 'Fall 1977'), ('Winter 1977', 'Winter 1977'), ('Spring 1978', 'Spring 1978'), ('Summer 1978', 'Summer 1978'), ('Fall 1978', 'Fall 1978'), ('Winter 1978', 'Winter 1978'), ('Spring 1979', 'Spring 1979'), ('Summer 1979', 'Summer 1979'), ('Fall 1979', 'Fall 1979'), ('Winter 1979', 'Winter 1979'), ('Spring 1980', 'Spring 1980'), ('Summer 1980', 'Summer 1980'), ('Fall 1980', 'Fall 1980'), ('Winter 1980', 'Winter 1980'), ('Spring 1981', 'Spring 1981'), ('Summer 1981', 'Summer 1981'), ('Fall 1981', 'Fall 1981'), ('Winter 1981', 'Winter 1981'), ('Spring 1982', 'Spring 1982'), ('Summer 1982', 'Summer 1982'), ('Fall 1982', 'Fall 1982'), ('Winter 1982', 'Winter 1982'), ('Spring 1983', 'Spring 1983'), ('Summer 1983', 'Summer 1983'), ('Fall 1983', 'Fall 1983'), ('Winter 1983', 'Winter 1983'), ('Spring 1984', 'Spring 1984'), ('Summer 1984', 'Summer 1984'), ('Fall 1984', 'Fall 1984'), ('Winter 1984', 'Winter 1984'), ('Spring 1985', 'Spring 1985'), ('Summer 1985', 'Summer 1985'), ('Fall 1985', 'Fall 1985'), ('Winter 1985', 'Winter 1985'), ('Spring 1986', 'Spring 1986'), ('Summer 1986', 'Summer 1986'), ('Fall 1986', 'Fall 1986'), ('Winter 1986', 'Winter 1986'), ('Spring 1987', 'Spring 1987'), ('Summer 1987', 'Summer 1987'), ('Fall 1987', 'Fall 1987'), ('Winter 1987', 'Winter 1987'), ('Spring 1988', 'Spring 1988'), ('Summer 1988', 'Summer 1988'), ('Fall 1988', 'Fall 1988'), ('Winter 1988', 'Winter 1988'), ('Spring 1989', 'Spring 1989'), ('Summer 1989', 'Summer 1989'), ('Fall 1989', 'Fall 1989'), ('Winter 1989', 'Winter 1989'), ('Spring 1990', 'Spring 1990'), ('Summer 1990', 'Summer 1990'), ('Fall 1990', 'Fall 1990'), ('Winter 1990', 'Winter 1990'), ('Spring 1991', 'Spring 1991'), ('Summer 1991', 'Summer 1991'), ('Fall 1991', 'Fall 1991'), ('Winter 1991', 'Winter 1991'), ('Spring 1992', 'Spring 1992'), ('Summer 1992', 'Summer 1992'), ('Fall 1992', 'Fall 1992'), ('Winter 1992', 'Winter 1992'), ('Spring 1993', 'Spring 1993'), ('Summer 1993', 'Summer 1993'), ('Fall 1993', 'Fall 1993'), ('Winter 1993', 'Winter 1993'), ('Spring 1994', 'Spring 1994'), ('Summer 1994', 'Summer 1994'), ('Fall 1994', 'Fall 1994'), ('Winter 1994', 'Winter 1994'), ('Spring 1995', 'Spring 1995'), ('Summer 1995', 'Summer 1995'), ('Fall 1995', 'Fall 1995'), ('Winter 1995', 'Winter 1995'), ('Spring 1996', 'Spring 1996'), ('Summer 1996', 'Summer 1996'), ('Fall 1996', 'Fall 1996'), ('Winter 1996', 'Winter 1996'), ('Spring 1997', 'Spring 1997'), ('Summer 1997', 'Summer 1997'), ('Fall 1997', 'Fall 1997'), ('Winter 1997', 'Winter 1997'), ('Spring 1998', 'Spring 1998'), ('Summer 1998', 'Summer 1998'), ('Fall 1998', 'Fall 1998'), ('Winter 1998', 'Winter 1998'), ('Spring 1999', 'Spring 1999'), ('Summer 1999', 'Summer 1999'), ('Fall 1999', 'Fall 1999'), ('Winter 1999', 'Winter 1999'), ('Spring 2000', 'Spring 2000'), ('Summer 2000', 'Summer 2000'), ('Fall 2000', 'Fall 2000'), ('Winter 2000', 'Winter 2000'), ('Spring 2001', 'Spring 2001'), ('Summer 2001', 'Summer 2001'), ('Fall 2001', 'Fall 2001'), ('Winter 2001', 'Winter 2001'), ('Spring 2002', 'Spring 2002'), ('Summer 2002', 'Summer 2002'), ('Fall 2002', 'Fall 2002'), ('Winter 2002', 'Winter 2002'), ('Spring 2003', 'Spring 2003'), ('Summer 2003', 'Summer 2003'), ('Fall 2003', 'Fall 2003'), ('Winter 2003', 'Winter 2003'), ('Spring 2004', 'Spring 2004'), ('Summer 2004', 'Summer 2004'), ('Fall 2004', 'Fall 2004'), ('Winter 2004', 'Winter 2004'), ('Spring 2005', 'Spring 2005'), ('Summer 2005', 'Summer 2005'), ('Fall 2005', 'Fall 2005'), ('Winter 2005', 'Winter 2005'), ('Spring 2006', 'Spring 2006'), ('Summer 2006', 'Summer 2006'), ('Fall 2006', 'Fall 2006'), ('Winter 2006', 'Winter 2006'), ('Spring 2007', 'Spring 2007'), ('Summer 2007', 'Summer 2007'), ('Fall 2007', 'Fall 2007'), ('Winter 2007', 'Winter 2007'), ('Spring 2008', 'Spring 2008'), ('Summer 2008', 'Summer 2008'), ('Fall 2008', 'Fall 2008'), ('Winter 2008', 'Winter 2008'), ('Spring 2009', 'Spring 2009'), ('Summer 2009', 'Summer 2009'), ('Fall 2009', 'Fall 2009'), ('Winter 2009', 'Winter 2009'), ('Spring 2010', 'Spring 2010'), ('Summer 2010', 'Summer 2010'), ('Fall 2010', 'Fall 2010'), ('Winter 2010', 'Winter 2010'), ('Spring 2011', 'Spring 2011'), ('Summer 2011', 'Summer 2011'), ('Fall 2011', 'Fall 2011'), ('Winter 2011', 'Winter 2011'), ('Spring 2012', 'Spring 2012'), ('Summer 2012', 'Summer 2012'), ('Fall 2012', 'Fall 2012'), ('Winter 2012', 'Winter 2012'), ('Spring 2013', 'Spring 2013'), ('Summer 2013', 'Summer 2013'), ('Fall 2013', 'Fall 2013'), ('Winter 2013', 'Winter 2013'), ('Spring 2014', 'Spring 2014'), ('Summer 2014', 'Summer 2014'), ('Fall 2014', 'Fall 2014'), ('Winter 2014', 'Winter 2014'), ('Spring 2015', 'Spring 2015'), ('Summer 2015', 'Summer 2015'), ('Fall 2015', 'Fall 2015'), ('Winter 2015', 'Winter 2015'), ('Spring 2016', 'Spring 2016'), ('Summer 2016', 'Summer 2016'), ('Fall 2016', 'Fall 2016'), ('Winter 2016', 'Winter 2016'), ('Spring 2017', 'Spring 2017'), ('Summer 2017', 'Summer 2017'), ('Fall 2017', 'Fall 2017'), ('Winter 2017', 'Winter 2017'), ('Spring 2018', 'Spring 2018'), ('Summer 2018', 'Summer 2018'), ('Fall 2018', 'Fall 2018'), ('Winter 2018', 'Winter 2018'), ('Spring 2019', 'Spring 2019'), ('Summer 2019', 'Summer 2019'), ('Fall 2019', 'Fall 2019'), ('Winter 2019', 'Winter 2019'), ('Spring 2020', 'Spring 2020'), ('Summer 2020', 'Summer 2020'), ('Fall 2020', 'Fall 2020'), ('Winter 2020', 'Winter 2020'), ('Spring 2021', 'Spring 2021'), ('Summer 2021', 'Summer 2021'), ('Fall 2021', 'Fall 2021'), ('Winter 2021', 'Winter 2021'), ('Spring 2022', 'Spring 2022'), ('Summer 2022', 'Summer 2022'), ('Fall 2022', 'Fall 2022'), ('Winter 2022', 'Winter 2022'), ('Spring 2023', 'Spring 2023'), ('Summer 2023', 'Summer 2023'), ('Fall 2023', 'Fall 2023'), ('Winter 2023', 'Winter 2023'), ('Spring 2024', 'Spring 2024'), ('Summer 2024', 'Summer 2024'), ('Fall 2024', 'Fall 2024'), ('Winter 2024', 'Winter 2024'), ('Spring 2025', 'Spring 2025'), ('Summer 2025', 'Summer 2025'), ('Fall 2025', 'Fall 2025'), ('Winter 2025', 'Winter 2025'), ('Spring 2026', 'Spring 2026'), ('Summer 2026', 'Summer 2026'), ('Fall 2026', 'Fall 2026'), ('Winter 2026', 'Winter 2026'), ('Spring 2027', 'Spring 2027'), ('Summer 2027', 'Summer 2027'), ('Fall 2027', 'Fall 2027'), ('Winter 2027', 'Winter 2027'), ('Spring 2028', 'Spring 2028'), ('Summer 2028', 'Summer 2028'), ('Fall 2028', 'Fall 2028'), ('Winter 2028', 'Winter 2028'), ('Spring 2029', 'Spring 2029'), ('Summer 2029', 'Summer 2029'), ('Fall 2029', 'Fall 2029'), ('Winter 2029', 'Winter 2029'), ('Spring 2030', 'Spring 2030'), ('Summer 2030', 'Summer 2030'), ('Fall 2030', 'Fall 2030'), ('Winter 2030', 'Winter 2030'), ('Spring 2031', 'Spring 2031'), ('Summer 2031', 'Summer 2031'), ('Fall 2031', 'Fall 2031'), ('Winter 2031', 'Winter 2031'), ('Spring 2032', 'Spring 2032'), ('Summer 2032', 'Summer 2032'), ('Fall 2032', 'Fall 2032'), ('Winter 2032', 'Winter 2032'), ('Spring 2033', 'Spring 2033'), ('Summer 2033', 'Summer 2033'), ('Fall 2033', 'Fall 2033'), ('Winter 2033', 'Winter 2033'), ('Spring 2034', 'Spring 2034'), ('Summer 2034', 'Summer 2034'), ('Fall 2034', 'Fall 2034'), ('Winter 2034', 'Winter 2034'), ('Spring 2035', 'Spring 2035'), ('Summer 2035', 'Summer 2035'), ('Fall 2035', 'Fall 2035'), ('Winter 2035', 'Winter 2035'), ('Spring 2036', 'Spring 2036'), ('Summer 2036', 'Summer 2036'), ('Fall 2036', 'Fall 2036'), ('Winter 2036', 'Winter 2036'), ('Spring 2037', 'Spring 2037'), ('Summer 2037', 'Summer 2037'), ('Fall 2037', 'Fall 2037'), ('Winter 2037', 'Winter 2037'), ('Spring 2038', 'Spring 2038'), ('Summer 2038', 'Summer 2038'), ('Fall 2038', 'Fall 2038'), ('Winter 2038', 'Winter 2038'), ('Spring 2039', 'Spring 2039'), ('Summer 2039', 'Summer 2039'), ('Fall 2039', 'Fall 2039'), ('Winter 2039', 'Winter 2039'), ('Spring 2040', 'Spring 2040'), ('Summer 2040', 'Summer 2040'), ('Fall 2040', 'Fall 2040'), ('Winter 2040', 'Winter 2040'), ('Spring 2041', 'Spring 2041'), ('Summer 2041', 'Summer 2041'), ('Fall 2041', 'Fall 2041'), ('Winter 2041', 'Winter 2041'), ('Spring 2042', 'Spring 2042'), ('Summer 2042', 'Summer 2042'), ('Fall 2042', 'Fall 2042'), ('Winter 2042', 'Winter 2042'), ('Spring 2043', 'Spring 2043'), ('Summer 2043', 'Summer 2043'), ('Fall 2043', 'Fall 2043'), ('Winter 2043', 'Winter 2043'), ('Spring 2044', 'Spring 2044'), ('Summer 2044', 'Summer 2044'), ('Fall 2044', 'Fall 2044'), ('Winter 2044', 'Winter 2044'), ('Spring 2045', 'Spring 2045'), ('Summer 2045', 'Summer 2045'), ('Fall 2045', 'Fall 2045'), ('Winter 2045', 'Winter 2045'), ('Spring 2046', 'Spring 2046'), ('Summer 2046', 'Summer 2046'), ('Fall 2046', 'Fall 2046'), ('Winter 2046', 'Winter 2046'), ('Spring 2047', 'Spring 2047'), ('Summer 2047', 'Summer 2047'), ('Fall 2047', 'Fall 2047'), ('Winter 2047', 'Winter 2047'), ('Spring 2048', 'Spring 2048'), ('Summer 2048', 'Summer 2048'), ('Fall 2048', 'Fall 2048'), ('Winter 2048', 'Winter 2048'), ('Spring 2049', 'Spring 2049'), ('Summer 2049', 'Summer 2049'), ('Fall 2049', 'Fall 2049'), ('Winter 2049', 'Winter 2049'), ('Spring 2050', 'Spring 2050'), ('Summer 2050', 'Summer 2050'), ('Fall 2050', 'Fall 2050'), ('Winter 2050', 'Winter 2050'), ('Spring 2051', 'Spring 2051'), ('Summer 2051', 'Summer 2051'), ('Fall 2051', 'Fall 2051'), ('Winter 2051', 'Winter 2051'), ('Spring 2052', 'Spring 2052'), ('Summer 2052', 'Summer 2052'), ('Fall 2052', 'Fall 2052'), ('Winter 2052', 'Winter 2052'), ('Spring 2053', 'Spring 2053'), ('Summer 2053', 'Summer 2053'), ('Fall 2053', 'Fall 2053'), ('Winter 2053', 'Winter 2053'), ('Spring 2054', 'Spring 2054'), ('Summer 2054', 'Summer 2054'), ('Fall 2054', 'Fall 2054'), ('Winter 2054', 'Winter 2054'), ('Spring 2055', 'Spring 2055'), ('Summer 2055', 'Summer 2055'), ('Fall 2055', 'Fall 2055'), ('Winter 2055', 'Winter 2055'), ('Spring 2056', 'Spring 2056'), ('Summer 2056', 'Summer 2056'), ('Fall 2056', 'Fall 2056'), ('Winter 2056', 'Winter 2056'), ('Spring 2057', 'Spring 2057'), ('Summer 2057', 'Summer 2057'), ('Fall 2057', 'Fall 2057'), ('Winter 2057', 'Winter 2057'), ('Spring 2058', 'Spring 2058'), ('Summer 2058', 'Summer 2058'), ('Fall 2058', 'Fall 2058'), ('Winter 2058', 'Winter 2058'), ('Spring 2059', 'Spring 2059'), ('Summer 2059', 'Summer 2059'), ('Fall 2059', 'Fall 2059'), ('Winter 2059', 'Winter 2059'), ('Spring 2060', 'Spring 2060'), ('Summer 2060', 'Summer 2060'), ('Fall 2060', 'Fall 2060'), ('Winter 2060', 'Winter 2060'), ('Spring 2061', 'Spring 2061'), ('Summer 2061', 'Summer 2061'), ('Fall 2061', 'Fall 2061'), ('Winter 2061', 'Winter 2061'), ('Spring 2062', 'Spring 2062'), ('Summer 2062', 'Summer 2062'), ('Fall 2062', 'Fall 2062'), ('Winter 2062', 'Winter 2062'), ('Spring 2063', 'Spring 2063'), ('Summer 2063', 'Summer 2063'), ('Fall 2063', 'Fall 2063'), ('Winter 2063', 'Winter 2063'), ('Spring 2064', 'Spring 2064'), ('Summer 2064', 'Summer 2064'), ('Fall 2064', 'Fall 2064'), ('Winter 2064', 'Winter 2064'), ('Spring 2065', 'Spring 2065'), ('Summer 2065', 'Summer 2065'), ('Fall 2065', 'Fall 2065'), ('Winter 2065', 'Winter 2065'), ('Spring 2066', 'Spring 2066'), ('Summer 2066', 'Summer 2066'), ('Fall 2066', 'Fall 2066'), ('Winter 2066', 'Winter 2066'), ('Spring 2067', 'Spring 2067'), ('Summer 2067', 'Summer 2067'), ('Fall 2067', 'Fall 2067'), ('Winter 2067', 'Winter 2067'), ('Spring 2068', 'Spring 2068'), ('Summer 2068', 'Summer 2068'), ('Fall 2068', 'Fall 2068'), ('Winter 2068', 'Winter 2068'), ('Spring 2069', 'Spring 2069'), ('Summer 2069', 'Summer 2069'), ('Fall 2069', 'Fall 2069'), ('Winter 2069', 'Winter 2069'), ('Spring 2070', 'Spring 2070'), ('Summer 2070', 'Summer 2070'), ('Fall 2070', 'Fall 2070'), ('Winter 2070', 'Winter 2070')], max_length=20)),
                ('airDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('prequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sequel_anime', to='anime.anime')),
                ('sequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prequel_anime', to='anime.anime')),
            ],
        ),
    ]