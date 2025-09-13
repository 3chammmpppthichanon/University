using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Composite.Composite
{
    public class Trait : ITFT
    {
        public List<ITFT> Members { get; set; }
        public string Skill { get; set; }

        public Trait(string skill)
        {
            Members = new List<ITFT>();
            Skill = skill;
        }

        public void Add(ITFT member)
        {
            Members.Add(member);
        }

        public int TotalPower()
        {
            int sum = 0;
            foreach (var member in Members)
            {
                // ใช้ reflection เพื่อเรียก TotalPower ถ้ามี
                var method = member.GetType().GetMethod("TotalPower");
                if (method != null)
                {
                    sum += (int)method.Invoke(member, null);
                }
            }
            return sum;
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"Trait Skill: {Skill}\n");
            foreach (var member in Members)
            {
                member.DisplayInfo();
                Console.WriteLine("");
            }
            Console.WriteLine($"Total Team Power: {TotalPower()}");
        }
    }
}