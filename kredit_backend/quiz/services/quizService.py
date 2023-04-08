from abc import ABC, abstractmethod

class QuizService(ABC):
    @abstractmethod
    def getAllQuizOfAUser(self,userId):
        pass