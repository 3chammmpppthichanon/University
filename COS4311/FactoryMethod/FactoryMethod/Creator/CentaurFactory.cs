using System;
using System.Collections.Generic;
using System.Text;
using FactoryMethod.Product;

namespace FactoryMethod.Creator
{
    public class CentaurFactory : MotorcycleFactory
    {
        public override IMotorcycle CreateMotorcycle()
        {
            return new Centaur();
        }
    }
}
