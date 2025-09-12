using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public interface IRubberMaterial
    {
        // Properties
        public string TypeTire { get; set; }
        public int Durability { get; set; }
        public decimal CostPerKg { get; set; }
        public int Density { get; set; }

        // Method
        public void GetMaterial();
        decimal CalculateWeight(decimal volume);
    }
}
