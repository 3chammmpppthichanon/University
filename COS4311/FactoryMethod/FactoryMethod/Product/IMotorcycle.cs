using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod.Product
{
    public interface IMotorcycle
    {
        // Properties
        public string ModelName { get; set; }
        public string EngineCC { get; set; }
        public List<string> Accessories { get; set; }

        // Methods
        public void Assemble();
        public void Test();
        public void ShowSpecs();
    }
}
