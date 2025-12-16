using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.Product

{
    public interface IStallionsPartsFactory
    {
        public IHandlebar CreateHandlebar();
        public ISeat CreateSeat();
    }
}
