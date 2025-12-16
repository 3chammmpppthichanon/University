using AbstractFactory.Product;
using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.ConcreteProduct.Handlebar
{
    public class CafeRacerHandlebar : IHandlebar
    {
        public bool IsClipOn { get; set; }
        public string ModelName { get; set; }
        public float Weight { get; set; }
        public string Material { get; set; }

        public CafeRacerHandlebar(string modelName, float weight, string material, bool isClipOn)
        {
            ModelName = modelName;
            Weight = weight;
            Material = material;
            IsClipOn = isClipOn;
        }

        public void GetDescription()
        {
            Console.WriteLine("--- Cafe racer handlebar description ---");
            Console.WriteLine($"Handlebar Model: {ModelName}, Material: {Material}, Weight: {Weight}kg, Is Clip-On: {IsClipOn}");
            Console.WriteLine("--------------------------------");
        }
    }
}
