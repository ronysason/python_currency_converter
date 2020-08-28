import requests
import json


def get_rate(from_cur, to_cur):
    try:
        req_rates = requests.get("https://api.exchangeratesapi.io/latest")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    support_rates = json.loads(req_rates.text)['rates'].keys()

    if from_cur not in support_rates or to_cur not in support_rates:
        print("Either one or both of the currencies requested are not available")
        return -1

    api_base_url = "https://api.exchangeratesapi.io/latest?base="
    try:
        req_rate = requests.get(api_base_url + from_cur + "&symbols=" + to_cur)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = json.loads(req_rate.text)

    return response['rates'][to_cur]


def convert(txt_file):
    f = open(txt_file, "r")
    from_cur = f.readline().rstrip()
    to_cur = f.readline().rstrip()

    rate = get_rate(from_cur, to_cur)

    if rate > 0:
        print("Converting from " + from_cur + " to " + to_cur + ":")

        #  converts the rest of file
        for x in f:
            print(float(x) * rate)

    f.close()


convert("input.txt")
