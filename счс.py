from LxmlSoup import  LxmlSoup
import requests
import os

if not os.path.exists('music'):
    os.makedirs('music')

search_url = "https://www.myinstants.com/ru/search/?name=%D0%BC%D0%B5%D0%BC%D1%8B"
original_url = 'https://www.myinstants.com'
html = requests.get(search_url).text
soup = LxmlSoup(html)
buttons = soup.find_all('button', class_ = 'small-button')

for button in buttons:
    url = button.get('onclick').split("'")[1]
    print(original_url+url)
    try:
        response = requests.get(original_url+url,
         stream=True )
        response.raise_for_status()

        filename = os.path.join('music',url.split('/')[1])

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'файл сохронён: {filename}')
    except Exception as error:
        print(f'ООШИБКА ПРИ СКАЧАВАНИИ{url}: {error}')

