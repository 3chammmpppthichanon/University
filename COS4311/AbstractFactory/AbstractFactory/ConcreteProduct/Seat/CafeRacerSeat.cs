using AbstractFactory.Product;
using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.ConcreteProduct.Seat
{
    public class CafeRacerSeat: ISeat
    {
        public bool HasCowl { get; set; } // ตูดมด
        public int SeatingCapacity { get; set; }
        public string Color { get; set; }
        public string Material { get; set; }

        public CafeRacerSeat(bool hascowl, int seatingCapacity, string color, string material)
        {
            HasCowl = hascowl;
            SeatingCapacity = seatingCapacity;
            Material = material;
            Color = color;
        }

        public void GetDescription()
        {
            Console.WriteLine("--- Cafe racer seat description ---");
            Console.WriteLine($"Cafe racer seat, Has cowl {HasCowl}, Seating capacity: {Material}, Color: {Color}, Material: {Material}");
            Console.WriteLine("--------------------------------");
        }
    }
}
