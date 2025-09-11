using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public class TouringTire : Tire
    {
        public int HeatResistance { get; set; }

        public TouringTire(IRubberMaterial rubberMaterial,
                       int size = 17, int maxSpeed = 180, decimal weight = 9.0m, string brand = "Scorpion")
        {
            HeatResistance = 120;
            Price = 1500.00m;
            Size = size;
            MaxSpeed = maxSpeed;
            Weight = weight;
            Brand += brand;
            RubberMaterial = rubberMaterial;
            WearFactor = 1.10m;
        }

        public override string GetDetail()
            => $"({Brand}) - {Size}\" - {RubberMaterial.TypeTire} - ${Price:F2} - Max {MaxSpeed} km/h - HeatResist {HeatResistance}°C";

        public override string GetRecommendedUsage()
            => "Suitable for long-distance driving, extended journeys, constant speed, focuses on comfort, quietness, and longevity";

        public override decimal CalculateLifeSpan(int drivingHours)
        {
            decimal life = BaseLifeHours() - drivingHours;
            return life < 0 ? 0 : life;
        }
    }
}
