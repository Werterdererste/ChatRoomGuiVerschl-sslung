import cryptocode


class verschluesslung:

    def __init__(self):
        self.__key = "jh981zhcbn9uca89fgh43uizhgf789qcqhghcbgz8324q93rtgf73WO%//TWi7tqu734qui<sd0o)Z/zugtzzfTR"
        pass

    def Verschluesseln(self, msg):
        msg = cryptocode.encrypt(msg, self.__key)
        print(msg)
        return msg

    def Entschluessln(self, msg):
        msg = cryptocode.decrypt(msg, self.__key)
        return msg


