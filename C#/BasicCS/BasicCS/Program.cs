using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Runtime.Versioning;
using System.Text;
using System.Threading.Tasks;

namespace BasicCS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Display(fname: "Thichanon", lname: "Sompetch");
        }

        static void Display(string fname, string lname)
        {
            Console.WriteLine($"This is my name -> {fname} {lname}");
            Console.ReadKey();
        }
    }
}
