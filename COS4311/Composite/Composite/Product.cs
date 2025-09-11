using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite
{
    public class Product : IComputerComponent
    {
        public string Name { get; set; }
        public string Brand { get; set; }
        public decimal Price { get; set; }
        public int Quantity { get; set; }

        public Product(string name, string brand, decimal price, int quantity)
        {
            Name = name;
            Brand = brand;
            Price = price;
            Quantity = quantity;
        }

        public decimal CalculateTotalPrice()
        {
            return Price * Quantity;
        }
        public void Display()
        {
            Console.WriteLine($"{Name} ({Brand}) x{Quantity} = {CalculateTotalPrice():0.00}");
        }
    }
}
