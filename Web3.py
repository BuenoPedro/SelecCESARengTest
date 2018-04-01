from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

firefox = webdriver.Firefox()
firefox.get('http://trivago.com.br/')

campo_busca = firefox.find_element_by_name('sQuery')
campo_busca.send_keys('Natal')

firefox.find_element_by_class_name('horus-btn-search__label').click()

time.sleep(3)

porDistancia = Select(firefox.find_element_by_id('mf-select-sortby'))
porDistancia.select_by_value('133800')

firefox.find_element_by_class_name('horus__btn-detail--roomtype').click()
firefox.find_element_by_xpath("//button[@class='btn__roomtype']").click()

time.sleep(6)

segundo_item = firefox.find_element_by_css_selector(".hotel.item-order__list-item.js_co_item[data-item='2030527']")
segundo_nome = segundo_item.find_element_by_css_selector(".item__name.m-0.jsheadline[itemprop='name']")

stars = segundo_item.find_elements_by_class_name("icon-ic.item__star")
#segundo_item = firefox.find_element_by_css_selector(".item__name.m-0.jsheadline[itemprop='name']")
print(segundo_nome.text)
print(len(stars),'estrelas')








