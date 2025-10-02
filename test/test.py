from urllib.parse import urlparse, parse_qs

def main():

    url = "https://midominio.com/producto?utm_source=google&utm_medium=cpc&utm_campaign=blackfriday&utm_term=zapatillas&utm_content=banner1"

    def create_from_url(url):
        """
        Recibe una URL con parámetros UTM y crea un registro en utm.utm
        """
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)

        # Extrae los parámetros UTM (pueden venir como lista en parse_qs)
        values = {
            'source': params.get('utm_source', [''])[0].lower().strip(),
            'medium': params.get('utm_medium', [''])[0].lower().strip(),
            'campaing': params.get('utm_campaign', [''])[0].lower().strip(),
            'term': params.get('utm_term', [''])[0].lower().strip(),
            'content': params.get('utm_content', [''])[0].lower().strip(),
        }
        return values

    print(create_from_url(url))


if __name__ == "__main__":
    main()
