using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod.Product
{
    public class Centaur : IMotorcycle
    {
        public string ModelName { get; set; }
        public string EngineCC { get; set; }
        public List<string> Accessories { get; set; }
        public Centaur()
        {
            ModelName = "Centaur";
            EngineCC = "150 CC";

            // จองหน่วยความจำให้ List ก่อนใช้งาน
            Accessories = new List<string>();
        }

        public void Assemble()
        {
            Accessories.Add("Class Round Mirrors");
            Accessories.Add("Clubman handlebar");
            Accessories.Add("Cafe racer seat");
        }

        public void Test()
        {
            Console.WriteLine($"Testing {ModelName}: Engine... แง๊นนน แง๊นนน");
        }
        public void ShowSpecs()
        {
            Console.WriteLine($"[Spec sheet] Model: {ModelName}, Engine: {EngineCC}");
            Console.WriteLine($"Acessories include: {string.Join(", ", Accessories)}");
        }
    }
}