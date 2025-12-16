using AbstractFactory.Product;
using System;
using System.Collections.Generic;
using System.Text;

namespace AbstractFactory.ConcreteProduct.Handlebar
{
    public class ClassicHandlebar: IHandlebar
    {
        public float RiseHeight { get; set; }
        public string ModelName { get; set; }
        public float Weight { get; set; }
        public string Material { get; set; }

        public ClassicHandlebar(float riseHeight, string modelName, float weight, string material)
        {
            RiseHeight = riseHeight;
            ModelName = modelName;
            Weight = weight;
            Material = material;
        }
        
        public void GetDescription()
        {
            Console.WriteLine("--- Classic handlebar description ---");
            Console.WriteLine($"Handlebar Model: {ModelName}, Material: {Material}, Weight: {Weight}kg, Rise height: {RiseHeight}");
            Console.WriteLine("--------------------------------");
        }
    }
}
