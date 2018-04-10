import sys


class Commission(object):

    __hostPrice = 25
    __monitorPrice = 30
    __peripheralsPrice = 45

    def __init__(self, hosts, monitor, peripherals):
        self.qd = 1
        self.__hosts = hosts
        self.__monitor = monitor
        self.__peripherals = peripherals

    def get_commission(self):
        return Commission.__hostPrice*self.__hosts + Commission.__monitorPrice * self.__monitor +\
               Commission.__peripheralsPrice * self.__peripherals


if __name__ == "__main__":
    temp = Commission(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    print(temp.get_commission())
