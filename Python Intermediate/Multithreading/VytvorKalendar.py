import pandas as pd

start_date = '2024-01-01'
end_date = '2024-12-31'
all_dates = pd.date_range(start=start_date, end=end_date)
print(type(all_dates))
formatted_days = all_dates.strftime('%d')
formatted_months = all_dates.strftime('%m')
print(list(formatted_days))
print(list(formatted_months))

all_date_formatted = [a+b for a, b in zip(formatted_days, formatted_months)]
print(all_date_formatted)


#a = requests.get("https://svatky.adresa.info/txt?date=0101")
#print(a.text)

