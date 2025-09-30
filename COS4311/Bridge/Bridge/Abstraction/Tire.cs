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
        public IRubberMaterial RubberMaterial { get; set; }
        public decimal WearFactor { get; set; } = 1.0m;

        // Abstract Methods
        //public abstract string GetDetail();
        //Console.WriteLine($"Price: {Price} - Size: {Size} - Maxspeed: {MaxSpeed} - Weight: {Weight} - Brand: {Brand} {RubberMaterial.GetDetails()}");

        public virtual string GetDetail()
        {
            Console.WriteLine("\n---Material---");
            RubberMaterial.GetMaterial();
            return $"({Brand}) - {Size}\" - Max {MaxSpeed} km/h - {Weight:F2} kg - ${Price:F2}";
        }
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
