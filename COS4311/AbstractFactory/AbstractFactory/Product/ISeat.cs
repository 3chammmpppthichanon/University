using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.Product
{
    public interface ISeat
    {
        public string Material { get; }
        public string Color { get; }
        public int SeatingCapacity { get; }

        public void GetDescription();
    }
}
