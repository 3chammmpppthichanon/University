using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public class NaturalRubber : IRubberMaterial
    {
        public decimal PurityLevel { get; set; } // Purity level
        public string SourceCountry { get; set; } // Source country

        // Implementing IRubberMaterial properties
        public string TypeTire { get; set; } = "Natural Rubber";
        public int Durability { get; set; }
        public decimal CostPerKg { get; set; }
        public int Density { get; set; }

        // Default constructor
        public NaturalRubber()
        {
            TypeTire = "NaturalRubber";
            Durability = 80;
            CostPerKg = 2.10m;
            Density = 930;
            SourceCountry = "Thailand";
            PurityLevel = 92.5m; // Purity level
        }
        // Constructor parameters
        public NaturalRubber(int durability, decimal costPerKg, int density,
            string scourceCountry, decimal purityLevel, string typeTire = "Natural Rubber")
        {
            TypeTire = typeTire;
            Durability = durability;
            CostPerKg = costPerKg;
            Density = density;
            SourceCountry = scourceCountry;
            PurityLevel = purityLevel; // ความบริสุทธิ์
        }

        // Methods
        public void GetDetails()
        {
            Console.WriteLine($"=== Natural Rubber Details ===");
            Console.WriteLine(
                $"Type: {TypeTire}, Durability: {Durability}/100, " + $"CostPerKg: ${CostPerKg:F2}, Density: {Density} kg/m^3, " +
                $"ScourceCountry: {SourceCountry}, " + $"PurityLevel: {PurityLevel:F1}");
        }
        public decimal CalculateWeight(decimal volume)
        {
            // Weight = Density × Volume
            return (Density * volume);
        }
        public string GetQualityGrade()
        {
            if (PurityLevel >= 95) return "Premium";
            if (PurityLevel >= 85) return "Standard";
            return "Economy";
        }
    }
}
