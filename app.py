import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read('settings.ini')


law_url=Config.get('Remote','law_html_url')
print('will extract sections and articles from ' + law_url)

