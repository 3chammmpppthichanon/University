using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bridge
{
    public class SyntheticRubber : IRubberMaterial
    {
        // Properties
        public string ChemicalComposition { get; set; }

        // Implementing IRubberMaterial properties
        public string TypeTire { get; set; }
        public int Durability { get; set; }
        public decimal CostPerKg { get; set; }
        public int Density { get; set; }

        // Default constructor
        public SyntheticRubber()
        {
            ChemicalComposition = "SBR";
            TypeTire = "Synthetic Rubber";
            Durability = 85;
            CostPerKg = 1.80m;
            Density = 940;
        }
        // Constructor parameters
        public SyntheticRubber(string chemicalComposition, string typeTire, int durability, decimal cosPerKg, int density)
        {
            ChemicalComposition = chemicalComposition;
            TypeTire = typeTire;
            Durability = durability;
            CostPerKg = cosPerKg;
            Density = density;
        }

        // Methods
        public void GetDetails()
        {
            Console.WriteLine("=== Synthetic Rubber Details ===");
            Console.WriteLine(
                $"Type: {TypeTire}, Durability: {Durability}/100, CostPerKg: ${CostPerKg:F2}, " +
                $"Density: {Density} kg/m^3, Chemical Composition: {ChemicalComposition}");
        }
        public decimal CalculateWeight(decimal volume)
        {
            // Weight = Density × Volume
            return (Density * volume);
        }
    }
}
