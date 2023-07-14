from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class Sender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def format(self):
        pass


class IMSender(Sender):
    def format(self):
        return ''.join(["I'm ", self.sender])


class Receiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def format(self):
        pass


class IMReceiver(Receiver):
    def format(self):
        return ''.join(["I'm ", self.receiver])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"



# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)
content = MyContent('Hello, there!')
receiver = IMReceiver('james')
sender = IMSender('qmal')
email = Email('IM')
email.set_sender(sender)
email.set_receiver(receiver)

email.set_content(content)
print(email)