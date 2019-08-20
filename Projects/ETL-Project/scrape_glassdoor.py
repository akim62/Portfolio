from splinter import Browser
from bs4 import BeautifulSoup
​
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def create_soup(url):
    browser = init_browser()
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    browser.quit()
    return soup
​
​
def scrape_glassdoor(url):
    #browser = init_browser()
    tech_listings = {}
​
    
    url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=full%20stack%20developer&locT=C&locId=1146798&locKeyword=Irvine,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=25&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=1&remoteWorkType=0"
    #browser.visit(url)

​
    #html = browser.html
    #soup = BeautifulSoup(html, "html.parser")

    soup = create_soup(url)
​
    tech_listings["job"] = soup.find("div", class_="jobHeader").get_text()
    tech_listings["company"] = soup.find("div", class_="jobInfoItem jobEmpolyerName").get_text()
    tech_listings["salary"] = soup.find("span", class_="salaryText").get_text()
    tech_listings["city"] = soup.find("span", class_="subtle loc").get_text()
    tech_listings["easy"] = soup.find("span", class_="easyApply").get_text()
​
    return tech_listings

def scrape_indeed(url):
    #browser = init_browser()
    tech_listings = {}
​
    
    url = "https://www.indeed.com/jobs?q=developer&l=Irvine%2C%20CA&start=10&advn=6908518619934192&vjk=9fc0a07016cd1dbf"
    #browser.visit(url)

​
    #html = browser.html
    #soup = BeautifulSoup(html, "html.parser")

    soup = create_soup(url)
​
    tech_listings["job"] = soup.find("div", class_="title").get_text()
    tech_listings["company"] = soup.find("span", class_="company").get_text()
    tech_listings["salary"] = soup.find("span", class_="salary no-wrap").get_text()
    tech_listings["city"] = soup.find("div", class_="location").get_text()
    tech_listings["easy"] = soup.find("span", class_="iaLabel").get_text()
​
    return tech_listings
