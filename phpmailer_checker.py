#!/usr/bin/python
#PHPMailer Version Checker
#By Jason Bernier
#www.jasonbernier.com
#https://github.com/jasonbernier/phpmailer-checker
#This just checks a URL that the user inputs for PHPMailer versions 5.2.16 through 5.2.18 and reports a match.

import urllib2
import re

def checker(url_input):
   webtext = urllib2.urlopen(url_input).read()
   if bool(re.search(r'5\.2\.(?:0|1)[0-8]', webtext)):
      print url_input + ' appears to have PHPMailer installed!'
      print 'The version reported as being installed is '
      print webtext
      print 'Check https://www.exploit-db.com/exploits/40969/ or https://www.exploit-db.com/exploits/40974/ for a possible exploit'
   else:
      print "This version DOES NOT appear to be vulnerable. The current version installed is " + webtext
      
def main():
   print "PHPMailer Checker"
   print "By Jason Bernier" + '\n'
   
   while True:
      url_input = raw_input("Enter your URL to test for PHP mailer - EX: http://www.yoursite.com\n")
      if 'http://' in url_input[:7] or 'https://' in url_input[:8]:
         break
   if bool(re.search(r'/VERSION$', url_input)):
      checker(url_input)
   else: 
      checker(url_input + "/VERSION")
        
if __name__ == "__main__":
   main()
