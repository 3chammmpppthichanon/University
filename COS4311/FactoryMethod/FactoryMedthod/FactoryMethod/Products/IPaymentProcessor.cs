using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;

namespace FactoryMethod.Products
{
    public interface IPaymentProcessor
    {
        public string PaymentMethodName { get; set; }
        public decimal TransactionFee {  get; set; }

        void ValidatePayment(string details);
        bool AuthorizePayment();
        void ProcessPayment(decimal amount);
        string GetReceipt();
    }   
}
