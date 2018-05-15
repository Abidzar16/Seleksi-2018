# import libraries
import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.bukalapak.com/c/komputer/aksesoris-226/portable-hd?search%5Bcity%5D=&search%5Bcourier%5D=&search%5Bfree_shipping_coverage%5D=&search%5Binstallment%5D=0&search%5Bnew%5D=1&search%5Bpremium_seller%5D=0&search%5Bprice_max%5D=&search%5Bprice_min%5D=400000&search%5Bprovince%5D=&search%5Brating_gte%5D=0&search%5Brating_lte%5D=5&search%5Bsort_by%5D=weekly_sales_ratio%3Adesc&search%5Btodays_deal%5D=0&search%5Btop_seller%5D=0&search%5Bused%5D=0&search%5Bwholesale%5D=0&utf8=%E2%9C%93&view_mode=list'

#pengambilan dan parsing quote_page
page = requests.get(quote_page)
soup = BeautifulSoup(page.content, 'html.parser')

