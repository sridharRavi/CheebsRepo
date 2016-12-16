import smtplib;
#Please turn on your internet Connection during this progam
print "Your Email server must be in the form of smtp.email_service.com";
services=['smtp.gmail.com','smtp.mail.yahoo.com','smtp.mail.outlook.com','smtp.mail.att.net','smtp.comcast.net','smtp.verizon.net'];
print "various email services include";
print services;
my_Email_Server=raw_input("enter your corresponding email server");
smtp_values={'smtp.gmail.com':'587','smtp.mail.yahoo.com':'587','smtp.mail.outlook.com':'587','smtp.mail.att.net':'465','smtp.comcast.net':'587','smtp.verizon.net':'587'};
smtpObj=smtplib.SMTP(my_Email_Server,int(smtp_values[my_Email_Server]));
#if a problem arises over the previous function,Then use SSL with port number 465
#smtObj=smtplib.SMTP_SSL('server',port_num);
#This oddly named function is used to initiate a 'conversation' with your smtp server;
smtpObj.ehlo();
#The TLS encryption gets started!!
smtpObj.starttls();
print "carefully Enter your email and password please"
email_address=raw_input("enter your mail address");
my_password=raw_input("enter your password");
#NEVER LEAVE YOUR PASSWORD IN AN UNENCRYPTED FILE LIKE THIS OR LEAVE IT IN A COMMENT!!
smtpObj.login(email_address,my_password);
# if you are using a gmail account,an SMTP.AuthenticationError might occur.Log into your browser and change the settings to allow access to less secure apps
#visit this page 'https://www.google.com/settings/security/lesssecureapps' to turn of your settings
#other email services please visit the corresponding mail support page!!
recv_address=raw_input("enter the recipient's address");
print "The syntax should be 'subject:content' followed by '\n'";
content=raw_input("enter the message you want to send!!");
smtpObj.sendmail(email_address,recv_address,content);
smtpObj.quit();
#Coded by Sridhar Cheebu