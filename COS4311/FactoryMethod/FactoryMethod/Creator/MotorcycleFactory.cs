using FactoryMethod.Product;
using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod.Creator
{
    public abstract class MotorcycleFactory
    {
        public abstract IMotorcycle CreateMotorcycle();
        public void OrderMotocycle()
        {
            IMotorcycle bike = CreateMotorcycle();
            bike.Assemble();
            bike.Test();
            bike.ShowSpecs();
        }
    }
}
