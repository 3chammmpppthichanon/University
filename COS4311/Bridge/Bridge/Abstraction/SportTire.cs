using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public class SportTire : Tire
    {
        public int GripLevel { get; set; } // 1 - 10 ระดับ
        public decimal CorneringStability { get; set; } // %
        public SportTire(IRubberMaterial rubberMaterial,
                     int size = 17, int maxSpeed = 220, decimal weight = 8.5m, string brand = "Diablo Rosso")
        {
            GripLevel = 10;
            CorneringStability = 95.5m;
            Price = 2000.00m;
            Size = size;
            MaxSpeed = maxSpeed;
            Weight = weight;
            Brand += brand;
            RubberMaterial = rubberMaterial;
            WearFactor = 0.85m; // High grip but wears faster than touring tires
        }

        public override string GetDetail()
            => $"Grip {GripLevel} - Cornering stability {CorneringStability} - {base.GetDetail()}";

        public override string GetRecommendedUsage()
            => "Suitable for sporty driving, frequent cornering, high road grip, designed for superior handling and control";

        public override decimal CalculateLifeSpan(int drivingHours)
        {
            decimal life = BaseLifeHours() - drivingHours;
            return life < 0 ? 0 : life;
        }
    }
}
