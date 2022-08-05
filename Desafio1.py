from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


link = 'https://www.grocerycrud.com/v1.x/demo/bootstrap_theme'
Name = 'Teste Sicredi'
Lastname = 'Teste'
ContactFirstName = 'Rodrigo Vargas'
Phone = '5199999999'
AddressLine1 = 'Av Assis Brasil, 3970'
Classificacao = 'Uso Interno'
AddressLine2 =  'Torre D'
City = 'Porto Alegre'
State = 'RS'
PostalCode = '91000-000'
Country = 'Brasil'
CreditLimit = '200'

# Acessar a página https://www.grocerycrud.com/v1.x/demo/bootstrap_theme

navegador = webdriver.Chrome()
navegador.get(link)
navegador.maximize_window()

# Mudar o valor da combo Select version para “Bootstrap V4 Theme”
navegador.find_element(By.ID,'switch-version-select').click()
navegador.find_element(By.XPATH,'/html/body/div[1]/select/option[2]').click()
sleep(2)

# Clicar no botão Add Customer
navegador.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[1]/a').click()

# Preencher os campos do formulário
navegador.find_element(By.ID,'field-customerName').send_keys(Name)
navegador.find_element(By.ID,'field-contactLastName').send_keys(Lastname)
navegador.find_element(By.ID,'field-contactFirstName').send_keys(ContactFirstName)
navegador.find_element(By.ID,'field-phone').send_keys(Phone)
navegador.find_element(By.ID,'field-addressLine1').send_keys(AddressLine1)
navegador.find_element(By.ID,'field-addressLine2').send_keys(AddressLine2)
navegador.find_element(By.ID,'field-city').send_keys(City)
navegador.find_element(By.ID,'field-state').send_keys(State)
navegador.find_element(By.ID,'field-postalCode').send_keys(PostalCode)
navegador.find_element(By.ID,'field-country').send_keys(Country)
navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/form/div[11]/div/div/a/span').click()
sleep(2)
navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/form/div[11]/div/div/div/ul/li[8]').click()
sleep(2)
navegador.find_element(By.ID,'field-creditLimit').send_keys(CreditLimit)

# Clicar no botão Save

navegador.find_element(By.ID,'form-button-save').click()
sleep(3)
navegador.save_screenshot('C:\\Users\\pigsr\\PycharmProjects\\DesafioAutomacaoTesteWeb\\Imagens\imagem.png')
sleep(3)
navegador.close()
