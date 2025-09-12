using System;

namespace Bridge
{
    public class Program
    {
        static void Main(string[] args)
        {
            IRubberMaterial naturalRubber = new NaturalRubber();
            IRubberMaterial syntheticRubber = new SyntheticRubber();

            Tire cityTire = new CityTire(syntheticRubber);
            Console.WriteLine(cityTire.GetRecommendedUsage());
            Console.WriteLine(cityTire.GetDetail()); // Display tire details
            Console.WriteLine(cityTire.CalculateTotalCost());
            Console.WriteLine($"Life span after 150 hours: {cityTire.CalculateLifeSpan(150)} hours");
            Console.WriteLine($"Total cost: ${cityTire.CalculateTotalCost():F2}");
            Console.WriteLine("---------------------------------------------------");


            Console.WriteLine("---------------------------------------------------");

            Tire touringTire = new TouringTire(naturalRubber);
            Console.WriteLine(touringTire.GetRecommendedUsage());
            Console.WriteLine(touringTire.GetDetail()); // Display tire details
            Console.WriteLine(touringTire.CalculateTotalCost());
            Console.WriteLine($"Life span after 2000 hours: {touringTire.CalculateLifeSpan(2000)} hours");
            Console.WriteLine($"Total cost: ${touringTire.CalculateTotalCost():F2}");
            Console.WriteLine("---------------------------------------------------");

            Tire sportTire = new SportTire(naturalRubber);
            Console.WriteLine(sportTire.GetRecommendedUsage());
            Console.WriteLine(sportTire.GetDetail());// Display tire details
            Console.WriteLine(sportTire.CalculateTotalCost());
            Console.WriteLine($"Life span after 120 hours: {sportTire.CalculateLifeSpan(150)} hours");
            Console.WriteLine($"Total cost: ${sportTire.CalculateTotalCost():F2}");
            Console.WriteLine("---------------------------------------------------");
        }
    }
}