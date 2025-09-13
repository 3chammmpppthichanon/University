using System;
using Composite.Composite;
using Composite.Leaf;

namespace Composite
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // สร้างฮีโร่แต่ละตัว
            var yuumi = new Yuumi("Final Chapter", magicDamage: 120, heal: 80, mana: 40, cost: 2, cooldown: 8, range: "Long");
            var garen = new Garen("Judgment", attackDamage: 150, armor: 60, health: 900, mana: 50, cost: 3, cooldown: 10, range: "Melee");
            var ezreal = new Ezreal("Trueshot Barrage", physicalDamage: 110, magicDamage: 100, mana: 60, cost: 4, cooldown: 12, range: "Long");

            // สร้าง Trait Battle Academia
            var battleAcademia = new Trait("Battle Academia champions upgrade their abilities and gain Potential Potential. Potential improves their abilities.");

            // เพิ่มสมาชิก
            battleAcademia.Add(yuumi);
            battleAcademia.Add(garen);
            battleAcademia.Add(ezreal);

            // แสดงข้อมูลกลุ่มและสมาชิก
            battleAcademia.DisplayInfo();
        }
    }
}