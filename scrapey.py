# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:36:55 2020

@author: joshs
"""
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = 'C:/Users/joshs/scraper/chromedriver.exe'
driver = webdriver.Chrome(path)

def worldOMeter():
    
    url = 'https://www.worldometers.info/coronavirus/usa/maryland/'
    driver.get(url)
    
    
    current_cases_count = driver.find_element_by_xpath("//div[@class='maincounter-number']/span")
    deaths_in_md = driver.find_element_by_xpath("(//div[@class='maincounter-number']/span)[2]")
    current_recovered = driver.find_element_by_xpath("(//div[@class='maincounter-number']/span)[3]")
    
    
    count = current_cases_count.text
    deaths_md = deaths_in_md.text
    recovered = current_recovered.text
    
        
    print("current case count in maryland: "+ count)
    
    print("current deaths in Maryland: " + deaths_md)
    
    print("current recovery cases: " + recovered)
   
    return 0

def cdcGovStats():
    
    
    url2 = 'https://covidtracking.com/data/state/maryland/cases'
    driver.get(url2)
    
    current_cdc_cases = driver.find_element_by_xpath("((//td)[2]/span)[2]")
    cases_today = driver.find_element_by_xpath("((//td)[3]/span)[2]")
    
    todaysCases = cases_today.text
    cdc_total_confirmed = current_cdc_cases.text
    
    
    
    print("cdc's updated numbers for MD: " + cdc_total_confirmed )
   
    print("total calculated new daily cases for MD: " + todaysCases)
    
    return 0

def baltimoreCity_Data():
    
    url3 = 'https://coronavirus.maryland.gov/'
    driver.get(url3)
    
    baltimore_city_cases = driver.find_element_by_xpath("((//table[@class='topBlackBoxTable']/tbody/tr)[4]/td)[2]")
    baltimore_city_deaths = driver.find_element_by_xpath("((//table[@class='topBlackBoxTable']/tbody/tr)[4]/td)[3]")
    
    Baltimore_city = baltimore_city_cases.text
    Baltimore_deaths = baltimore_city_deaths.text
    
    print("Cases Reported By john's Hopkins to date: " + Baltimore_city)
    print("Death's in baltimore to date: " + Baltimore_deaths)
    
    return 0

worldOMeter() 

cdcGovStats()

baltimoreCity_Data()