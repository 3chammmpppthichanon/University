using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace FactoryMethod
{
    // Product
    public interface IChampion
    {
        public string Name { get; set; }
        public int Cost { get; set; }
        public List<string> Traits { get; set; }
        public void CastAbility();
    }

    // Concrete Products 
    public class Aatrox : IChampion
    {
        public string Name { get; set; } = "Aatrox";
        public int Cost { get; set; } = 1;
        public List<string> Traits { get; set; } = new List<string> { "Mighty Mech", "Heavyweight", "Juggernaut" };

        public void CastAbility()
        {
            Console.WriteLine($"{Name} is casting");
        }
    }

    public class Ahri : IChampion
    {
        public string Name { get; set; } = "Ahri";
        public int Cost { get; set; } = 1;
        public List<string> Traits { get; set; } = new List<string> { "Star Guardian", "Sorcerer" };

        public void CastAbility()
        {
            Console.WriteLine($"{Name} is casting");
        }
    }

    // Factory Method
    public abstract class ChampionFactory()
    {
        public abstract IChampion CreateChampion();
    }

    // Concrete Creators
    public class AatroxFactory : ChampionFactory
    {
        public override IChampion CreateChampion()
        {
            return new Aatrox();
        }
    }

    public class AhriFactory : ChampionFactory
    {
        public override IChampion CreateChampion()
        {
            return new Ahri();
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            ChampionFactory aatroxFactory = new AatroxFactory();
            ChampionFactory ahriFactory = new AhriFactory();

            IChampion aatrox = aatroxFactory.CreateChampion();
            IChampion ahri = ahriFactory.CreateChampion();

            Console.WriteLine($"Champion: {aatrox.Name}, Cost: {aatrox.Cost}, Traists: {string.Join(", ", aatrox.Traits)}"); 
            Console.WriteLine($"Champion: {ahri.Name}, Cost: {ahri.Cost}, Traists: {string.Join(", ", ahri.Traits)}");
        }
    }
}