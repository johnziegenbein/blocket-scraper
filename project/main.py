import sys

from requests_html import HTMLSession

def main():
    url = 'https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cb=40&cbl1=9&cg=1020&q=passat+hybrid&utrustning_dragkrok=1'
    # FIXME this only retrieves first 40. Add pagination support

    session = HTMLSession()
    r = session.get(url)
    r.html.render()

    if r.status_code == 200:
        divs = r.html.find('div')
        f = filter(lambda n: n.attrs.get('class') == 'styled__SalesInfo-sc-1kpvi4z-20', divs) # FIXME doesnt work
        for fs in f:
            print(fs)

    else:
        sys.exit('Could not retrieve html document')


if __name__ == "__main__":
    main()
