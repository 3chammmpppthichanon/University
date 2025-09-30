using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace FactoryMethod
{

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