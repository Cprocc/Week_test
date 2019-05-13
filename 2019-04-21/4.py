class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ll = words
        self.cur = ''

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.cur += letter
        for item in range(len(self.ll)):
            lens = len(self.ll[item])
            if self.cur[len(self.cur)-lens:] == self.ll[item]:
                return True
        return False


if __name__ == '__main__':
    ss = StreamChecker(["cd","f","kl"])
    print(ss.query('c'))
    print(ss.query('f'))
    print(ss.query('k'))
    print(ss.query('l'))
