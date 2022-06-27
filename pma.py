import os,requests,random,threading,time,sys,ctypes,re,urllib3
from multiprocessing.dummy import Pool,Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,Style,init
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
Folder('result')

urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path =  str(sys.argv[0]).split('\\')
    exit('\n  [!] python '+path[len(path)-1]+' list.txt')

def pma(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/phpMyAdmin/','/phpmyadmin/','/PMA/','/pma/','/mydb/','/dbadmin/','/mysql/','/myadmin/','/phpmyadmin2/','/phpMyAdmin2/','/phpMyAdmin-2/','/php-my-admin/','/phpMyAdmin-2.2.3/','/phpMyAdmin-2.2.6/','/phpMyAdmin-2.5.1/','/phpMyAdmin-2.5.4/','/phpMyAdmin-2.5.5-rc1/','/phpMyAdmin-2.5.5-rc2/','/phpMyAdmin-2.5.5/','/phpMyAdmin-2.5.5-pl1/','/phpMyAdmin-2.5.6-rc1/','/phpMyAdmin-2.5.6-rc2/','/phpMyAdmin-2.5.6/','/phpMyAdmin-2.5.7/','/phpMyAdmin-2.5.7-pl1/','/phpMyAdmin-2.6.0-alpha/','/phpMyAdmin-2.6.0-alpha2/','/phpMyAdmin-2.6.0-beta1/','/phpMyAdmin-2.6.0-beta2/','/phpMyAdmin-2.6.0-rc1/','/phpMyAdmin-2.6.0-rc2/','/phpMyAdmin-2.6.0-rc3/','/phpMyAdmin-2.6.0/','/phpMyAdmin-2.6.0-pl1/','/phpMyAdmin-2.6.0-pl2/','/phpMyAdmin-2.6.0-pl3/','/phpMyAdmin-2.6.1-rc1/','/phpMyAdmin-2.6.1-rc2/','/phpMyAdmin-2.6.1/','/phpMyAdmin-2.6.1-pl1/','/phpMyAdmin-2.6.1-pl2/','/phpMyAdmin-2.6.1-pl3/','/phpMyAdmin-2.6.2-rc1/','/phpMyAdmin-2.6.2-beta1/','/phpMyAdmin-2.6.2-rc1/','/phpMyAdmin-2.6.2/','/phpMyAdmin-2.6.2-pl1/','/phpMyAdmin-2.6.3/','/phpMyAdmin-2.6.3-rc1/','/phpMyAdmin-2.6.3/','/phpMyAdmin-2.6.3-pl1/','/phpMyAdmin-2.6.4-rc1/','/phpMyAdmin-2.6.4-pl1/','/phpMyAdmin-2.6.4-pl2/','/phpMyAdmin-2.6.4-pl3/','/phpMyAdmin-2.6.4-pl4/','/phpMyAdmin-2.6.4/','/phpMyAdmin-2.7.0-beta1/','/phpMyAdmin-2.7.0-rc1/','/phpMyAdmin-2.7.0-pl1/','/phpMyAdmin-2.7.0-pl2/','/phpMyAdmin-2.7.0/','/phpMyAdmin-2.8.0-beta1/','/phpMyAdmin-2.8.0-rc1/','/phpMyAdmin-2.8.0-rc2/','/phpMyAdmin-2.8.0/','/phpMyAdmin-2.8.0.1/','/phpMyAdmin-2.8.0.2/','/phpMyAdmin-2.8.0.3/','/phpMyAdmin-2.8.0.4/','/phpMyAdmin-2.8.1-rc1/','/phpMyAdmin-2.8.1/','/phpMyAdmin-2.8.2/','/sqlmanager/','/mysqlmanager/','/p/m/a/','/PMA2005/','/pma2005/','/phpmanager/','/php-myadmin/','/phpmy-admin/','/webadmin/','/sqlweb/','/websql/','/webdb/','/mysqladmin/','/mysql-admin/','/mya/']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req = x.get(url, headers=head)
            if "phpmyadmin.net" in req.text :
                print(fw+"["+fg+"BX"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found PMA")
                open("result/pma.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"BX"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found PMA")
        except :
            pass

if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """
          \\\|||||//         
          (  O O  )          
|--ooO-------(_)------------|
|                           |
|    phpMyAdmin Scanner~    |
|                           |
|----------------------Ooo--|
          |__||__|           
           ||  ||            
          ooO  Ooo           
\n"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
    p = Pool(100)
    p.map(pma, target)
    p.close()
    p.join()
    print("\n")
    print(fr+"|-------------------------------------|")
    print(fr+"|             "+fw+"DONE MASZEH"+fr+"             |")
    print(fr+"|-------------------------------------|")