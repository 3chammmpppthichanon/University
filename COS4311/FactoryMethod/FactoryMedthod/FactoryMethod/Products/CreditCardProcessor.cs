using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Products
{
    public class CreditCardProcessor : IPaymentProcessor
    {
        public string PaymentMethodName { get; set; }
        public decimal TransactionFee { get; set; }
        public string CardNumber { get; set; }
        public string ExpiryDate { get; set; }

        public void ValidatePayment(string details)
        {
            var parts = details.Split(",");
            CardNumber = parts[0];
            ExpiryDate = parts[1];
            Console.WriteLine($"[{PaymentMethodName}] Validating card number {CardNumber}, expiry {ExpiryDate}");
        }

        public bool AuthorizePayment()
        {
            Console.WriteLine($"[{PaymentMethodName}] Authorizing credit card...");
            return true;
        }

        public void ProcessPayment(decimal amount)
        {
            var fee = amount + TransactionFee;
            Console.WriteLine($"[{PaymentMethodName}] Processing payment {amount:C}, fee {fee:C}");
        }

        public string GetReceipt()
        {
            return $"Receipt: Paid via {PaymentMethodName}, fee rate {TransactionFee:P}";
        }
    }
}
