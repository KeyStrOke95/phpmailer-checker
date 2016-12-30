#!/usr/bin/python
#PHPMailer Version Checker
#By Jason Bernier
#www.jasonbernier.com
#https://github.com/jasonbernier/phpmailer-checker
#This just checks a URL that the user inputs for PHPMailer versions 5.2.16 through 5.2.18 and reports a match.

import urllib2
import re

print "PHPMailer Checker"
print "By Jason Bernier" + '\n'

url_input = raw_input("Enter your URL to test for PHP mailer - EX: http://www.yoursite.com/VERSION " +'\n')
webtext = urllib2.urlopen(url_input).read()
matches = re.findall('5.2.16|5.2.17|5.2.18', webtext);

if len(matches) == 0:
   print url_input + ' DOES NOT appear to have PHPMailer Installed'
else:
   print url_input + ' appears to have PHPMailer installed!'
   print 'The version reported as being installed is '
   print matches
   print 'Check https://www.exploit-db.com/exploits/40969/ or https://www.exploit-db.com/exploits/40974/ for a possible exploit'