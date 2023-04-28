import requests
from bs4 import BeautifulSoup

base_url = 'https://lista.mercadolivre.com.br/'

product_name_search = input('Qual produto você deseja encontrar? ')

response = requests.get(base_url + product_name_search)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class': 'ui-search-result__content-wrapper shops__result-content-wrapper'})\
    or print('Nenhum resultado encontrado durante a busca.')

for product in products:
    title = product.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})

    link = product.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
    
    real = product.find('span', attrs={'class': 'price-tag-fraction'})
    
    centavos = product.find('span', attrs={'class': 'price-tag-cents'})
    
    print("Título do produto:", title.text)
    print("Link do produto:", link['href'])
    
    print("Preço do produto: R$", real.text) if (centavos) == None else\
        print("Preço do produto: R$", real.text + ',' + centavos.text)
    
    print('\n')
