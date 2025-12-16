using FactoryMethod.Creator;

namespace FactoryMethod 
{
    public class Program
    {
        public static void Main(string[] args)
        {
            MotorcycleFactory motorcycle = new CentaurFactory();
            Console.WriteLine("Client: Ordering a motorcycle...");
            motorcycle.OrderMotocycle();

            motorcycle = new MakinaFactory();
            Console.WriteLine("Client: Ordering a motorcycle...");
            motorcycle.OrderMotocycle();
        }
    }
}