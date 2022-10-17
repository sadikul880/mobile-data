mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchange_rate': 103.25
}

#  Your Code Starts from here

import random
mobile_dict = mobile_data.get('data')
exchange_rate= mobile_data.get('exchange_rate')

for mobile in mobile_dict:

    mobile_name = mobile.get('name')
    price = mobile.get('price')
    usd = float(price.strip(' USD'))
    bdt = round(usd * exchange_rate)
    country = mobile.get('made')

    template =[
        f'{mobile_name} is made in {country}.This phon is very wonderful.The prize is {usd} USD which is almost equal to {bdt} BDT .',

        f'{mobile_name} is made in {country}.The prize is {usd} USD which is almost equal to {bdt} BDT .',

        f'{mobile_name} is made in {country}.very premium phone.The prize is {usd} USD which is almost equal to {bdt} BDT .',

        f'{mobile_name} is made in {country}.The prize is {usd} USD which is almost equal to {bdt} BDT .',

        f'{mobile_name} is made in {country}.The prize is {usd} USD which is almost equal to {bdt} BDT .',
    ]

    print(random.choice(template))