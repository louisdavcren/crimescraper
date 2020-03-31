from bs4 import BeautifulSoup as bs # BeautifulSoup for scraping HTML
import mechanize          # Mechanize for filling forms
import requests                     

# Mech setup

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("https://data.police.uk/data/")
response = br.response()

# Selecting form
def select_form(form):
    return form.attrs.get('action', None) == '.'

br.select_form(predicate=select_form)

print(response.geturl())

most_recent = '2019-12'
least_recent = '2019-10'
selected_force = 'south-wales'

br.form['date_from'] =   [least_recent]
br.form['date_to']   =   [most_recent]
br.form['forces']    =   [selected_force]

# Submit Form
br.submit()

# outpath = 'C:\Users\lejdc\Downloads'



        $(function() {
                fetch_download('/data/progress/9bc93225-ad44-4dac-951e-795f50954c7e/');
        });
    