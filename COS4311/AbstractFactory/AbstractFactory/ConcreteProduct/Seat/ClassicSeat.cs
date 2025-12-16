using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace AbstractFactory.ConcreteProduct.Seat
{
    public class ClassicSeat
    {
        public string StitchingPattern { get; set; }
        public string Material { get; set; }
        public int SeatingCapacity { get; set; }
        public string Color { get; set; }

        public ClassicSeat(string stitchingPattern, string material, int seatingCapacity, string color)
        {
            StitchingPattern = stitchingPattern;
            Material = material;
            SeatingCapacity = seatingCapacity;
            Color = color;
        }
        public void GetDescription()
        {
            Console.WriteLine("--- Classic seat description ---");
            Console.WriteLine($"Material: {Material}, Color: {Color}, Stitching pattern: {StitchingPattern}, Seating capacity: {SeatingCapacity}");
            Console.WriteLine("--------------------------------");
        }
    }
}
