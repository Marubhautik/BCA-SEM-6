import smtplib
import ssl

class Mail:

    def __init__(self):
        self.port =465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "parmarchandu7058@gmail.com"
        self.password = ''

    def send(self,emails,subject,content):
        ssl_context = ssl.create_default_context()
        sevice = smtplib.SMTP_SSL(self.smtp_server_domain_name,self.port,context=ssl_context)
        sevice.login(self.sender_mail,self.password)

        for email in emails:
            result = sevice.sendmail(self.sender_mail,email,f"Subject:{subject}\n{content}")
            sevice.quit()
# if __name__=='__main__':
mails= input("Enter emails:").split()
subject = input("Enter subject: ")
content = input("enter content: ")
mail = Mail()
mail.send(mails,subject,content)

'''Enter emails:marubhautik97@gmail.com
Enter subject: bhhhhhhdf
enter content: fsda'''