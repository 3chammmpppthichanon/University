using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public abstract class Tire
    {
        // Properties
        public decimal Price { get; set; }
        public int Size { get; set; }
        public int MaxSpeed { get; set; }
        public decimal Weight { get; set; }
        public string Brand { get; set; } = "Pirelli";
        protected IRubberMaterial RubberMaterial { get; set; }
        protected decimal WearFactor { get; set; } = 1.0m;

        // Abstract Methods
        public abstract string GetDetail();
        public abstract string GetRecommendedUsage();
        public abstract decimal CalculateLifeSpan(int drivingHours);
        public virtual decimal CalculateTotalCost()
        {
            decimal materialCost = RubberMaterial.CostPerKg * Weight;
            return Price + materialCost;
        }
        protected decimal BaseLifeHours()
        {
            return RubberMaterial.Durability * 50m * WearFactor;
        }
    }
}
