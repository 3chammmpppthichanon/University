using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public class CityTire : Tire
    {
        public int NoiseLevel { get; set; } // dB
        public decimal FuelEfficiencyFactor { get; set; } // %
        public CityTire(IRubberMaterial rubberMaterial,
                    int size = 17, int maxSpeed = 160, decimal weight = 8.0m, string brand = "Angel City")
        {
            Price = 1000.00m;
            NoiseLevel = 65;
            FuelEfficiencyFactor = 5.0m;
            Size = size;
            MaxSpeed = maxSpeed;
            Weight = weight;
            Brand += brand;
            RubberMaterial = rubberMaterial;
            WearFactor = 0.95m;
        }

        public override string GetDetail()
            => $"Noise level: {NoiseLevel} - Fuel efficiency factor: {FuelEfficiencyFactor}" + base.GetDetail();

        public override string GetRecommendedUsage()
            => "Recommended for city use, smooth roads, moderate speeds, frequent braking/acceleration. Good grip in both dry and wet normal road conditions";

        public override decimal CalculateLifeSpan(int drivingHours)
        {
            decimal life = BaseLifeHours() - drivingHours;
            return life < 0 ? 0 : life;
        }
    }
}
