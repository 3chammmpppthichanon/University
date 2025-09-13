using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite.Leaf
{
    public class Yuumi : Hero
    {
        public int MagicDamage { get; set; }
        public int Heal { get; set; }

        public Yuumi(string skill, int magicDamage, int heal, int mana, int cost, int cooldown, string range)
            : base(skill, mana, cost, cooldown, range)
        {
            MagicDamage = magicDamage;
            Heal = heal;
        }

        public override int TotalPower() => MagicDamage + Heal;

        public override void DisplayInfo()
        {
            Console.WriteLine("Yuumi Info:");
            Console.WriteLine($"  Skill         : {Skill}");
            Console.WriteLine($"  Magic Damage  : {MagicDamage}");
            Console.WriteLine($"  Heal          : {Heal}");
            Console.WriteLine($"  Mana Cost     : {Mana}");
            Console.WriteLine($"  Gold Cost     : {Cost}");
            Console.WriteLine($"  Cooldown      : {Cooldown} sec");
            Console.WriteLine($"  Range         : {Range}");
            Console.WriteLine($"  Total Power   : {TotalPower()}");
        }
    }
}
