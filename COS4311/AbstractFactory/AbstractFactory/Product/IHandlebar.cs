using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.Product
{
    public interface IHandlebar
    {
        public string ModelName { get;}
        public string Material { get; }
        public float Weight { get; }

        public void GetDescription();

    }
}
