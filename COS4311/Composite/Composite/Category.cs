using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite
{
    public class Category : IComputerComponent
    {
        public List<IComputerComponent> Catalogs { get; set; }
        public string Name { get; set; }

        public Category(string name)
        {
            Catalogs = new List<IComputerComponent>();
            Name = name;
        }

        public void Add(IComputerComponent catalog)
        {
            Catalogs.Add(catalog);
        }

        public decimal CalculateTotalPrice()
        {
            decimal total = 0m;
            foreach(var catalog in Catalogs)
            {
                total += catalog.CalculateTotalPrice();
            }
            return total;
        }

        public void Display()
        {
            Console.WriteLine($"{Name}, total: {CalculateTotalPrice():0.00}");
            foreach(var catalog in Catalogs)
            {
                catalog.Display();
            }
        }
    }
}
