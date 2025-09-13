using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite.Leaf
{
    public class Ezreal : Hero
    {
        public int PhysicalDamage { get; set; }
        public int MagicDamage { get; set; }

        public Ezreal(string skill, int physicalDamage, int magicDamage, int mana, int cost, int cooldown, string range)
            : base(skill, mana, cost, cooldown, range)
        {
            PhysicalDamage = physicalDamage;
            MagicDamage = magicDamage;
        }

        public override int TotalPower() => PhysicalDamage + MagicDamage;

        public override void DisplayInfo()
        {
            Console.WriteLine("Ezreal Info:");
            Console.WriteLine($"  Skill          : {Skill}");
            Console.WriteLine($"  Physical Damage: {PhysicalDamage}");
            Console.WriteLine($"  Magic Damage   : {MagicDamage}");
            Console.WriteLine($"  Mana Cost      : {Mana}");
            Console.WriteLine($"  Gold Cost      : {Cost}");
            Console.WriteLine($"  Cooldown       : {Cooldown} sec");
            Console.WriteLine($"  Range          : {Range}");
            Console.WriteLine($"  Total Power    : {TotalPower()}");
        }
    }
}
