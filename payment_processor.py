from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def pay(self, amount): pass

    @abstractmethod
    def refund(self, amount): pass

class PayPal(IPayment):
    def pay(self, amount):
        print("rediricting to paypal")
    
    def refund(self, amount):
        print("refund via paypal")

class CryptoPayment(IPayment):
    def pay(self, amount):
        print("rediricting to CryptoPayment")
    
    def refund(self, amount):
        print("refund via CryptoPayment")

class PaymentService:
    def checkout(self, payment_method: IPayment, amount):
        try:
            self.payment_method.pay(amount)
        except Exception:
            self.payment_method.refund(amount)
    
class PaymentFactory:
    def create(self, method_type: str) -> IPayment:
        if method_type == "paypal":
            return PayPal()
        elif method_type == "crypto":
            return CryptoPayment()

factory = PaymentFactory()
payment = factory.create("paypal")

service = PaymentService()
service.checkout(payment, 100)