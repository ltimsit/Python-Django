import requests, json, dewiki, sys

if __name__=='__main__':

    if len(sys.argv) != 2:
        exit();
    search = sys.argv[1]
    data = {'action': 'query', 'prop': 'extracts', 'format': 'json', 'exintro': '', 'explaintext': '', 'titles': search}
    api_main_path = "https://fr.wikipedia.org/w/api.php"
    r = requests.get(api_main_path, params=data)
    if r.status_code != 200:
        exit("error status code", r.status_code)
    c = json.loads(r.text)
    # c = r.json
    print(c)
    if '-1' in c['query']['pages']:
        exit('page missing')
    for k in c['query']['pages']:
        thrd_key = k;
    text_result = c['query']['pages'][thrd_key]['extract']
    with open(search+'.wiki', "w") as file:
        file.write(text_result)
