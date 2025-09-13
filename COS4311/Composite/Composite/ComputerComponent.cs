using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite
{
    public abstract class ComputerComponent
    {
        public string name;
        public double price;

        public ComputerComponent(string name, double price)
        {
            this.name = name;
            this.price = price;
        }

        public abstract void Display();
        public abstract double CalculatePrice();
        public abstract void Add(ComputerComponent component);
    }
}
