import pytest
from selene import browser, be, have, by

def test_ya_search_positive():

    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('Курсы тестировщиков'))

def test_ya_search_negative():
        browser.open('https://ya.ru')
        browser.element('[name="text"]').should(be.blank).type('burusuzugu').press_enter()
        browser.element('html').should(have.text('Ничего не нашли'))



