import threading
import requests
import pandas as pd
import time

start_date = '2024-01-01'
end_date = '2024-12-31'
all_dates = pd.date_range(start=start_date, end=end_date)
formatted_days = all_dates.strftime('%d')
formatted_months = all_dates.strftime('%m')
all_date_formatted = [a+b for a, b in zip(formatted_days, formatted_months)]

def uloz_jmena(datumy, dest):
    with open(dest, 'w') as f:
        for datum in datumy:
            a = requests.get(f"https://svatky.adresa.info/txt?date={datum}")
            f.write(a.text.split(";")[-1])

t = time.time()
uloz_jmena(all_date_formatted, 'prvnich_deset_jmen.txt')
print(f"single thread time: {time.time() -t}")

if __name__ == "__main__":
    t = time.time()
    t1 = threading.Thread(target=uloz_jmena, args=(all_date_formatted[:183],"Prvnich5.txt"))
    t2 = threading.Thread(target=uloz_jmena, args=(all_date_formatted[183:],"Druhych5.txt"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
    print(f"double thread time: {time.time() - t}")