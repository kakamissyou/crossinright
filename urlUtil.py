__author__ = 'Administrator'
import urllib
class myURLOpener(urllib.FancyURLopener):

    # read an URL, with automatic HTTP authentication
    def setpasswd(self, user, passwd):
        self. _user = user
        self. _passwd = passwd

    def prompt_user_passwd(self, host, realm):
        return self._user, self._passwd

#Main
urlopener = myURLOpener()
urlopener.setpasswd("zkteco", "zkeco")
fp = urlopener.open("http://biosecurity.xmzkteco.com/")
print fp.read()