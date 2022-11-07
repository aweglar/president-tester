import requests

# set of presidents to test against
PRESIDENTS = {'Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren', 'Harrison',
    'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes',
    'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding',
    'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter',
    'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump', 'Biden'}

# query duckduckgo api
response = requests.get("http://api.duckduckgo.com/?q=presidents of the united states&format=json")
# isolate list of presidents from response
data = response.json()['RelatedTopics']

def test_presence_of_all_presidents():
    # iterate over all presidents
    for i in range(0, len(data)):
        item = data[i]['Text']
        name = item.split("-")[0]

        last_name_list = name.split(" ")
        
        if len(last_name_list) > 1:
            last_name = last_name_list[-2]
            # delete last_name from PRESIDENTS variable if present
            # this tracks which presidents were in response
            if last_name in PRESIDENTS:
                PRESIDENTS.remove(last_name)

    # test fails if set is not empty
    assert(len(PRESIDENTS) == 0)
