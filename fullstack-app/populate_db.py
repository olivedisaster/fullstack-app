import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

api = tradeapi.REST('AKORBK3PUHT6IVABBPQL', 'nRnMWK24fAfNERXbANKVncWddzzweWARqqZ3innA', base_url='https://api.alpaca.markets')
assets = api.list_assets()

for asset in assets:
    print(asset)

#cursor.execute("DELETE FROM stock")

connection.commit()