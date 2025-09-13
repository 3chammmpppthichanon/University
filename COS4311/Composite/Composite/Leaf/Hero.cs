using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite.Leaf
{
    // Abstract base class for all TFT heroes
    public abstract class Hero : ITFT
    {
        public string Skill { get; set; }
        public int Mana { get; set; }
        public int Cost { get; set; }
        public int Cooldown { get; set; }
        public string Range { get; set; }

        protected Hero(string skill, int mana, int cost, int cooldown, string range)
        {
            Skill = skill;
            Mana = mana;
            Cost = cost;
            Cooldown = cooldown;
            Range = range;
        }

        public abstract void DisplayInfo();
        public abstract int TotalPower();
        public virtual bool CanCast(int currentMana) => currentMana >= Mana;
    }
}
