using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace FactoryMethod.Product
{
    public class Makina : IMotorcycle
    {
        public string ModelName { get; set; }
        public string EngineCC { get; set; }
        public List<string> Accessories { get; set; }
        public Makina()
        {
            ModelName = "Makina";
            EngineCC = "300 CC";
            // จองหน่วยความจำให้ List ก่อนใช้งาน
            Accessories = new List<string>();
        }
        public void Assemble()
        {
            Accessories.Add("Sport Round Mirrors");
            Accessories.Add("Clip-on handlebar");
            Accessories.Add("Sport bike seat");
        }
        public void Test()
        {
            Console.WriteLine($"Testing {ModelName}: Engine... แง๊ววว แง๊ววว");
            Console.WriteLine("Testing Feul injector");
        }
        public void ShowSpecs()
        {
            Console.WriteLine($"[Spec sheet] Model: {ModelName}, Engine: {EngineCC}");
            Console.WriteLine($"Acessories include: {string.Join(", ", Accessories)}");
        }
    }
}
