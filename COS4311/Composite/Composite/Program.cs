using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var root = new Category("All Products");

            var shoes = new Category("Shoes");
            var keyboards = new Category("Keyboards");


            shoes.Add(new Product("Ultraboost 22", "Adidas", 6800m, 1));
            shoes.Add(new Product("Air Max 97", "Nike", 7200m, 2));

            
            keyboards.Add(new Product("K70 RGB", "Corsair", 3990m, 1));
            keyboards.Add(new Product("BlackWidow V3", "Razer", 3290m, 1));

            root.Add(shoes);
            root.Add(keyboards);

            root.Display();
            Console.WriteLine($"Grand total: {root.CalculateTotalPrice():0.00}");
        }
    }
}