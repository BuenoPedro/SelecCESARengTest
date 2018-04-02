'''
1. Acessar a p?gina (https://www.discourse.org/) - OK
2. Clicar na op??o Demo dispon?vel no menu principal - OK
3. Fazer scroll at? o final da p?gina - OK
4. Imprimir:
a. A descri??o de todos os t?picos fechados (s?o os que tem um cadeado ao lado esquerdo
do t?tulo) - OK
b. Quantidade de itens de cada categoria e dos que n?o possuem categoria - OK
c. O t?tulo do t?pico que cont?m o maior n?mero de views

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

SCROLL_PAUSE_TIME = 0.5

firefox = webdriver.Firefox()
firefox.get('https://www.discourse.org/')

main = firefox.find_element_by_id('main')
demo = main.find_element_by_xpath('.//*[text()[contains(.,"Demo")]]')
demo.click()

time.sleep(3)

firefox.switch_to.window(firefox.window_handles[1])

time.sleep(6)

last_height = firefox.execute_script("return document.body.scrollHeight")

while True:

    firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(SCROLL_PAUSE_TIME)


    new_height = firefox.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


topicos = firefox.find_elements_by_class_name('link-top-line')
for i in range(len(topicos)):
    try:
        cadeado = topicos[i].find_element_by_class_name('fa.fa-lock.d-icon.d-icon-lock')
        #print('passou')
        nome = topicos[i].find_element_by_class_name('title.raw-link.raw-topic-link')
        print(nome.text)
    except NoSuchElementException:
        #print('exception')
        continue

#topicos = firefox.find_elements_by_class_name('topic-list-item.category-discourse.ember-view')

'''
for j in range(len(topicos)):

    try:
        category = topicos[i].find_element_by_class_name('category')
        tipo = category.find_element_by_class_name('category-name')
        print(category.text)
        categorias[category.text] = categorias[category.text] + 1


    except NoSuchElementException:
        print('excecao')
        categorias['none'] = categorias['none'] + 1
'''

nao_categorizado = firefox.find_elements_by_class_name('category-uncategorized')
movies = firefox.find_elements_by_class_name('category-movies')
discourse = firefox.find_elements_by_class_name('category-discourse')
general = firefox.find_elements_by_class_name('category-general')
videos = firefox.find_elements_by_class_name('category-videos')
tech = firefox.find_elements_by_class_name('category-tech')
gaming = firefox.find_elements_by_class_name('category-gaming')
school = firefox.find_elements_by_class_name('category-school')
sports = firefox.find_elements_by_class_name('category-sports')

print('Quantidade de cada categoria: ')
categorias = [
    'Nao categorizado: ' + str(len(nao_categorizado)),
    'Filmes: ' + str(len(movies)),
    'Discursao: ' + str(len(discourse)),
    'Geral: ' + str(len(general)),
    'Videos: ' + str(len(videos)),
    'Tecnologia: ' + str(len(tech)),
    'Jogos: ' + str(len(gaming)),
    'Estudo: ' + str(len(school)),
    'Esportes: ' + str(len(sports))
]

print(categorias)


tpcs = firefox.find_elements_by_class_name('topic-list-item')

maior_numero = 0
nome_tpc = ' '

for j in range(len(tpcs)):
    num_views = tpcs[i].find_element_by_class_name('num.views')
    number = num_views.find_element_by_class_name('number').text
    print(number)
    if(maior_numero < int(number)):
        maior_numero = int(number)
        nome_tpc = tpcs[i].find_element_by_class_name('title.raw-link.raw-topic-link')

print(number)
print(nome_tpc.text)





