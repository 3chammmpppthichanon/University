using FactoryMethod.Product;
using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod.Creator
{
    public class MakinaFactory : MotorcycleFactory
    {
        public override IMotorcycle CreateMotorcycle()
        {
            return new Makina();
        }
    }
}
