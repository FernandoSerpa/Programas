from selenium import webdriver
import matplotlib.pyplot as plt

chrome_driver_path = r'C:\Users\ferna\Desktop\Programação\Python\Pycharm\PASTA GERAL\chromedriver.exe'

driver = webdriver.Chrome(executable_path=f'{chrome_driver_path}')
bitcoin = []
dolar = []
euro = []
time = []
x = 1
while True:

    # BITCOIN

    driver.get(r'https://www.google.com/search?client=opera-gx&q=bitcoin&sourceid=opera&ie=UTF-8&oe=UTF-8')
    k = float(driver.find_element_by_xpath(r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
    bitcoin.append(k)

    # DOLAR

    driver.get('https://www.google.com/search?client=opera-gx&q=dolar&sourceid=opera&ie=UTF-8&oe=UTF-8')
    k = float(driver.find_element_by_xpath(r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
    dolar.append(k)

    # EURO

    driver.get('https://www.google.com/search?client=opera-gx&q=euro&sourceid=opera&ie=UTF-8&oe=UTF-8')
    k = float(driver.find_element_by_xpath(r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
    euro.append(k)

    # TEMPO
    time.append(x)
    x += 1

    # GRÁFICO

    plt.ion()
    plt.subplot(221)
    plt.plot(time, bitcoin,color='Green')
    plt.title('Bitcoin')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(time,dolar,color='Blue')
    plt.title('Dolar')
    plt.grid(True)

    plt.subplot(223)
    plt.plot(time,euro,color='Red')
    plt.title('Euro')
    plt.grid(True)

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,wspace=0.5)
    plt.pause(300)
    plt.ioff()
