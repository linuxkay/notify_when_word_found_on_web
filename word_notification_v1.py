#! python3
# Original code author at https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45
import bs4, requests

# ------------------- E-mail list ------------------------
toAddress = ['example1@email.com','example2@email.com']
# --------------------------------------------------------

#Download page
getPage = requests.get('https://www.catalog.update.microsoft.com/Search.aspx?q=KB4598457')
getPage.raise_for_status() #if error it will stop the program

#Parse text for target word
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
foods = menu.select('.resultsbottomBorder.resultspadding')

the_one = '2021-07' # This is the name of the food you are looking for
flength = len(the_one)
available = False

for food in foods:
    for i in range(len(food.text)):
        chunk = food.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

if available == True:
    print('found')
else:
    print('not found')
