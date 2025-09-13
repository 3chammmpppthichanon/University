using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite.Leaf
{
    public class Garen : Hero
    {
        public int AttackDamage { get; set; }
        public int Armor { get; set; }
        public int Health { get; set; }

        public Garen(string skill, int attackDamage, int armor, int health, int mana, int cost, int cooldown, string range)
            : base(skill, mana, cost, cooldown, range)
        {
            AttackDamage = attackDamage;
            Armor = armor;
            Health = health;
        }

        public override int TotalPower() => AttackDamage;

        public override bool CanCast(int currentMana)
        {
            return currentMana >= Mana && Health > (Health * 0.2);
        }

        public override void DisplayInfo()
        {
            Console.WriteLine("Garen Info:");
            Console.WriteLine($"  Skill         : {Skill}");
            Console.WriteLine($"  Attack Damage : {AttackDamage}");
            Console.WriteLine($"  Armor         : {Armor}");
            Console.WriteLine($"  Health        : {Health}");
            Console.WriteLine($"  Mana Cost     : {Mana}");
            Console.WriteLine($"  Gold Cost     : {Cost}");
            Console.WriteLine($"  Cooldown      : {Cooldown} sec");
            Console.WriteLine($"  Range         : {Range}");
            Console.WriteLine($"  Total Power   : {TotalPower()}");
        }
    }
}
