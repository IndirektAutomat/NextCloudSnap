import argparse
import subprocess

def getDomains(rawConfig):
    parsedByNewLine = rawConfig.split('\n')
    for element in parsedByNewLine:
        if('RemoteDomain:' in element):
            domainName = element.replace(' ', '').split(':')[1]
        elif('RemoteIP' in element)
            domainIP = element.replace(' ', '').split(':')[1]
    return(domainName, domainIP)

def main(): 
    print('\u001b[32;1mStarting Install...\n\u001b[0m')
    print('by: ' + '\u001b[34;1m Indirekt' + '\u001b[33;1m Automat \u001b[0m\n\n')

    subprocess.call(['snap', 'install', 'nextcloud'])
    askAdminPass = input('What should the Admin password be?  > ')
    subprocess.call(['nextcloud.manual-install', 'admin', askAdminPass])




if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description='Automation Script for the Installation of NextCloud through the Snap Package Manager by:\u001b[34;1m Indirekt\u001b[33;1m Automat \u001b[0m')
    parser.add_argument('--remoteDomain', nargs='?', help='Take credentials from config file for ')
    args = parser.parse_args()
    main(args)